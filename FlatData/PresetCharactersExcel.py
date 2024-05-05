# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PresetCharactersExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PresetCharactersExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPresetCharactersExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # PresetCharactersExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PresetCharactersExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def PresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def ArenaSimulatorFixed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharactersExcel
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def Exp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def FavorExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def FavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def StarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def ExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def PassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def ExtraPassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def CommonSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def LeaderSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def EquipSlot01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharactersExcel
    def EquipSlotTier01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def EquipSlotLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def EquipSlot02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharactersExcel
    def EquipSlotTier02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def EquipSlotLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def EquipSlot03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharactersExcel
    def EquipSlotTier03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharactersExcel
    def EquipSlotLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(22)
def PresetCharactersExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(0, CharacterId, 0)
def PresetCharactersExcelAddCharacterId(builder, CharacterId):
    """This method is deprecated. Please switch to AddCharacterId."""
    return AddCharacterId(builder, CharacterId)
def AddPresetGroupId(builder, PresetGroupId): builder.PrependInt64Slot(1, PresetGroupId, 0)
def PresetCharactersExcelAddPresetGroupId(builder, PresetGroupId):
    """This method is deprecated. Please switch to AddPresetGroupId."""
    return AddPresetGroupId(builder, PresetGroupId)
def AddArenaSimulatorFixed(builder, ArenaSimulatorFixed): builder.PrependBoolSlot(2, ArenaSimulatorFixed, 0)
def PresetCharactersExcelAddArenaSimulatorFixed(builder, ArenaSimulatorFixed):
    """This method is deprecated. Please switch to AddArenaSimulatorFixed."""
    return AddArenaSimulatorFixed(builder, ArenaSimulatorFixed)
def AddLevel(builder, Level): builder.PrependInt32Slot(3, Level, 0)
def PresetCharactersExcelAddLevel(builder, Level):
    """This method is deprecated. Please switch to AddLevel."""
    return AddLevel(builder, Level)
def AddExp(builder, Exp): builder.PrependInt32Slot(4, Exp, 0)
def PresetCharactersExcelAddExp(builder, Exp):
    """This method is deprecated. Please switch to AddExp."""
    return AddExp(builder, Exp)
def AddFavorExp(builder, FavorExp): builder.PrependInt32Slot(5, FavorExp, 0)
def PresetCharactersExcelAddFavorExp(builder, FavorExp):
    """This method is deprecated. Please switch to AddFavorExp."""
    return AddFavorExp(builder, FavorExp)
def AddFavorRank(builder, FavorRank): builder.PrependInt32Slot(6, FavorRank, 0)
def PresetCharactersExcelAddFavorRank(builder, FavorRank):
    """This method is deprecated. Please switch to AddFavorRank."""
    return AddFavorRank(builder, FavorRank)
def AddStarGrade(builder, StarGrade): builder.PrependInt32Slot(7, StarGrade, 0)
def PresetCharactersExcelAddStarGrade(builder, StarGrade):
    """This method is deprecated. Please switch to AddStarGrade."""
    return AddStarGrade(builder, StarGrade)
def AddExSkillLevel(builder, ExSkillLevel): builder.PrependInt32Slot(8, ExSkillLevel, 0)
def PresetCharactersExcelAddExSkillLevel(builder, ExSkillLevel):
    """This method is deprecated. Please switch to AddExSkillLevel."""
    return AddExSkillLevel(builder, ExSkillLevel)
def AddPassiveSkillLevel(builder, PassiveSkillLevel): builder.PrependInt32Slot(9, PassiveSkillLevel, 0)
def PresetCharactersExcelAddPassiveSkillLevel(builder, PassiveSkillLevel):
    """This method is deprecated. Please switch to AddPassiveSkillLevel."""
    return AddPassiveSkillLevel(builder, PassiveSkillLevel)
def AddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel): builder.PrependInt32Slot(10, ExtraPassiveSkillLevel, 0)
def PresetCharactersExcelAddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel):
    """This method is deprecated. Please switch to AddExtraPassiveSkillLevel."""
    return AddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel)
