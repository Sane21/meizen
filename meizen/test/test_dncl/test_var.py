from meizen.dncl.var import Variable, VariableTable, ConstTable
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
    assert var_table.get("hoge").name_type == NameType.VARIABLE
    var_table.append("fuga", "001")
    var_table.append("piyo", "002")
    assert var_table.get("fuga").address == "001"
    assert not var_table.get("fuga").address == var_table.get("piyo").address


def test_const_table():
    table = ConstTable()
    table.append("HOGE", "000")
    assert table.get("HOGE").name_type == NameType.CONST
