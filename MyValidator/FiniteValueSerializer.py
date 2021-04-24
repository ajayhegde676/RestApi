from marshmallow import Schema, fields, post_load, INCLUDE
from MyValidator.Myclass import FiniteValue


class FiniteSchema(Schema):  # schema to validate the incoming data
    values = fields.List(fields.Dict(), required=True)
    invalid_trigger = fields.Str(required=True)
    key = fields.Str(required=True)
    support_multiple = fields.Bool()
    pick_first = fields.Bool()
    supported_values = fields.List(fields.Str(), required=True)

    @post_load()             # decorator used for deserialization
    def deserial(self, data, **kwargs):
        return FiniteValue(**data)

    class Meta:
        unknown = INCLUDE  # including undefined fields in schema
