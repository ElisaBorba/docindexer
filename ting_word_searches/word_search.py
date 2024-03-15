from ting_file_management.queue import Queue

from ting_file_management.file_process import process


def exists_word(word, instance=Queue()):
    words_list = []

    for item in instance._data:
        word_count = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        words_list.append(word_count)

        for index, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                word_count["ocorrencias"].append({"linha": index})

    words_list = [
        word_count for word_count in words_list if word_count["ocorrencias"]
    ]
    return words_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
