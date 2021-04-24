from MyValidator.constants import Constants as c
from typing import List, Dict, Tuple

SlotValidationResult = Tuple[bool, bool, str, Dict]


def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                  invalid_trigger: str = None, key: str = None, support_multiple: bool = True,
                                  pick_first: bool = False, **kwargs) -> SlotValidationResult:

    filled, partially_filled, trigger, params = False, False, invalid_trigger, {}
    count, n, ls = 0, len(values), []
    for each in values:
        if each[c.staticValue] in supported_values:
            count += 1
            ls.append(each[c.staticValue].upper())
    if n>0 and n == count:
        filled = True
        trigger = ''
        params = {key: ls[0]} if pick_first else {key: ls}
    else:
        if n:
            partially_filled = True
    return filled, partially_filled, trigger, params


def validate_numeric_constraints_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                                        support_multiple: bool = True, pick_first: bool = False, constraint=None,
                                        var_name=None, **kwargs) -> SlotValidationResult:

    filled, partially_filled, trigger, params = False, False, invalid_trigger, {}
    count, n, ls = 0, len(values), []
    for each in values:
        if constraint is None:
            count += 1
            ls.append(each[c.staticValue])
            continue
        exp = constraint.replace(var_name, str(each[c.staticValue]))
        if eval(exp):          # evaluate the expression which is passed to eval as an argument
            count += 1
            ls.append(each[c.staticValue])
    if n>0 and n == count:
        filled = True
        trigger = ''
        params = {key: ls[0]} if pick_first else {key: ls}
    else:
        if n:
            partially_filled = True
        if count > 0 and support_multiple:
            params = {key: ls[0]} if pick_first else {key: ls}
    return filled, partially_filled, trigger, params
