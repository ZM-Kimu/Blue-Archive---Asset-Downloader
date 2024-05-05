# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentSpineDialogOffsetExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentSpineDialogOffsetExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEventContentSpineDialogOffsetExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EventContentSpineDialogOffsetExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentSpineDialogOffsetExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentSpineDialogOffsetExcel
    def EventContentType_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentSpineDialogOffsetExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentSpineDialogOffsetExcel
    def SpineOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # EventContentSpineDialogOffsetExcel
    def SpineOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # EventContentSpineDialogOffsetExcel
    def DialogOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # EventContentSpineDialogOffsetExcel
    def DialogOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(7)
def EventContentSpineDialogOffsetExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def EventContentSpineDialogOffsetExcelAddEventContentId(builder, EventContentId):
    """This method is deprecated. Please switch to AddEventContentId."""
    return AddEventContentId(builder, EventContentId)
def AddEventContentType_(builder, EventContentType_): builder.PrependInt32Slot(1, EventContentType_, 0)
def EventContentSpineDialogOffsetExcelAddEventContentType_(builder, EventContentType_):
    """This method is deprecated. Please switch to AddEventContentType_."""
    return AddEventContentType_(builder, EventContentType_)
def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(2, CharacterId, 0)
def EventContentSpineDialogOffsetExcelAddCharacterId(builder, CharacterId):
    """This method is deprecated. Please switch to AddCharacterId."""
    return AddCharacterId(builder, CharacterId)
def AddSpineOffsetX(builder, SpineOffsetX): builder.PrependFloat32Slot(3, SpineOffsetX, 0.0)
def EventContentSpineDialogOffsetExcelAddSpineOffsetX(builder, SpineOffsetX):
    """This method is deprecated. Please switch to AddSpineOffsetX."""
    return AddSpineOffsetX(builder, SpineOffsetX)
def AddSpineOffsetY(builder, SpineOffsetY): builder.PrependFloat32Slot(4, SpineOffsetY, 0.0)
def EventContentSpineDialogOffsetExcelAddSpineOffsetY(builder, SpineOffsetY):
    """This method is deprecated. Please switch to AddSpineOffsetY."""
    return AddSpineOffsetY(builder, SpineOffsetY)
def AddDialogOffsetX(builder, DialogOffsetX): builder.PrependFloat32Slot(5, DialogOffsetX, 0.0)
def EventContentSpineDialogOffsetExcelAddDialogOffsetX(builder, DialogOffsetX):
    """This method is deprecated. Please switch to AddDialogOffsetX."""
    return AddDialogOffsetX(builder, DialogOffsetX)
def AddDialogOffsetY(builder, DialogOffsetY): builder.PrependFloat32Slot(6, DialogOffsetY, 0.0)
def EventContentSpineDialogOffsetExcelAddDialogOffsetY(builder, DialogOffsetY):
    """This method is deprecated. Please switch to AddDialogOffsetY."""
    return AddDialogOffsetY(builder, DialogOffsetY)
def End(builder): return builder.EndObject()
def EventContentSpineDialogOffsetExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)