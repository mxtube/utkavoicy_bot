from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .sa import intpk, usage_at, Base
from .user import User


class AnalyticsVoicy(Base):

    __tablename__ = 'analytics_voicy'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    voicy_id: Mapped[int] = mapped_column(ForeignKey('voicy.id'), nullable=False)
    usage_at: Mapped[usage_at]

    repr_cols_num = 4

