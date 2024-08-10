from sqlalchemy.orm import mapped_column, DeclarativeBase
from sqlalchemy import text

import datetime
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
usage_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.utcnow)]
deleted_at = Annotated[datetime.datetime, mapped_column(nullable=True)]


class Base(DeclarativeBase):

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f'{col}={getattr(self, col)}')

        return f"{self.__class__.__name__} {','.join(cols)}"
