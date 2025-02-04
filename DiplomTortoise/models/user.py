from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=30, unique=True, null=False)
    firstname = fields.CharField(max_length=30, null=False)
    lastname = fields.CharField(max_length=30)
    age = fields.IntField(null=False)
    password = fields.CharField(min_lenght=8, max_length=128, null=False)
    createddate = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username

