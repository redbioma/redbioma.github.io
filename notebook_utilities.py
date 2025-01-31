#!/usr/bin/env python3
import os
import subprocess
import shutil

def convert_notebooks_to_html(source_folder, destination_folder):
    """
    Convierte archivos .ipynb a formato HTML y mueve los archivos generados a otra carpeta.

    Parameters:
        source_folder (str): Carpeta donde se encuentran los archivos .ipynb.
        destination_folder (str): Carpeta donde se moverán los archivos convertidos.
    """
    # Asegurarse de que la carpeta de destino existe
    os.makedirs(destination_folder, exist_ok=True)

    # Recorrer los archivos del folder
    for file_name in os.listdir(source_folder):
        if file_name.endswith(".ipynb"):
            full_path = os.path.join(source_folder, file_name)

            # Ejecutar el comando nbconvert para convertir a HTML
            try:
                subprocess.run(
                    ["jupyter", "nbconvert", "--to", "html", full_path],
                    check=True,
                )
                print(f"Convertido: {file_name}")

                # Mover el archivo generado (mismo nombre pero con extensión .html)
                html_file = os.path.splitext(file_name)[0] + ".html"
                generated_file = os.path.join(source_folder, html_file)
                if os.path.exists(generated_file):
                    shutil.move(generated_file, os.path.join(destination_folder, html_file))
                    print(f"Movido: {html_file} a {destination_folder}")
                else:
                    print(f"Archivo HTML no encontrado para: {file_name}")

            except subprocess.CalledProcessError as e:
                print(f"Error al convertir {file_name}: {e}")


def rename_files_in_directory(directory):
    """
    Renombra los archivos en un directorio eliminando la parte ".fixed" del nombre del archivo.

    Parameters:
        directory (str): Carpeta donde se encuentran los archivos a renombrar.
    """
    for file_name in os.listdir(directory):
        if ".fixed" in file_name:
            old_file_path = os.path.join(directory, file_name)
            new_file_name = file_name.replace(".fixed", "")
            new_file_path = os.path.join(directory, new_file_name)

            # Renombrar el archivo
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renombrado: {file_name} -> {new_file_name}")
            except Exception as e:
                print(f"Error al renombrar {file_name}: {e}")

if __name__ == "__main__":
    # Configurar las carpetas fuente y destino
    source_folder = "assets/jupyter/2024-07-ml"
    destination_folder = "assets/html/2024-07-ml"

    convert_notebooks_to_html(source_folder, destination_folder)
    rename_files_in_directory(destination_folder)