def AddCommonSkillLevel(builder, CommonSkillLevel): builder.PrependInt32Slot(11, CommonSkillLevel, 0)
def PresetCharactersExcelAddCommonSkillLevel(builder, CommonSkillLevel):
    """This method is deprecated. Please switch to AddCommonSkillLevel."""
    return AddCommonSkillLevel(builder, CommonSkillLevel)
def AddLeaderSkillLevel(builder, LeaderSkillLevel): builder.PrependInt32Slot(12, LeaderSkillLevel, 0)
def PresetCharactersExcelAddLeaderSkillLevel(builder, LeaderSkillLevel):
    """This method is deprecated. Please switch to AddLeaderSkillLevel."""
    return AddLeaderSkillLevel(builder, LeaderSkillLevel)
def AddEquipSlot01(builder, EquipSlot01): builder.PrependBoolSlot(13, EquipSlot01, 0)
def PresetCharactersExcelAddEquipSlot01(builder, EquipSlot01):
    """This method is deprecated. Please switch to AddEquipSlot01."""
    return AddEquipSlot01(builder, EquipSlot01)
def AddEquipSlotTier01(builder, EquipSlotTier01): builder.PrependInt32Slot(14, EquipSlotTier01, 0)
def PresetCharactersExcelAddEquipSlotTier01(builder, EquipSlotTier01):
    """This method is deprecated. Please switch to AddEquipSlotTier01."""
    return AddEquipSlotTier01(builder, EquipSlotTier01)
def AddEquipSlotLevel01(builder, EquipSlotLevel01): builder.PrependInt32Slot(15, EquipSlotLevel01, 0)
def PresetCharactersExcelAddEquipSlotLevel01(builder, EquipSlotLevel01):
    """This method is deprecated. Please switch to AddEquipSlotLevel01."""
    return AddEquipSlotLevel01(builder, EquipSlotLevel01)
def AddEquipSlot02(builder, EquipSlot02): builder.PrependBoolSlot(16, EquipSlot02, 0)
def PresetCharactersExcelAddEquipSlot02(builder, EquipSlot02):
    """This method is deprecated. Please switch to AddEquipSlot02."""
    return AddEquipSlot02(builder, EquipSlot02)
def AddEquipSlotTier02(builder, EquipSlotTier02): builder.PrependInt32Slot(17, EquipSlotTier02, 0)
def PresetCharactersExcelAddEquipSlotTier02(builder, EquipSlotTier02):
    """This method is deprecated. Please switch to AddEquipSlotTier02."""
    return AddEquipSlotTier02(builder, EquipSlotTier02)
def AddEquipSlotLevel02(builder, EquipSlotLevel02): builder.PrependInt32Slot(18, EquipSlotLevel02, 0)
def PresetCharactersExcelAddEquipSlotLevel02(builder, EquipSlotLevel02):
    """This method is deprecated. Please switch to AddEquipSlotLevel02."""
    return AddEquipSlotLevel02(builder, EquipSlotLevel02)
def AddEquipSlot03(builder, EquipSlot03): builder.PrependBoolSlot(19, EquipSlot03, 0)
def PresetCharactersExcelAddEquipSlot03(builder, EquipSlot03):
    """This method is deprecated. Please switch to AddEquipSlot03."""
    return AddEquipSlot03(builder, EquipSlot03)
def AddEquipSlotTier03(builder, EquipSlotTier03): builder.PrependInt32Slot(20, EquipSlotTier03, 0)
def PresetCharactersExcelAddEquipSlotTier03(builder, EquipSlotTier03):
    """This method is deprecated. Please switch to AddEquipSlotTier03."""
    return AddEquipSlotTier03(builder, EquipSlotTier03)
def AddEquipSlotLevel03(builder, EquipSlotLevel03): builder.PrependInt32Slot(21, EquipSlotLevel03, 0)
def PresetCharactersExcelAddEquipSlotLevel03(builder, EquipSlotLevel03):
    """This method is deprecated. Please switch to AddEquipSlotLevel03."""
    return AddEquipSlotLevel03(builder, EquipSlotLevel03)
def End(builder): return builder.EndObject()
def PresetCharactersExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)