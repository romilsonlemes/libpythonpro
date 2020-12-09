from unittest.mock import Mock
from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'romilsonlemes', 'id': 18754178,
        'avatar_url': 'https://avatars3.githubusercontent.com/u/18754178?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('romilsonlemes')
    assert 'https://avatars3.githubusercontent.com/u/18754178?v=4' == url
