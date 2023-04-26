from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    correct_message = "oi, tudo bem?"
    even_key = 2
    odd_key = 1
    range_key = 20
    wrong_message = 37
    wrong_key = "oi"
    assert encrypt_message(correct_message, even_key) == '?meb odut ,_io'

    assert encrypt_message(correct_message, odd_key) == 'o_?meb odut ,i'

    assert encrypt_message(correct_message, range_key) == '?meb odut ,io'

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(correct_message, wrong_key)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(wrong_message, even_key)
