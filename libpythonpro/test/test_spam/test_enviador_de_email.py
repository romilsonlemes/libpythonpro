from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'romilsonlemes@gmail.com',
        'romilsonlemes@yahoo.com.br',
        'Cursos da Python Pro',
        'Primeira turma em homenagem a Jessica Ferrari.'
    )
    assert 'romilsonlemes@gmail.com' in resultado
