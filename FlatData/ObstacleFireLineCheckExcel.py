# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObstacleFireLineCheckExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObstacleFireLineCheckExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsObstacleFireLineCheckExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ObstacleFireLineCheckExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ObstacleFireLineCheckExcel
    def MyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ObstacleFireLineCheckExcel
    def AllyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ObstacleFireLineCheckExcel
    def EnemyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ObstacleFireLineCheckExcel
    def EmptyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(4)
def ObstacleFireLineCheckExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddMyObstacleFireLineCheck(builder, MyObstacleFireLineCheck): builder.PrependBoolSlot(0, MyObstacleFireLineCheck, 0)
def ObstacleFireLineCheckExcelAddMyObstacleFireLineCheck(builder, MyObstacleFireLineCheck):
    """This method is deprecated. Please switch to AddMyObstacleFireLineCheck."""
    return AddMyObstacleFireLineCheck(builder, MyObstacleFireLineCheck)
def AddAllyObstacleFireLineCheck(builder, AllyObstacleFireLineCheck): builder.PrependBoolSlot(1, AllyObstacleFireLineCheck, 0)
def ObstacleFireLineCheckExcelAddAllyObstacleFireLineCheck(builder, AllyObstacleFireLineCheck):
    """This method is deprecated. Please switch to AddAllyObstacleFireLineCheck."""
    return AddAllyObstacleFireLineCheck(builder, AllyObstacleFireLineCheck)
def AddEnemyObstacleFireLineCheck(builder, EnemyObstacleFireLineCheck): builder.PrependBoolSlot(2, EnemyObstacleFireLineCheck, 0)
def ObstacleFireLineCheckExcelAddEnemyObstacleFireLineCheck(builder, EnemyObstacleFireLineCheck):
    """This method is deprecated. Please switch to AddEnemyObstacleFireLineCheck."""
    return AddEnemyObstacleFireLineCheck(builder, EnemyObstacleFireLineCheck)
def AddEmptyObstacleFireLineCheck(builder, EmptyObstacleFireLineCheck): builder.PrependBoolSlot(3, EmptyObstacleFireLineCheck, 0)
def ObstacleFireLineCheckExcelAddEmptyObstacleFireLineCheck(builder, EmptyObstacleFireLineCheck):
    """This method is deprecated. Please switch to AddEmptyObstacleFireLineCheck."""
    return AddEmptyObstacleFireLineCheck(builder, EmptyObstacleFireLineCheck)
def End(builder): return builder.EndObject()
def ObstacleFireLineCheckExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)