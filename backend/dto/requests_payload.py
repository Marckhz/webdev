import logging
from typing import List, Optional

from fastapi_camelcase import CamelModel
from pydantic import validator

from models.entities import Skill, User

logger = logging.getLogger(__name__)


class ConvenienceORMMixin:
    def to_orm(self, exclude={}):
        raise NotImplementedError

    def _to_orm(self, model_class, exclude={}):
        self_dict = self.dict(exclude=exclude)
        for key in self.__fields__.keys():
            try:
                attr = getattr(self, key)
                if type(attr) == list:
                    self_dict[key] = [i.to_orm() for i in attr]
                else:
                    self_dict[key] = attr.to_orm()
            except AttributeError as e:
                logger.info(e)
        return model_class(**self_dict)


class SkillsDTO(CamelModel, ConvenienceORMMixin):
    id: Optional[int]
    skill: str

    class Config:
        orm_mode = True
        anystr_lower = True

    def to_orm(self, exclude={}):
        return self._to_orm(Skill, exclude=exclude)

    @validator('skill')
    def contain_at_least_letter(cls, v):
        if not v:
            raise ValueError('must contain at least a letter')
        return v


class UserDTO(CamelModel, ConvenienceORMMixin):
    id: Optional[int]
    name: str
    subscriptions: Optional[List[SkillsDTO]] = []

    def to_orm(self, exclude={}):
        return self._to_orm(User, exclude=exclude)

    @validator('name')
    def validate_name(cls, v):
        if not v:
            raise ValueError('must contain at least a letter')
        return v

    class Config:
        orm_mode = True


class UserSkillDTO(CamelModel):
    user: UserDTO
    skill: SkillsDTO
