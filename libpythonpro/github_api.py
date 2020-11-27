import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github
    :param usuario: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    """
    retorno = 'Link do Linkedin: \n' + resp.json()['bio'] + '\nFoto de Perfil:\n ' + resp.json()['avatar_url']
    """
    retorno = 'Foto de Perfil:\n ' + resp.json()['avatar_url']
    return retorno


if __name__ == '__main__':
    print(buscar_avatar('romilsonlemes'))
