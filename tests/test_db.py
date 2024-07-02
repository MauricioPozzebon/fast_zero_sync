from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='Mauri', email='mauri@mauri.com.br', password='senha')
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'mauri@mauri.com.br')
    )
    assert result.username == 'Mauri'
