from jose import jwt

from todo_api.security import create_access_token
from todo_api.settings import Settings


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = jwt.decode(token, Settings().SECRET_KEY, algorithms=[Settings().ALGORITHM])

    assert decoded['test'] == data['test']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token
