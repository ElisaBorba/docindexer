from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    instance = PriorityQueue()
    high_priority_value = {
        "nome_do_arquivo": "arquivo_high.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [
            "Acima de tudo",
            "é fundamental ressaltar que a adoção",
            "de políticas descentralizadoras nos obriga",
        ],
    }

    regular_priority_value = {
        "nome_do_arquivo": "arquivo_regular.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            "Acima de tudo",
            "é fundamental ressaltar que a adoção",
            "de políticas descentralizadoras nos obriga",
            "à análise do levantamento das variáveis envolvidas," "Fim",
        ],
    }

    # TESTA PRIORITY
    assert instance.is_priority(high_priority_value)
    assert not instance.is_priority(regular_priority_value)

    # TESTA ENQUEUE
    instance.enqueue(high_priority_value)
    assert instance.high_priority._data == [high_priority_value]

    instance.enqueue(regular_priority_value)
    assert instance.regular_priority._data == [regular_priority_value]

    # TESTA SEARCH
    assert instance.search(0) == high_priority_value
    assert instance.search(1) == regular_priority_value
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        instance.search(2)

    # TESTA DEQUEUE
    instance.dequeue()
    assert len(instance.high_priority._data) == 0
    assert len(instance.regular_priority._data) == 1

    instance.dequeue()
    assert len(instance.high_priority._data) == 0
    assert len(instance.regular_priority._data) == 0
