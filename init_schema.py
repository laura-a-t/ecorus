from api.utils import get_config
from api.db.db import EngineSingleton
from api.db.models import Base


if __name__ == '__main__':
    db_config = get_config('DB')
    engine = EngineSingleton(db_config).get_engine()
    Base.metadata.create_all(engine, checkfirst=True)
