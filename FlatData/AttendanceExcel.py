# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AttendanceExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AttendanceExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAttendanceExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AttendanceExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AttendanceExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def AccountType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def AccountLevelLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def Title(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AttendanceExcel
    def InfomationLocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AttendanceExcel
    def CountRule(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def CountReset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def BookSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def StartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AttendanceExcel
    def StartableEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AttendanceExcel
    def EndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AttendanceExcel
    def ExpiryDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def MailType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def DialogCategory_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AttendanceExcel
    def TitleImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AttendanceExcel
    def DecorationImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(18)
def AttendanceExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def AttendanceExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddType(builder, Type): builder.PrependInt32Slot(1, Type, 0)
def AttendanceExcelAddType(builder, Type):
    """This method is deprecated. Please switch to AddType."""
    return AddType(builder, Type)
def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(2, DisplayOrder, 0)
def AttendanceExcelAddDisplayOrder(builder, DisplayOrder):
    """This method is deprecated. Please switch to AddDisplayOrder."""
    return AddDisplayOrder(builder, DisplayOrder)
def AddAccountType(builder, AccountType): builder.PrependInt32Slot(3, AccountType, 0)
def AttendanceExcelAddAccountType(builder, AccountType):
    """This method is deprecated. Please switch to AddAccountType."""
    return AddAccountType(builder, AccountType)
def AddAccountLevelLimit(builder, AccountLevelLimit): builder.PrependInt64Slot(4, AccountLevelLimit, 0)
def AttendanceExcelAddAccountLevelLimit(builder, AccountLevelLimit):
    """This method is deprecated. Please switch to AddAccountLevelLimit."""
    return AddAccountLevelLimit(builder, AccountLevelLimit)
def AddTitle(builder, Title): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(Title), 0)
def AttendanceExcelAddTitle(builder, Title):
    """This method is deprecated. Please switch to AddTitle."""
    return AddTitle(builder, Title)
def AddInfomationLocalizeCode(builder, InfomationLocalizeCode): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(InfomationLocalizeCode), 0)
def AttendanceExcelAddInfomationLocalizeCode(builder, InfomationLocalizeCode):
    """This method is deprecated. Please switch to AddInfomationLocalizeCode."""
    return AddInfomationLocalizeCode(builder, InfomationLocalizeCode)
def AddCountRule(builder, CountRule): builder.PrependInt32Slot(7, CountRule, 0)
def AttendanceExcelAddCountRule(builder, CountRule):
    """This method is deprecated. Please switch to AddCountRule."""
    return AddCountRule(builder, CountRule)
def AddCountReset(builder, CountReset): builder.PrependInt32Slot(8, CountReset, 0)
def AttendanceExcelAddCountReset(builder, CountReset):
    """This method is deprecated. Please switch to AddCountReset."""
    return AddCountReset(builder, CountReset)
def AddBookSize(builder, BookSize): builder.PrependInt64Slot(9, BookSize, 0)
def AttendanceExcelAddBookSize(builder, BookSize):
    """This method is deprecated. Please switch to AddBookSize."""
    return AddBookSize(builder, BookSize)
def AddStartDate(builder, StartDate): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(StartDate), 0)
def AttendanceExcelAddStartDate(builder, StartDate):
    """This method is deprecated. Please switch to AddStartDate."""
    return AddStartDate(builder, StartDate)
def AddStartableEndDate(builder, StartableEndDate): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(StartableEndDate), 0)
def AttendanceExcelAddStartableEndDate(builder, StartableEndDate):
    """This method is deprecated. Please switch to AddStartableEndDate."""
    return AddStartableEndDate(builder, StartableEndDate)
def AddEndDate(builder, EndDate): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(EndDate), 0)
def AttendanceExcelAddEndDate(builder, EndDate):
    """This method is deprecated. Please switch to AddEndDate."""
    return AddEndDate(builder, EndDate)
def AddExpiryDate(builder, ExpiryDate): builder.PrependInt64Slot(13, ExpiryDate, 0)
def AttendanceExcelAddExpiryDate(builder, ExpiryDate):
    """This method is deprecated. Please switch to AddExpiryDate."""
    return AddExpiryDate(builder, ExpiryDate)
def AddMailType_(builder, MailType_): builder.PrependInt32Slot(14, MailType_, 0)
def AttendanceExcelAddMailType_(builder, MailType_):
    """This method is deprecated. Please switch to AddMailType_."""
    return AddMailType_(builder, MailType_)
def AddDialogCategory_(builder, DialogCategory_): builder.PrependInt32Slot(15, DialogCategory_, 0)
def AttendanceExcelAddDialogCategory_(builder, DialogCategory_):
    """This method is deprecated. Please switch to AddDialogCategory_."""
    return AddDialogCategory_(builder, DialogCategory_)
def AddTitleImagePath(builder, TitleImagePath): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(TitleImagePath), 0)
def AttendanceExcelAddTitleImagePath(builder, TitleImagePath):
    """This method is deprecated. Please switch to AddTitleImagePath."""
    return AddTitleImagePath(builder, TitleImagePath)
def AddDecorationImagePath(builder, DecorationImagePath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(DecorationImagePath), 0)
def AttendanceExcelAddDecorationImagePath(builder, DecorationImagePath):
    """This method is deprecated. Please switch to AddDecorationImagePath."""
    return AddDecorationImagePath(builder, DecorationImagePath)
def End(builder): return builder.EndObject()
def AttendanceExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)