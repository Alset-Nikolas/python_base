from pony.orm import Database, Required, Json
from .settings_dispatcher import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class UserState(db.Entity):
    """Состояние пользователя при регистрации"""
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)


class Registration(db.Entity):
    """Заявка на регистрауию"""
    user_id = Required(str, unique=True)
    departure_city = Required(str)
    arrival_city = Required(str)
    date = Required(str)
    flight = Required(str)
    comment = Required(str)
    telephone = Required(str)


db.generate_mapping(create_tables=True)
