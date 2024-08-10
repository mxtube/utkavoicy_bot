from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .sa import intpk, created_at, updated_at, deleted_at, Base


class User(Base):

    __tablename__ = 'user'

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    deleted_at: Mapped[deleted_at]

    repr_cols_num = 6
    repr_cols = ('created_at', )
