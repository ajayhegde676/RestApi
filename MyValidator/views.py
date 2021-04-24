from MyValidator.FiniteValueSerializer import FiniteSchema
from MyValidator.NumericValueSerializer import NumericSchema
from MyValidator.validator import validate_finite_values_entity,validate_numeric_constraints_entity
from MyValidator.constants import Constants as c
from marshmallow import INCLUDE
from rest_framework.response import Response
from rest_framework.views import APIView


class FiniteValues(APIView):
    def post(self, request):
        schema = FiniteSchema()
        entity_obj = schema.load(request.data, unknown=INCLUDE)
        res = validate_finite_values_entity(**vars(entity_obj))
        return Response(
                {c.staticFilled: res[0], c.staticPartial: res[1], c.staticTrigger: res[2], c.staticParams: res[3]})


class NumericConstraints(APIView):
    def post(self, request):
        schema = NumericSchema()
        entity_obj = schema.load(request.data, unknown=INCLUDE)
        res = validate_numeric_constraints_entity(**vars(entity_obj))
        return Response(
                {c.staticFilled: res[0], c.staticPartial: res[1], c.staticTrigger: res[2], c.staticParams: res[3]})