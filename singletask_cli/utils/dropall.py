from sqlalchemy import orm
from singletask_cli.context import sql_engine
from singletask_sql.tables import tracked_tables

tables = [x.__tablename__ for x in tracked_tables]
tables.append('alembic_version')

with orm.Session(sql_engine) as session:
    for table in tables:
        try:
            session.execute(f'drop table public.{table} CASCADE;')
        except Exception as ex:
            print(ex)
        session.commit()

    try:
        session.execute('DROP FUNCTION procedure_update CASCADE;')
    except Exception as ex:
        print(ex)
    session.commit()
