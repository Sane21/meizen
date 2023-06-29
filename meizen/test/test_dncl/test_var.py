from meizen.dncl.var import Variable
from meizen.dncl.type import NameType


def test_variable():
    v = Variable(NameType.CONST, "NAME", "0")
    assert v.address == "0"
    assert v.name == "NAME"
    assert v.name_type == NameType.CONST
    v.address = "1"
    assert v.name_type == NameType.VARIABLE
