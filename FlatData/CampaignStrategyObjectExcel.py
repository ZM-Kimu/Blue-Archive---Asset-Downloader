# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CampaignStrategyObjectExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CampaignStrategyObjectExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCampaignStrategyObjectExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CampaignStrategyObjectExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CampaignStrategyObjectExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CampaignStrategyObjectExcel
    def PrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CampaignStrategyObjectExcel
    def StrategyObjectType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def StrategyRewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def StrategyRewardID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def StrategyRewardName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CampaignStrategyObjectExcel
    def StrategyRewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def StrategySightRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def PortalId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def HealValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def SwithId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def BuffId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CampaignStrategyObjectExcel
    def Disposable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(15)
def CampaignStrategyObjectExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def CampaignStrategyObjectExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddKey(builder, Key): builder.PrependUint32Slot(1, Key, 0)
def CampaignStrategyObjectExcelAddKey(builder, Key):
    """This method is deprecated. Please switch to AddKey."""
    return AddKey(builder, Key)
def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)
def CampaignStrategyObjectExcelAddName(builder, Name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, Name)
def AddPrefabName(builder, PrefabName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabName), 0)
def CampaignStrategyObjectExcelAddPrefabName(builder, PrefabName):
    """This method is deprecated. Please switch to AddPrefabName."""
    return AddPrefabName(builder, PrefabName)
def AddStrategyObjectType_(builder, StrategyObjectType_): builder.PrependInt32Slot(4, StrategyObjectType_, 0)
def CampaignStrategyObjectExcelAddStrategyObjectType_(builder, StrategyObjectType_):
    """This method is deprecated. Please switch to AddStrategyObjectType_."""
    return AddStrategyObjectType_(builder, StrategyObjectType_)
def AddStrategyRewardParcelType(builder, StrategyRewardParcelType): builder.PrependInt32Slot(5, StrategyRewardParcelType, 0)
def CampaignStrategyObjectExcelAddStrategyRewardParcelType(builder, StrategyRewardParcelType):
    """This method is deprecated. Please switch to AddStrategyRewardParcelType."""
    return AddStrategyRewardParcelType(builder, StrategyRewardParcelType)
def AddStrategyRewardID(builder, StrategyRewardID): builder.PrependInt64Slot(6, StrategyRewardID, 0)
def CampaignStrategyObjectExcelAddStrategyRewardID(builder, StrategyRewardID):
    """This method is deprecated. Please switch to AddStrategyRewardID."""
    return AddStrategyRewardID(builder, StrategyRewardID)
def AddStrategyRewardName(builder, StrategyRewardName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(StrategyRewardName), 0)
def CampaignStrategyObjectExcelAddStrategyRewardName(builder, StrategyRewardName):
    """This method is deprecated. Please switch to AddStrategyRewardName."""
    return AddStrategyRewardName(builder, StrategyRewardName)
def AddStrategyRewardAmount(builder, StrategyRewardAmount): builder.PrependInt32Slot(8, StrategyRewardAmount, 0)
def CampaignStrategyObjectExcelAddStrategyRewardAmount(builder, StrategyRewardAmount):
    """This method is deprecated. Please switch to AddStrategyRewardAmount."""
    return AddStrategyRewardAmount(builder, StrategyRewardAmount)
def AddStrategySightRange(builder, StrategySightRange): builder.PrependInt64Slot(9, StrategySightRange, 0)
def CampaignStrategyObjectExcelAddStrategySightRange(builder, StrategySightRange):
    """This method is deprecated. Please switch to AddStrategySightRange."""
    return AddStrategySightRange(builder, StrategySightRange)
def AddPortalId(builder, PortalId): builder.PrependInt32Slot(10, PortalId, 0)
def CampaignStrategyObjectExcelAddPortalId(builder, PortalId):
    """This method is deprecated. Please switch to AddPortalId."""
    return AddPortalId(builder, PortalId)
def AddHealValue(builder, HealValue): builder.PrependInt32Slot(11, HealValue, 0)
def CampaignStrategyObjectExcelAddHealValue(builder, HealValue):
    """This method is deprecated. Please switch to AddHealValue."""
    return AddHealValue(builder, HealValue)
def AddSwithId(builder, SwithId): builder.PrependInt32Slot(12, SwithId, 0)
def CampaignStrategyObjectExcelAddSwithId(builder, SwithId):
    """This method is deprecated. Please switch to AddSwithId."""
    return AddSwithId(builder, SwithId)
def AddBuffId(builder, BuffId): builder.PrependInt32Slot(13, BuffId, 0)
def CampaignStrategyObjectExcelAddBuffId(builder, BuffId):
    """This method is deprecated. Please switch to AddBuffId."""
    return AddBuffId(builder, BuffId)
def AddDisposable(builder, Disposable): builder.PrependBoolSlot(14, Disposable, 0)
def CampaignStrategyObjectExcelAddDisposable(builder, Disposable):
    """This method is deprecated. Please switch to AddDisposable."""
    return AddDisposable(builder, Disposable)
def End(builder): return builder.EndObject()
def CampaignStrategyObjectExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)