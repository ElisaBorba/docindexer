from ting_file_management.queue import Queue


def exists_word(word, instance=Queue()):
    words_list = []

    for item in instance._data:
        word_count = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        words_list.append(word_count)

        for index, word_to_compare in enumerate(item["linhas_do_arquivo"]):
            if word.lower() == word_to_compare.lower():
                index_line = {"linha": index + 1}
                word_count["ocorrencias"].append(index_line)

    return words_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


instance = Queue()
instance.enqueue(
    {
        "nome_do_arquivo": "texto1.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [
            "Acima de tudo",
            "é fundamental ressaltar que a adoção",
            "de políticas Ressaltar nos obriga",
            "à análise do levantamento das variáveis envolvidas Fim",
        ],
    }
)
print("texto 1:   ", exists_word("ressaltar", instance))

instance.enqueue(
    {
        "nome_do_arquivo": "texto2.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            "Acima de tudo",
            "é fundamental ressaltar que a adoção",
            "de políticas descentralizadoras nos obriga",
            "à análise do levantamento das variáveis envolvidas",
            "Fim",
        ],
    }
)

print("texto 2:   ", exists_word("ressaltar", instance))
