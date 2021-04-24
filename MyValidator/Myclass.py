class Base:
    def __init__(self, values, invalid_trigger, key, support_multiple, pick_first):
        self.values = values
        self.invalid_trigger = invalid_trigger
        self.key = key
        self.support_multiple = support_multiple
        self.pick_first = pick_first


class FiniteValue(Base):
    def __init__(self, values, supported_values, invalid_trigger, key, support_multiple, pick_first, **kwargs):
        super().__init__(values, invalid_trigger, key, support_multiple, pick_first)
        self.supported_values = supported_values


class NumericValue(Base):
    def __init__(self, values, invalid_trigger, key, support_multiple, pick_first, constraint, var_name, **kwargs):
        super().__init__(values, invalid_trigger, key, support_multiple, pick_first)
        self.constraint = constraint
        self.var_name = var_name
