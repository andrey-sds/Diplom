import asyncio
from backend.db import inint_db, close_db
from routers.user import create_user, update_user, get_user, delete_user


async def main():
    await inint_db()

    try:
        user_ids = []

        # Создание 100 пользователей
        for i in range(1, 101):
            user_result = await create_user(
                username=f'User{i}',
                firstname=f'Urban{i}',
                lastname=f'Test{i}',
                age=20 + i % 10,  # Возраст будет от 20 до 29
                password='12345678'
            )

            if isinstance(user_result, int):
                user_ids.append(user_result)
            else:
                print(f"Ошибка при создании пользователя {i}: {user_result}")

        # Вывод всех пользователей
        print("Все пользователи:")
        for user_id in user_ids:
            fetch_user = await get_user(user_id)
            print(f"ID: {fetch_user.id}, Имя: {fetch_user.firstname}, Фамилия: {fetch_user.lastname}, Возраст: {fetch_user.age}")

        # Обновление данных пользователей с 11 по 20
        print("\nОбновление данных пользователей с 11 по 20:")
        for user_id in user_ids[10:20]:
            upd_user = await update_user(user_id, age=33, lastname=f"Profi{user_id}")
            print(f"Обновлено: ID {upd_user.id}, Имя: {upd_user.firstname}, Фамилия: {upd_user.lastname}, Возраст: {upd_user.age}")

        # Удаление всех пользователей
        print("\nУдаление всех пользователей:")
        for user_id in user_ids:
            is_deleted = await delete_user(user_id)
            print(f'Удален пользователь с ID {user_id}: {is_deleted}')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        await close_db()

if __name__ == '__main__':
    asyncio.run(main())
