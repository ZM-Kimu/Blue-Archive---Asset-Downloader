# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EquipmentStatExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EquipmentStatExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEquipmentStatExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EquipmentStatExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EquipmentStatExcel
    def EquipmentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def StatLevelUpType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def StatType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EquipmentStatExcel
    def StatTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EquipmentStatExcel
    def StatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentStatExcel
    def StatTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # EquipmentStatExcel
    def MinStat(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EquipmentStatExcel
    def MinStatAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EquipmentStatExcel
    def MinStatLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentStatExcel
    def MinStatIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # EquipmentStatExcel
    def MaxStat(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EquipmentStatExcel
    def MaxStatAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EquipmentStatExcel
    def MaxStatLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentStatExcel
    def MaxStatIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # EquipmentStatExcel
    def LevelUpInsertLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def LevelUpFeedExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def LevelUpFeedCostCurrency(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def LevelUpFeedCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def EquipmentCategory_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def LevelUpFeedAddExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def DefaultMaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def TranscendenceMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentStatExcel
    def DamageFactorGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(14)
def EquipmentStatExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEquipmentId(builder, EquipmentId): builder.PrependInt64Slot(0, EquipmentId, 0)
def EquipmentStatExcelAddEquipmentId(builder, EquipmentId):
    """This method is deprecated. Please switch to AddEquipmentId."""
    return AddEquipmentId(builder, EquipmentId)
def AddStatLevelUpType_(builder, StatLevelUpType_): builder.PrependInt32Slot(1, StatLevelUpType_, 0)
def EquipmentStatExcelAddStatLevelUpType_(builder, StatLevelUpType_):
    """This method is deprecated. Please switch to AddStatLevelUpType_."""
    return AddStatLevelUpType_(builder, StatLevelUpType_)
def AddStatType(builder, StatType): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(StatType), 0)
def EquipmentStatExcelAddStatType(builder, StatType):
    """This method is deprecated. Please switch to AddStatType."""
    return AddStatType(builder, StatType)
def StartStatTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EquipmentStatExcelStartStatTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStatTypeVector(builder, numElems)
def AddMinStat(builder, MinStat): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(MinStat), 0)
def EquipmentStatExcelAddMinStat(builder, MinStat):
    """This method is deprecated. Please switch to AddMinStat."""
    return AddMinStat(builder, MinStat)
def StartMinStatVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EquipmentStatExcelStartMinStatVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMinStatVector(builder, numElems)
def AddMaxStat(builder, MaxStat): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(MaxStat), 0)
def EquipmentStatExcelAddMaxStat(builder, MaxStat):
    """This method is deprecated. Please switch to AddMaxStat."""
    return AddMaxStat(builder, MaxStat)
def StartMaxStatVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EquipmentStatExcelStartMaxStatVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMaxStatVector(builder, numElems)
def AddLevelUpInsertLimit(builder, LevelUpInsertLimit): builder.PrependInt32Slot(5, LevelUpInsertLimit, 0)
def EquipmentStatExcelAddLevelUpInsertLimit(builder, LevelUpInsertLimit):
    """This method is deprecated. Please switch to AddLevelUpInsertLimit."""
    return AddLevelUpInsertLimit(builder, LevelUpInsertLimit)
def AddLevelUpFeedExp(builder, LevelUpFeedExp): builder.PrependInt64Slot(6, LevelUpFeedExp, 0)
def EquipmentStatExcelAddLevelUpFeedExp(builder, LevelUpFeedExp):
    """This method is deprecated. Please switch to AddLevelUpFeedExp."""
    return AddLevelUpFeedExp(builder, LevelUpFeedExp)
def AddLevelUpFeedCostCurrency(builder, LevelUpFeedCostCurrency): builder.PrependInt32Slot(7, LevelUpFeedCostCurrency, 0)
def EquipmentStatExcelAddLevelUpFeedCostCurrency(builder, LevelUpFeedCostCurrency):
    """This method is deprecated. Please switch to AddLevelUpFeedCostCurrency."""
    return AddLevelUpFeedCostCurrency(builder, LevelUpFeedCostCurrency)
def AddLevelUpFeedCostAmount(builder, LevelUpFeedCostAmount): builder.PrependInt64Slot(8, LevelUpFeedCostAmount, 0)
def EquipmentStatExcelAddLevelUpFeedCostAmount(builder, LevelUpFeedCostAmount):
    """This method is deprecated. Please switch to AddLevelUpFeedCostAmount."""
    return AddLevelUpFeedCostAmount(builder, LevelUpFeedCostAmount)
def AddEquipmentCategory_(builder, EquipmentCategory_): builder.PrependInt32Slot(9, EquipmentCategory_, 0)
def EquipmentStatExcelAddEquipmentCategory_(builder, EquipmentCategory_):
    """This method is deprecated. Please switch to AddEquipmentCategory_."""
    return AddEquipmentCategory_(builder, EquipmentCategory_)
def AddLevelUpFeedAddExp(builder, LevelUpFeedAddExp): builder.PrependInt64Slot(10, LevelUpFeedAddExp, 0)
def EquipmentStatExcelAddLevelUpFeedAddExp(builder, LevelUpFeedAddExp):
    """This method is deprecated. Please switch to AddLevelUpFeedAddExp."""
    return AddLevelUpFeedAddExp(builder, LevelUpFeedAddExp)
def AddDefaultMaxLevel(builder, DefaultMaxLevel): builder.PrependInt32Slot(11, DefaultMaxLevel, 0)
def EquipmentStatExcelAddDefaultMaxLevel(builder, DefaultMaxLevel):
    """This method is deprecated. Please switch to AddDefaultMaxLevel."""
    return AddDefaultMaxLevel(builder, DefaultMaxLevel)
def AddTranscendenceMax(builder, TranscendenceMax): builder.PrependInt32Slot(12, TranscendenceMax, 0)
def EquipmentStatExcelAddTranscendenceMax(builder, TranscendenceMax):
    """This method is deprecated. Please switch to AddTranscendenceMax."""
    return AddTranscendenceMax(builder, TranscendenceMax)
def AddDamageFactorGroupId(builder, DamageFactorGroupId): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(DamageFactorGroupId), 0)
def EquipmentStatExcelAddDamageFactorGroupId(builder, DamageFactorGroupId):
    """This method is deprecated. Please switch to AddDamageFactorGroupId."""
    return AddDamageFactorGroupId(builder, DamageFactorGroupId)
def End(builder): return builder.EndObject()
def EquipmentStatExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)