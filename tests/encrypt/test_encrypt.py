from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Teste com key maior que o tamanho da mensagem
    assert encrypt_message("adalberto", 33) == "otreblada"

    # Teste com key ímpar
    assert encrypt_message("adalberto", 3) == "ada_otrebl"

    # Teste com key par
    assert encrypt_message("adalberto", 4) == "otreb_lada"

    # Teste com a Key negativa
    assert encrypt_message("adalberto", -1) == "otreblada"

    # Teste com tipo inválido para message
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message([], 13)

    # Teste com tipo inválido para key
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("", "")
