from tortoise import Tortoise


async def init_tortoise():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['database.tortoise_orm']}
    )
    await Tortoise.generate_schemas()


