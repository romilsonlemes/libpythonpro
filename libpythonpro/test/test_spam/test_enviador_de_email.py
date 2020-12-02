import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailEnvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


"""TESTAR EMAIL VÁLIDOS
========================"""


@pytest.mark.parametrize(
    'destinatario',
    ['romilsonlemes@yahoo.com.br', 'romilsonlemes@yahoo.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'romilsonlemes@gmail.com',
        'Cursos da Python Pro',
        'Primeira turma em homenagem a Jessica Ferrari.'
    )
    assert destinatario in resultado


""" TESTAR EMAIL INVÁLIDOS
========================"""


@pytest.mark.parametrize(
    'destinatario',
    ['', 'romilsonlemes']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailEnvalido):
        enviador.enviar(
            destinatario,
            'romilsonlemes@gmail.com',
            'Cursos da Python Pro',
            'Primeira turma em homenagem a Jessica Ferrari.'
        )
