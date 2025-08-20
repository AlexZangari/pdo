#!/usr/bin/env python3
import argparse, numpy as np, h5py, pathlib, json


def prob_from_field(psi, eps=1e-12):
    amp2 = np.abs(psi)**2
    s = amp2.sum()
    return amp2/s if s>eps else np.full_like(amp2, 1.0/amp2.size)


def shannon(p):
    p = p[p>0]
    return float(-(p*np.log(p)).sum())


def load_any(path):
    path = pathlib.Path(path)
    if path.suffix == ".npz":
        z = np.load(path)
        return z["psi"], z["t"]
    elif path.suffix in (".h5", ".hdf5"):
        with h5py.File(path, "r") as f:
            return f["psi"][...], f["t"][...]
    raise ValueError("Formato no reconocido (use .npz o .h5)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help="NPZ/HDF5 con psi(x,t)")
    ap.add_argument("--ref-window", type=int, default=10,
                    help="ventana inicial para S_ref (default=10 frames)")
    ap.add_argument("--out", default="entropy_sp.csv")
    args = ap.parse_args()

    psi, t = load_any(args.file)   # psi: [T, ...]
    T = psi.shape[0]
    S = np.zeros(T, dtype=float)

    for k in range(T):
        p = prob_from_field(psi[k].ravel())
        S[k] = shannon(p)

    Sref = S[:min(args.ref_window, T)].mean()
    C = np.exp(-(S - Sref))

    hdr = "t,S_p,DeltaS_p,C\n"
    lines = [f"{t[i]},{S[i]},{S[i]-Sref},{C[i]}" for i in range(T)]
    pathlib.Path(args.out).write_text(hdr + "\n".join(lines))

    meta = {"file": args.file, "S_ref": float(Sref)}
    pathlib.Path(args.out + ".meta.json").write_text(json.dumps(meta, indent=2))
    print(f"OK -> {args.out} (+ .meta.json)")

if __name__ == "__main__":
    main()
