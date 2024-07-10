#!/bin/bash

# Directorio donde están los archivos .ipynb
DIRECTORIO="assets/jupyter"

# Recorre todos los archivos .ipynb en el directorio
for archivo in "$DIRECTORIO"/*.ipynb; do
  # Extrae el nombre del archivo sin la extensión
  nombre_archivo=$(basename "$archivo" .ipynb)
  
  # Ejecuta el comando jq y guarda el resultado en un nuevo archivo
  jq -M 'del(.metadata.widgets)' "$archivo" > "$DIRECTORIO/$nombre_archivo.fixed.ipynb"
done
