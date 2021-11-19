# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopRecruitExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopRecruitExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsShopRecruitExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ShopRecruitExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ShopRecruitExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def IsLegacy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ShopRecruitExcel
    def GoodsId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ShopRecruitExcel
    def GoodsIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ShopRecruitExcel
    def GoodsIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ShopRecruitExcel
    def GoodsIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ShopRecruitExcel
    def GoodsDevName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ShopRecruitExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def MovieBannerPath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # ShopRecruitExcel
    def MovieBannerPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ShopRecruitExcel
    def MovieBannerPathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # ShopRecruitExcel
    def LinkedRobbyBannerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def InfoCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ShopRecruitExcel
    def InfoCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ShopRecruitExcel
    def InfoCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ShopRecruitExcel
    def InfoCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # ShopRecruitExcel
    def SalePeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ShopRecruitExcel
    def SalePeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ShopRecruitExcel
    def RecruitCoinId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def RecruitSellectionShopId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def PurchaseCooltimeMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def PurchaseCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def PurchaseCountResetType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ShopRecruitExcel
    def ProbabilityUrlDev(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ShopRecruitExcel
    def ProbabilityUrlLive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(18)
def ShopRecruitExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def ShopRecruitExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddCategoryType(builder, CategoryType): builder.PrependInt32Slot(1, CategoryType, 0)
def ShopRecruitExcelAddCategoryType(builder, CategoryType):
    """This method is deprecated. Please switch to AddCategoryType."""
    return AddCategoryType(builder, CategoryType)
def AddIsLegacy(builder, IsLegacy): builder.PrependBoolSlot(2, IsLegacy, 0)
def ShopRecruitExcelAddIsLegacy(builder, IsLegacy):
    """This method is deprecated. Please switch to AddIsLegacy."""
    return AddIsLegacy(builder, IsLegacy)
def AddGoodsId(builder, GoodsId): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(GoodsId), 0)
def ShopRecruitExcelAddGoodsId(builder, GoodsId):
    """This method is deprecated. Please switch to AddGoodsId."""
    return AddGoodsId(builder, GoodsId)
def StartGoodsIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ShopRecruitExcelStartGoodsIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartGoodsIdVector(builder, numElems)
def AddGoodsDevName(builder, GoodsDevName): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(GoodsDevName), 0)
def ShopRecruitExcelAddGoodsDevName(builder, GoodsDevName):
    """This method is deprecated. Please switch to AddGoodsDevName."""
    return AddGoodsDevName(builder, GoodsDevName)
def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(5, DisplayOrder, 0)
def ShopRecruitExcelAddDisplayOrder(builder, DisplayOrder):
    """This method is deprecated. Please switch to AddDisplayOrder."""
    return AddDisplayOrder(builder, DisplayOrder)
def AddMovieBannerPath(builder, MovieBannerPath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(MovieBannerPath), 0)
def ShopRecruitExcelAddMovieBannerPath(builder, MovieBannerPath):
    """This method is deprecated. Please switch to AddMovieBannerPath."""
    return AddMovieBannerPath(builder, MovieBannerPath)
def StartMovieBannerPathVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ShopRecruitExcelStartMovieBannerPathVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMovieBannerPathVector(builder, numElems)
def AddLinkedRobbyBannerId(builder, LinkedRobbyBannerId): builder.PrependInt64Slot(7, LinkedRobbyBannerId, 0)
def ShopRecruitExcelAddLinkedRobbyBannerId(builder, LinkedRobbyBannerId):
    """This method is deprecated. Please switch to AddLinkedRobbyBannerId."""
    return AddLinkedRobbyBannerId(builder, LinkedRobbyBannerId)
def AddInfoCharacterId(builder, InfoCharacterId): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(InfoCharacterId), 0)
def ShopRecruitExcelAddInfoCharacterId(builder, InfoCharacterId):
    """This method is deprecated. Please switch to AddInfoCharacterId."""
    return AddInfoCharacterId(builder, InfoCharacterId)
def StartInfoCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ShopRecruitExcelStartInfoCharacterIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartInfoCharacterIdVector(builder, numElems)
def AddSalePeriodFrom(builder, SalePeriodFrom): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodFrom), 0)
def ShopRecruitExcelAddSalePeriodFrom(builder, SalePeriodFrom):
    """This method is deprecated. Please switch to AddSalePeriodFrom."""
    return AddSalePeriodFrom(builder, SalePeriodFrom)
def AddSalePeriodTo(builder, SalePeriodTo): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodTo), 0)
def ShopRecruitExcelAddSalePeriodTo(builder, SalePeriodTo):
    """This method is deprecated. Please switch to AddSalePeriodTo."""
    return AddSalePeriodTo(builder, SalePeriodTo)
def AddRecruitCoinId(builder, RecruitCoinId): builder.PrependInt64Slot(11, RecruitCoinId, 0)
def ShopRecruitExcelAddRecruitCoinId(builder, RecruitCoinId):
    """This method is deprecated. Please switch to AddRecruitCoinId."""
    return AddRecruitCoinId(builder, RecruitCoinId)
def AddRecruitSellectionShopId(builder, RecruitSellectionShopId): builder.PrependInt64Slot(12, RecruitSellectionShopId, 0)
def ShopRecruitExcelAddRecruitSellectionShopId(builder, RecruitSellectionShopId):
    """This method is deprecated. Please switch to AddRecruitSellectionShopId."""
    return AddRecruitSellectionShopId(builder, RecruitSellectionShopId)
def AddPurchaseCooltimeMin(builder, PurchaseCooltimeMin): builder.PrependInt64Slot(13, PurchaseCooltimeMin, 0)
def ShopRecruitExcelAddPurchaseCooltimeMin(builder, PurchaseCooltimeMin):
    """This method is deprecated. Please switch to AddPurchaseCooltimeMin."""
    return AddPurchaseCooltimeMin(builder, PurchaseCooltimeMin)
def AddPurchaseCountLimit(builder, PurchaseCountLimit): builder.PrependInt64Slot(14, PurchaseCountLimit, 0)
def ShopRecruitExcelAddPurchaseCountLimit(builder, PurchaseCountLimit):
    """This method is deprecated. Please switch to AddPurchaseCountLimit."""
    return AddPurchaseCountLimit(builder, PurchaseCountLimit)
def AddPurchaseCountResetType_(builder, PurchaseCountResetType_): builder.PrependInt32Slot(15, PurchaseCountResetType_, 0)
def ShopRecruitExcelAddPurchaseCountResetType_(builder, PurchaseCountResetType_):
    """This method is deprecated. Please switch to AddPurchaseCountResetType_."""
    return AddPurchaseCountResetType_(builder, PurchaseCountResetType_)
def AddProbabilityUrlDev(builder, ProbabilityUrlDev): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(ProbabilityUrlDev), 0)
def ShopRecruitExcelAddProbabilityUrlDev(builder, ProbabilityUrlDev):
    """This method is deprecated. Please switch to AddProbabilityUrlDev."""
    return AddProbabilityUrlDev(builder, ProbabilityUrlDev)
def AddProbabilityUrlLive(builder, ProbabilityUrlLive): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(ProbabilityUrlLive), 0)
def ShopRecruitExcelAddProbabilityUrlLive(builder, ProbabilityUrlLive):
    """This method is deprecated. Please switch to AddProbabilityUrlLive."""
    return AddProbabilityUrlLive(builder, ProbabilityUrlLive)
def End(builder): return builder.EndObject()
def ShopRecruitExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)