from ting_file_management.queue import Queue
import time


def exists_word(word, instance=Queue()):
    words_list = []

    for item in instance._data:
        word_count = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        words_list.append(word_count)

        # Filtrar apenas as linhas que contêm a palavra desejada
        lines_with_word = filter(
            lambda x: word.lower() in x.lower().split(),
            item["linhas_do_arquivo"],
        )

        # Para cada linha com a palavra, adicionar a ocorrência
        for index, line in enumerate(lines_with_word, start=1):
            word_count["ocorrencias"].append({"linha": index})

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
            "ressaltar é fundamental ressaltar que a adoção",
            "de políticas Ressaltar nos obriga",
            "à Ressaltar do levantamento das variáveis envolvidas Fim",
        ],
    }
)
# print("texto 1:   ", exists_word("ressaltar", instance))


start_time = time.time()
exists_word("ressaltar", instance)
end_time = time.time()
original_time = end_time - start_time
