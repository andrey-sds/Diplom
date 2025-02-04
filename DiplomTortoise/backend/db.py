from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {"default": "sqlite://orm_tort.sqlite3"},
    "apps": {
        "models": {
            "models": ["models.user", "aerich.models"],
            "default_connection": "default",
        }
    },
}


async def inint_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
