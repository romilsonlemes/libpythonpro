import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from unittest.mock import Mock

"""Inclusão de parametrize para realizar os testes """


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='romilson', email='romilsonlemes@gmail.com'),
            Usuario(nome='luciano', email='luciano@python.pro.br')
        ],
        [
            Usuario(nome='renzo', email='renzo@python.pro.br'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
        enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'romilsonlemes@gmail.com',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='romilson', email='romilsonlemes@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'renzo@python.pro.br',
        'romilsonlemes@gmail.com',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
