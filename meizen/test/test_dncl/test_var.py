from meizen.dncl.var import Variable
from meizen.dncl.var import VariableTable
from meizen.dncl.type import NameType


def test_variable():
    v = Variable(NameType.CONST, "NAME", "0")
    assert v.address == "0"
    assert v.name == "NAME"
    assert v.name_type == NameType.CONST
    v.address = "1"
    assert v.address == "1"


def test_vartable():
    const_table = VariableTable(NameType.CONST)
    var_table = VariableTable(NameType.VARIABLE)
    array_table = VariableTable(NameType.ARRAY)
