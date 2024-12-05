from sqlalchemy import create_engine
import config
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Article,User,Navigation
    Base.metadata.create_all(bind=engine)
    pass