# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ArenaSeasonCloseRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArenaSeasonCloseRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsArenaSeasonCloseRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ArenaSeasonCloseRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArenaSeasonCloseRewardExcel
    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RankStart(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RankEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelUniqueId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelUniqueIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelUniqueIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelUniqueIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelUniqueName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # ArenaSeasonCloseRewardExcel
    def RewardParcelUniqueNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelUniqueNameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaSeasonCloseRewardExcel
    def RewardParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

def Start(builder): builder.StartObject(7)
def ArenaSeasonCloseRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddSeasonId(builder, SeasonId): builder.PrependInt64Slot(0, SeasonId, 0)
def ArenaSeasonCloseRewardExcelAddSeasonId(builder, SeasonId):
    """This method is deprecated. Please switch to AddSeasonId."""
    return AddSeasonId(builder, SeasonId)
def AddRankStart(builder, RankStart): builder.PrependInt64Slot(1, RankStart, 0)
def ArenaSeasonCloseRewardExcelAddRankStart(builder, RankStart):
    """This method is deprecated. Please switch to AddRankStart."""
    return AddRankStart(builder, RankStart)
def AddRankEnd(builder, RankEnd): builder.PrependInt64Slot(2, RankEnd, 0)
def ArenaSeasonCloseRewardExcelAddRankEnd(builder, RankEnd):
    """This method is deprecated. Please switch to AddRankEnd."""
    return AddRankEnd(builder, RankEnd)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def ArenaSeasonCloseRewardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def StartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArenaSeasonCloseRewardExcelStartRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelTypeVector(builder, numElems)
def AddRewardParcelUniqueId(builder, RewardParcelUniqueId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelUniqueId), 0)
def ArenaSeasonCloseRewardExcelAddRewardParcelUniqueId(builder, RewardParcelUniqueId):
    """This method is deprecated. Please switch to AddRewardParcelUniqueId."""
    return AddRewardParcelUniqueId(builder, RewardParcelUniqueId)
def StartRewardParcelUniqueIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ArenaSeasonCloseRewardExcelStartRewardParcelUniqueIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelUniqueIdVector(builder, numElems)
def AddRewardParcelUniqueName(builder, RewardParcelUniqueName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelUniqueName), 0)
def ArenaSeasonCloseRewardExcelAddRewardParcelUniqueName(builder, RewardParcelUniqueName):
    """This method is deprecated. Please switch to AddRewardParcelUniqueName."""
    return AddRewardParcelUniqueName(builder, RewardParcelUniqueName)
def StartRewardParcelUniqueNameVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArenaSeasonCloseRewardExcelStartRewardParcelUniqueNameVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelUniqueNameVector(builder, numElems)
def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelAmount), 0)
def ArenaSeasonCloseRewardExcelAddRewardParcelAmount(builder, RewardParcelAmount):
    """This method is deprecated. Please switch to AddRewardParcelAmount."""
    return AddRewardParcelAmount(builder, RewardParcelAmount)
def StartRewardParcelAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ArenaSeasonCloseRewardExcelStartRewardParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def ArenaSeasonCloseRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)