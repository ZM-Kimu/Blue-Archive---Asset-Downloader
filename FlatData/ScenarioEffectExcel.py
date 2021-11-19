# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ScenarioEffectExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ScenarioEffectExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsScenarioEffectExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ScenarioEffectExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ScenarioEffectExcel
    def EffectName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ScenarioEffectExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(2)
def ScenarioEffectExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEffectName(builder, EffectName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(EffectName), 0)
def ScenarioEffectExcelAddEffectName(builder, EffectName):
    """This method is deprecated. Please switch to AddEffectName."""
    return AddEffectName(builder, EffectName)
def AddName(builder, Name): builder.PrependUint32Slot(1, Name, 0)
def ScenarioEffectExcelAddName(builder, Name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, Name)
def End(builder): return builder.EndObject()
def ScenarioEffectExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)