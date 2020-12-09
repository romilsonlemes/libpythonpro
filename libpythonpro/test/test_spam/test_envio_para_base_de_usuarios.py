import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario

"""Inclusáo de parametrize para realizar os testes """


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
        enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'romilsonlemes@gmail.com',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='romilson', email='romilsonlemes@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'renzo@python.pro.br',
        'romilsonlemes@gmail.com',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
