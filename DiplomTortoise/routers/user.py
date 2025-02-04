from models.user import User
from tortoise.exceptions import DoesNotExist,IntegrityError


async def create_user(username: str, firstname: str, lastname: str, age: int, password: str):
    # Проверяем, существует ли пользователь с таким username
    existing_user = await User.filter(username=username).exists()
    if existing_user:
        return f'Пользователь с именем {username} уже существует!'

    try:
        user = await User.create(
            username=username,
            firstname=firstname,
            lastname=lastname,
            age=age,
            password=password
        )
        return user.id
    except IntegrityError:
        return f'Ошибка при создании пользователя с именем {username}.'


async def get_user(user_id: int):
    try:
        user = await User.get(id=user_id)
        return user
    except DoesNotExist:
        return f'Пользователь {user_id} не найден!'


async def update_user(user_id: int, **kwargs):
    user = await User.get(id=user_id)
    if user:
        await user.update_from_dict(kwargs).save()
        return user
    return f'Пользователь {user_id} не найден!'


async def delete_user(user_id: int):
    user = await User.get(id=user_id)
    if user:
        await user.delete()
        return f'Пользователь {user_id} был удален!'
    return f'Пользователь {user_id} не найден!'


