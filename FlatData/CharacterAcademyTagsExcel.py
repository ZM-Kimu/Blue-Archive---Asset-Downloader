# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterAcademyTagsExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterAcademyTagsExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterAcademyTagsExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterAcademyTagsExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterAcademyTagsExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterAcademyTagsExcel
    def FavorTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def FavorTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # CharacterAcademyTagsExcel
    def FavorItemTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # CharacterAcademyTagsExcel
    def ForbiddenTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def ForbiddenTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def ForbiddenTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def ForbiddenTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def Start(builder): builder.StartObject(4)
def CharacterAcademyTagsExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def CharacterAcademyTagsExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddFavorTags(builder, FavorTags): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(FavorTags), 0)
def CharacterAcademyTagsExcelAddFavorTags(builder, FavorTags):
    """This method is deprecated. Please switch to AddFavorTags."""
    return AddFavorTags(builder, FavorTags)
def StartFavorTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterAcademyTagsExcelStartFavorTagsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartFavorTagsVector(builder, numElems)
def AddFavorItemTags(builder, FavorItemTags): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(FavorItemTags), 0)
def CharacterAcademyTagsExcelAddFavorItemTags(builder, FavorItemTags):
    """This method is deprecated. Please switch to AddFavorItemTags."""
    return AddFavorItemTags(builder, FavorItemTags)
def StartFavorItemTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterAcademyTagsExcelStartFavorItemTagsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartFavorItemTagsVector(builder, numElems)
def AddForbiddenTags(builder, ForbiddenTags): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ForbiddenTags), 0)
def CharacterAcademyTagsExcelAddForbiddenTags(builder, ForbiddenTags):
    """This method is deprecated. Please switch to AddForbiddenTags."""
    return AddForbiddenTags(builder, ForbiddenTags)
def StartForbiddenTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterAcademyTagsExcelStartForbiddenTagsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartForbiddenTagsVector(builder, numElems)
def End(builder): return builder.EndObject()
def CharacterAcademyTagsExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)