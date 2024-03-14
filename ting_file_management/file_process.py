from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return

    list_text = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_text),
        "linhas_do_arquivo": list_text,
    }

    instance.enqueue(new_dict)
    print(new_dict)


def remove(instance):
    if len(instance._data) == 0:
        return

    removed_item = instance.dequeue()
    print(f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance._data):
        print("Posição inválida", file=sys.stderr)
        return

    item_returned = instance.search(position)
    print(item_returned)
