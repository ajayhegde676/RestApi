from marshmallow import Schema, fields, post_load, INCLUDE
from MyValidator.Myclass import NumericValue


class NumericSchema(Schema):  # schema to validate the incoming data
    values = fields.List(fields.Dict(), required=True)
    invalid_trigger = fields.Str(required=True)
    key = fields.Str(required=True)
    support_multiple = fields.Bool()
    pick_first = fields.Bool()
    constraint = fields.Str()
    var_name = fields.Str(required=True)

    @post_load()              # decorator used for deserialization
    def deserial(self, data, **kwargs):
        return NumericValue(**data)

    class Meta:
        unknown = INCLUDE
