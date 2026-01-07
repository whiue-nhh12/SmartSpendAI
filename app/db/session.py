from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from core.config import settings

engine = create_async_engine(
    url = settings.DATA_URL,
    echo = True,
    future = True,
    pool_size = 10,
    max_overflow = 20
)

AsyncSessionLocal = async_sessionmaker(
    bind = engine,
    class_= AsyncSession,
    expire_on_commit = True,
    autocommit = False,
    autoflush= False
)

