import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize (
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
        enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'romilsonlemes@gmail.com',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


