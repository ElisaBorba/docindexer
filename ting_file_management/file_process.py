from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance=Queue()):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return None

    list_text = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_text),
        "linhas_do_arquivo": list_text,
    }

    instance.enqueue(new_dict)
    print(new_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


instance = Queue()
