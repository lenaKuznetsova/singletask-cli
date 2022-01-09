from singletask_sql.settings import BASE_DIR, dotenv_values
from singletask_sql.engine import create_engine


# todo - config after auth
env_path = [
    f'{BASE_DIR}/../.env',
    f'{BASE_DIR}/../.env.local'
]
conf = {}
for path in env_path:
    conf.update(dotenv_values(path))

sql_engine = create_engine(conf)
