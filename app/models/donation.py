from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import BaseModel


class Donation(BaseModel):
    __tablename__ = 'donation'

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String(256))

    def __repr__(self):
        base_repr = super().__repr__()
        return (f'{base_repr[:-1]}, user_id={self.user_id},'
                f' comment={self.comment!r})>')
