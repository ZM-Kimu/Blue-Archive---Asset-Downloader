# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ArenaRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArenaRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsArenaRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ArenaRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArenaRewardExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaRewardExcel
    def ArenaRewardType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ArenaRewardExcel
    def RankStart(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaRewardExcel
    def RankEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaRewardExcel
    def RankIconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ArenaRewardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ArenaRewardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ArenaRewardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaRewardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # ArenaRewardExcel
    def RewardParcelUniqueId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArenaRewardExcel
    def RewardParcelUniqueIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArenaRewardExcel
    def RewardParcelUniqueIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaRewardExcel
    def RewardParcelUniqueIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # ArenaRewardExcel
    def RewardParcelUniqueName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # ArenaRewardExcel
    def RewardParcelUniqueNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaRewardExcel
    def RewardParcelUniqueNameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # ArenaRewardExcel
    def RewardParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArenaRewardExcel
    def RewardParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArenaRewardExcel
    def RewardParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaRewardExcel
    def RewardParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

def Start(builder): builder.StartObject(9)
def ArenaRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)
def ArenaRewardExcelAddUniqueId(builder, UniqueId):
    """This method is deprecated. Please switch to AddUniqueId."""
    return AddUniqueId(builder, UniqueId)
def AddArenaRewardType_(builder, ArenaRewardType_): builder.PrependInt32Slot(1, ArenaRewardType_, 0)
def ArenaRewardExcelAddArenaRewardType_(builder, ArenaRewardType_):
    """This method is deprecated. Please switch to AddArenaRewardType_."""
    return AddArenaRewardType_(builder, ArenaRewardType_)
def AddRankStart(builder, RankStart): builder.PrependInt64Slot(2, RankStart, 0)
def ArenaRewardExcelAddRankStart(builder, RankStart):
    """This method is deprecated. Please switch to AddRankStart."""
    return AddRankStart(builder, RankStart)
def AddRankEnd(builder, RankEnd): builder.PrependInt64Slot(3, RankEnd, 0)
def ArenaRewardExcelAddRankEnd(builder, RankEnd):
    """This method is deprecated. Please switch to AddRankEnd."""
    return AddRankEnd(builder, RankEnd)
def AddRankIconPath(builder, RankIconPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(RankIconPath), 0)
def ArenaRewardExcelAddRankIconPath(builder, RankIconPath):
    """This method is deprecated. Please switch to AddRankIconPath."""
    return AddRankIconPath(builder, RankIconPath)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def ArenaRewardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def StartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArenaRewardExcelStartRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelTypeVector(builder, numElems)
def AddRewardParcelUniqueId(builder, RewardParcelUniqueId): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelUniqueId), 0)
def ArenaRewardExcelAddRewardParcelUniqueId(builder, RewardParcelUniqueId):
    """This method is deprecated. Please switch to AddRewardParcelUniqueId."""
    return AddRewardParcelUniqueId(builder, RewardParcelUniqueId)
def StartRewardParcelUniqueIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ArenaRewardExcelStartRewardParcelUniqueIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelUniqueIdVector(builder, numElems)
def AddRewardParcelUniqueName(builder, RewardParcelUniqueName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelUniqueName), 0)
def ArenaRewardExcelAddRewardParcelUniqueName(builder, RewardParcelUniqueName):
    """This method is deprecated. Please switch to AddRewardParcelUniqueName."""
    return AddRewardParcelUniqueName(builder, RewardParcelUniqueName)
def StartRewardParcelUniqueNameVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArenaRewardExcelStartRewardParcelUniqueNameVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelUniqueNameVector(builder, numElems)
def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelAmount), 0)
def ArenaRewardExcelAddRewardParcelAmount(builder, RewardParcelAmount):
    """This method is deprecated. Please switch to AddRewardParcelAmount."""
    return AddRewardParcelAmount(builder, RewardParcelAmount)
def StartRewardParcelAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ArenaRewardExcelStartRewardParcelAmountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelAmountVector(builder, numElems)
def End(builder): return builder.EndObject()
def ArenaRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)