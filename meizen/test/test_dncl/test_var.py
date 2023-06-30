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


def test_var_table():
    var_table = VariableTable()
    assert not var_table.is_exit_key("hoge")
    var_table.append("hoge", "000")
    assert var_table.is_exit_key("hoge")
