# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopRefreshExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopRefreshExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsShopRefreshExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ShopRefreshExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ShopRefreshExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRefreshExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ShopRefreshExcel
    def IsLegacy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ShopRefreshExcel
    def GoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRefreshExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRefreshExcel
    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ShopRefreshExcel
    def RefreshGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ShopRefreshExcel
    def Prob(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ShopRefreshExcel
    def BuyReportEventName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(9)
def ShopRefreshExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def ShopRefreshExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(1, LocalizeEtcId, 0)
def ShopRefreshExcelAddLocalizeEtcId(builder, LocalizeEtcId):
    """This method is deprecated. Please switch to AddLocalizeEtcId."""
    return AddLocalizeEtcId(builder, LocalizeEtcId)
def AddIsLegacy(builder, IsLegacy): builder.PrependBoolSlot(2, IsLegacy, 0)
def ShopRefreshExcelAddIsLegacy(builder, IsLegacy):
    """This method is deprecated. Please switch to AddIsLegacy."""
    return AddIsLegacy(builder, IsLegacy)
def AddGoodsId(builder, GoodsId): builder.PrependInt64Slot(3, GoodsId, 0)
def ShopRefreshExcelAddGoodsId(builder, GoodsId):
    """This method is deprecated. Please switch to AddGoodsId."""
    return AddGoodsId(builder, GoodsId)
def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(4, DisplayOrder, 0)
def ShopRefreshExcelAddDisplayOrder(builder, DisplayOrder):
    """This method is deprecated. Please switch to AddDisplayOrder."""
    return AddDisplayOrder(builder, DisplayOrder)
def AddCategoryType(builder, CategoryType): builder.PrependInt32Slot(5, CategoryType, 0)
def ShopRefreshExcelAddCategoryType(builder, CategoryType):
    """This method is deprecated. Please switch to AddCategoryType."""
    return AddCategoryType(builder, CategoryType)
def AddRefreshGroup(builder, RefreshGroup): builder.PrependInt32Slot(6, RefreshGroup, 0)
def ShopRefreshExcelAddRefreshGroup(builder, RefreshGroup):
    """This method is deprecated. Please switch to AddRefreshGroup."""
    return AddRefreshGroup(builder, RefreshGroup)
def AddProb(builder, Prob): builder.PrependInt32Slot(7, Prob, 0)
def ShopRefreshExcelAddProb(builder, Prob):
    """This method is deprecated. Please switch to AddProb."""
    return AddProb(builder, Prob)
def AddBuyReportEventName(builder, BuyReportEventName): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BuyReportEventName), 0)
def ShopRefreshExcelAddBuyReportEventName(builder, BuyReportEventName):
    """This method is deprecated. Please switch to AddBuyReportEventName."""
    return AddBuyReportEventName(builder, BuyReportEventName)
def End(builder): return builder.EndObject()
def ShopRefreshExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)