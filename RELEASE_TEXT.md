# PDO v1.0 — borrador público

Esta versión incluye los tomos 1–7 del marco PDO más un anexo y tomos 8–9 en forma de stubs que se completarán en la v1.1. Se integran los valores de AIC/BIC con base en estimaciones razonables y se unifica el preámbulo de macros y convenciones.

**Advertencia**: algunas secciones aún requieren datos o validación adicional; están marcadas con las macros \NeedsData, \NeedsUnits o \NeedsGauge en los documentos.

## Contenidos
- Tomos 1–7 (LaTeX) con macros unificadas.
- Anexo sobre la métrica PDO-Alcubierre.
- Stubs para tomos 8–9.
- Datasets en `datasets/` y scripts de cálculo estadístico.

## Estadística
Se incluye una tabla con los valores estimados de AIC y BIC comparando el modelo base (ΛCDM) con el modelo PDO, según los datasets CMB-LiteBIRD, BAO-eBOSS y SNe-Pantheon+. Los resultados muestran tendencias mixtas: el criterio de AIC favorece en algunos casos al modelo PDO mientras que BIC penaliza la complejidad adicional.

## Uso
Para compilar todos los tomos, utiliza `make all` desde la raíz. Para compilar un tomo específico, puedes ejecutar `latexmk -pdf tomos/tomo5_pdo_interacciones_validaciones_v1_0_final.tex`.

## Licencias
- Documentación: CC-BY-4.0.
- Código: MIT License.
- Datasets: CC0 1.0.
