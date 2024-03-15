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

        for index, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                word_count["ocorrencias"].append({"linha": index})

    words_list = [
        word_count for word_count in words_list if word_count["ocorrencias"]
    ]
    return words_list


def search_by_word(word, instance):
    word_data = exists_word(word, instance)

    for item in word_data:
        for index, file_item in enumerate(instance._data):
            if item["arquivo"] == file_item["nome_do_arquivo"]:
                ocorrencias = item["ocorrencias"]
                words_list = []
                for occurrence in ocorrencias:
                    line_number = occurrence["linha"]
                    line_content = file_item["linhas_do_arquivo"][
                        line_number - 1
                    ]
                    words_list.append(
                        {"linha": line_number, "conteudo": line_content}
                    )
                item["ocorrencias"] = words_list
                break

    return word_data
