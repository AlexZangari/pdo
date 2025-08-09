.PHONY: all
all:
	@for f in $$(ls ../tomos/*.tex); do \
		echo "Compilando $$f"; \
		latexmk -pdf -interaction=nonstopmode -shell-escape $$f; \
		latexmk -c $$f; \
	done
