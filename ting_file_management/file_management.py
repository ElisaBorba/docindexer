import os
import sys


def txt_importer(path_file):
    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None

    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None

    with open(path_file, "r") as file:
        return file.read().split("\n")
