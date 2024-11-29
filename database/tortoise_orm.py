from random import choice

from tortoise.models import Model
from tortoise import fields
from enum import IntEnum


class Device(IntEnum):
    BULBS = 1
    """
    Добавить остальное
    """


class User(Model):
    id = fields.IntField(
        pk=True
    )
    name = fields.CharField(
        max_length=100
    )
    tg_uuid = fields.UUIDField(
        unique=True
    )


class HousePreset(Model):
    id = fields.IntField(
        pk=True
    )
    name = fields.CharField(
        max_length=100
    )
    user = fields.ForeignKeyField(
        'models.User', related_name='house_presets', on_delete=fields.CASCADE
    )


class DevisePreset(Model):
    id = fields.IntField(
        pk=True
    )
    devise_name = fields.IntEnumField(
        Device
    )
    some_settings = fields.CharField(
        max_length=100
    )
    user = fields.ForeignKeyField(
        'models.User', related_name='devise_presets', on_delete=fields.CASCADE
    )
