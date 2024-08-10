from sqlalchemy.orm import Mapped, mapped_column

from .sa import intpk, deleted_at, created_at, Base


class Voicy(Base):

    __tablename__ = 'voicy'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    url: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[created_at]
    deleted_at: Mapped[deleted_at]

    repr_cols_num = 4
