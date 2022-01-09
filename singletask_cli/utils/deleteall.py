from sqlalchemy import orm
from singletask_cli.context import sql_engine
from singletask_sql.tables import tracked_tables

tables = [x.__tablename__ for x in tracked_tables]
tables.append('alembic_version')

with orm.Session(sql_engine) as session:
    for table in tables:
        session.execute(f"delete from {table};")
