# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticArenaSimulatorSettingExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticArenaSimulatorSettingExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTacticArenaSimulatorSettingExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TacticArenaSimulatorSettingExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TacticArenaSimulatorSettingExcel
    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def Repeat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerUserArenaGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerUserArenaRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerPresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerStrikerNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerSpecialNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderUserArenaGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderUserArenaRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderPresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderStrikerNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderSpecialNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(15)
def TacticArenaSimulatorSettingExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddOrder(builder, Order): builder.PrependInt64Slot(0, Order, 0)
def TacticArenaSimulatorSettingExcelAddOrder(builder, Order):
    """This method is deprecated. Please switch to AddOrder."""
    return AddOrder(builder, Order)
def AddRepeat(builder, Repeat): builder.PrependInt64Slot(1, Repeat, 0)
def TacticArenaSimulatorSettingExcelAddRepeat(builder, Repeat):
    """This method is deprecated. Please switch to AddRepeat."""
    return AddRepeat(builder, Repeat)
def AddAttackerFrom(builder, AttackerFrom): builder.PrependInt32Slot(2, AttackerFrom, 0)
def TacticArenaSimulatorSettingExcelAddAttackerFrom(builder, AttackerFrom):
    """This method is deprecated. Please switch to AddAttackerFrom."""
    return AddAttackerFrom(builder, AttackerFrom)
def AddAttackerUserArenaGroup(builder, AttackerUserArenaGroup): builder.PrependInt64Slot(3, AttackerUserArenaGroup, 0)
def TacticArenaSimulatorSettingExcelAddAttackerUserArenaGroup(builder, AttackerUserArenaGroup):
    """This method is deprecated. Please switch to AddAttackerUserArenaGroup."""
    return AddAttackerUserArenaGroup(builder, AttackerUserArenaGroup)
def AddAttackerUserArenaRank(builder, AttackerUserArenaRank): builder.PrependInt64Slot(4, AttackerUserArenaRank, 0)
def TacticArenaSimulatorSettingExcelAddAttackerUserArenaRank(builder, AttackerUserArenaRank):
    """This method is deprecated. Please switch to AddAttackerUserArenaRank."""
    return AddAttackerUserArenaRank(builder, AttackerUserArenaRank)
def AddAttackerPresetGroupId(builder, AttackerPresetGroupId): builder.PrependInt64Slot(5, AttackerPresetGroupId, 0)
def TacticArenaSimulatorSettingExcelAddAttackerPresetGroupId(builder, AttackerPresetGroupId):
    """This method is deprecated. Please switch to AddAttackerPresetGroupId."""
    return AddAttackerPresetGroupId(builder, AttackerPresetGroupId)
def AddAttackerStrikerNum(builder, AttackerStrikerNum): builder.PrependInt64Slot(6, AttackerStrikerNum, 0)
def TacticArenaSimulatorSettingExcelAddAttackerStrikerNum(builder, AttackerStrikerNum):
    """This method is deprecated. Please switch to AddAttackerStrikerNum."""
    return AddAttackerStrikerNum(builder, AttackerStrikerNum)
def AddAttackerSpecialNum(builder, AttackerSpecialNum): builder.PrependInt64Slot(7, AttackerSpecialNum, 0)
def TacticArenaSimulatorSettingExcelAddAttackerSpecialNum(builder, AttackerSpecialNum):
    """This method is deprecated. Please switch to AddAttackerSpecialNum."""
    return AddAttackerSpecialNum(builder, AttackerSpecialNum)
def AddDefenderFrom(builder, DefenderFrom): builder.PrependInt32Slot(8, DefenderFrom, 0)
def TacticArenaSimulatorSettingExcelAddDefenderFrom(builder, DefenderFrom):
    """This method is deprecated. Please switch to AddDefenderFrom."""
    return AddDefenderFrom(builder, DefenderFrom)
def AddDefenderUserArenaGroup(builder, DefenderUserArenaGroup): builder.PrependInt64Slot(9, DefenderUserArenaGroup, 0)
def TacticArenaSimulatorSettingExcelAddDefenderUserArenaGroup(builder, DefenderUserArenaGroup):
    """This method is deprecated. Please switch to AddDefenderUserArenaGroup."""
    return AddDefenderUserArenaGroup(builder, DefenderUserArenaGroup)
def AddDefenderUserArenaRank(builder, DefenderUserArenaRank): builder.PrependInt64Slot(10, DefenderUserArenaRank, 0)
def TacticArenaSimulatorSettingExcelAddDefenderUserArenaRank(builder, DefenderUserArenaRank):
    """This method is deprecated. Please switch to AddDefenderUserArenaRank."""
    return AddDefenderUserArenaRank(builder, DefenderUserArenaRank)
def AddDefenderPresetGroupId(builder, DefenderPresetGroupId): builder.PrependInt64Slot(11, DefenderPresetGroupId, 0)
def TacticArenaSimulatorSettingExcelAddDefenderPresetGroupId(builder, DefenderPresetGroupId):
    """This method is deprecated. Please switch to AddDefenderPresetGroupId."""
    return AddDefenderPresetGroupId(builder, DefenderPresetGroupId)
def AddDefenderStrikerNum(builder, DefenderStrikerNum): builder.PrependInt64Slot(12, DefenderStrikerNum, 0)
def TacticArenaSimulatorSettingExcelAddDefenderStrikerNum(builder, DefenderStrikerNum):
    """This method is deprecated. Please switch to AddDefenderStrikerNum."""
    return AddDefenderStrikerNum(builder, DefenderStrikerNum)
def AddDefenderSpecialNum(builder, DefenderSpecialNum): builder.PrependInt64Slot(13, DefenderSpecialNum, 0)
def TacticArenaSimulatorSettingExcelAddDefenderSpecialNum(builder, DefenderSpecialNum):
    """This method is deprecated. Please switch to AddDefenderSpecialNum."""
    return AddDefenderSpecialNum(builder, DefenderSpecialNum)
def AddGroundId(builder, GroundId): builder.PrependInt64Slot(14, GroundId, 0)
def TacticArenaSimulatorSettingExcelAddGroundId(builder, GroundId):
    """This method is deprecated. Please switch to AddGroundId."""
    return AddGroundId(builder, GroundId)
def End(builder): return builder.EndObject()
def TacticArenaSimulatorSettingExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)