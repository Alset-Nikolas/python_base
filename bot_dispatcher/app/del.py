from pony.orm import *
db = Database()
print(1)
DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='81k',
    host='localhost',
    database='vk_dispatcher_bot'
)

db.bind(**DB_CONFIG)


class UserState(db.Entity):
    """Состояние пользователя при регистрации"""
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)

db.generate_mapping(create_tables=True)

@db_session
def run():
    a = UserState(user_id="4", scenario_name="12", step_name="3", context={"2": 2})
    a2 = UserState(user_id="5", scenario_name="12", step_name="3", context={"2": 3})
    commit()
    print(a.user_id)
run()