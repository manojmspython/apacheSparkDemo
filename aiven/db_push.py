""" This module dumps data into postgres"""

from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from create_table import customers


@contextmanager
def session_scope(engine_handler):
    """Provide a transactional scope around a series of operations."""
    session = sessionmaker(bind=engine_handler)()
    try:
        yield session
        session.commit()
    except:
        import traceback

        print(traceback.format_exc())
        session.rollback()
        raise
    finally:
        session.close()


def dump_data(data, engine):
    """
    Dump the data into postgres
    :param data: Json data that needs to be pushed into DB
    :param engine: connection engine
    :return: None
    """
    with session_scope(engine_handler=engine) as session:
        c1 = customers.insert().values(**data)
        session.execute(c1)
        session.commit()
