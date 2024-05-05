# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterWeaponLevelExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterWeaponLevelExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterWeaponLevelExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterWeaponLevelExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterWeaponLevelExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.CharacterWeaponLevelExcel import CharacterWeaponLevelExcel
            obj = CharacterWeaponLevelExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CharacterWeaponLevelExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterWeaponLevelExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def Start(builder): builder.StartObject(1)
def CharacterWeaponLevelExcelTableStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def CharacterWeaponLevelExcelTableAddDataList(builder, DataList):
    """This method is deprecated. Please switch to AddDataList."""
    return AddDataList(builder, DataList)
def StartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterWeaponLevelExcelTableStartDataListVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartDataListVector(builder, numElems)
def End(builder): return builder.EndObject()
def CharacterWeaponLevelExcelTableEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)