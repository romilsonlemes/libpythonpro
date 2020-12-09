from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Romilson', email='romilsonlemes@gmail.com')
    print("Executa a Sessão !!")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Romilson', email='romilsonlemes@gmail.com'),
                Usuario(nome='Renzo', email='romilsonlemes@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
