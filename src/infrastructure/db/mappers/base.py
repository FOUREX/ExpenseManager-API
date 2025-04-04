from typing import Protocol, Type

from sqlalchemy import Row, RowMapping

from src.infrastructure.db.models.base import Base
from src.application.common.dto import DTO


class BaseMapper[ModelType: Base, SchemaType: DTO](Protocol):
    model: Type[ModelType]
    schema: Type[SchemaType]

    @classmethod
    def from_orm(cls, data: Type[ModelType] | ModelType | dict | Row | RowMapping) -> SchemaType:
        return cls.schema.model_validate(data, from_attributes=True)

    @classmethod
    def to_orm(cls, data: DTO) -> Type[ModelType]:
        return cls.model(**data.model_dump())

    @classmethod
    def to_orm_exclude_unset(cls, data: DTO) -> Type[ModelType]:
        return cls.model(**data.model_dump(exclude_unset=True))

    @classmethod
    def to_dict(cls, data: DTO) -> dict:
        return data.model_dump()

    @classmethod
    def to_dict_exclude_unset(cls, data: DTO) -> dict:
        return data.model_dump(exclude_unset=True)
