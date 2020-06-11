from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.utils import get_config


class EngineSingleton:
    instance = None

    def __init__(self, db_config):
        if not EngineSingleton.instance:
            EngineSingleton.instance = _get_engine(db_config)

    def get_engine(self):
        return EngineSingleton.instance


def _get_engine(db_config):
    return create_engine(db_config['connection_string'])


def get_session(db_config=None):
    if not db_config:
        db_config = get_config('DB')

    return sessionmaker(
        bind=EngineSingleton(db_config).get_engine()
    )()


@contextmanager
def session(db_config=None, commit=True):
    """Provide a transactional scope around a series of operations."""
    session = get_session(db_config)
    try:
        yield session
        if commit:
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
