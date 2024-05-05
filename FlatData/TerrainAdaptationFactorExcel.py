# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TerrainAdaptationFactorExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TerrainAdaptationFactorExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTerrainAdaptationFactorExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TerrainAdaptationFactorExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TerrainAdaptationFactorExcel
    def TerrainAdaptation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TerrainAdaptationFactorExcel
    def TerrainAdaptationStat_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TerrainAdaptationFactorExcel
    def ShotFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TerrainAdaptationFactorExcel
    def BlockFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TerrainAdaptationFactorExcel
    def AccuracyFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TerrainAdaptationFactorExcel
    def DodgeFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TerrainAdaptationFactorExcel
    def AttackPowerFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(7)
def TerrainAdaptationFactorExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTerrainAdaptation(builder, TerrainAdaptation): builder.PrependInt32Slot(0, TerrainAdaptation, 0)
def TerrainAdaptationFactorExcelAddTerrainAdaptation(builder, TerrainAdaptation):
    """This method is deprecated. Please switch to AddTerrainAdaptation."""
    return AddTerrainAdaptation(builder, TerrainAdaptation)
def AddTerrainAdaptationStat_(builder, TerrainAdaptationStat_): builder.PrependInt32Slot(1, TerrainAdaptationStat_, 0)
def TerrainAdaptationFactorExcelAddTerrainAdaptationStat_(builder, TerrainAdaptationStat_):
    """This method is deprecated. Please switch to AddTerrainAdaptationStat_."""
    return AddTerrainAdaptationStat_(builder, TerrainAdaptationStat_)
def AddShotFactor(builder, ShotFactor): builder.PrependInt64Slot(2, ShotFactor, 0)
def TerrainAdaptationFactorExcelAddShotFactor(builder, ShotFactor):
    """This method is deprecated. Please switch to AddShotFactor."""
    return AddShotFactor(builder, ShotFactor)
def AddBlockFactor(builder, BlockFactor): builder.PrependInt64Slot(3, BlockFactor, 0)
def TerrainAdaptationFactorExcelAddBlockFactor(builder, BlockFactor):
    """This method is deprecated. Please switch to AddBlockFactor."""
    return AddBlockFactor(builder, BlockFactor)
def AddAccuracyFactor(builder, AccuracyFactor): builder.PrependInt64Slot(4, AccuracyFactor, 0)
def TerrainAdaptationFactorExcelAddAccuracyFactor(builder, AccuracyFactor):
    """This method is deprecated. Please switch to AddAccuracyFactor."""
    return AddAccuracyFactor(builder, AccuracyFactor)
def AddDodgeFactor(builder, DodgeFactor): builder.PrependInt64Slot(5, DodgeFactor, 0)
def TerrainAdaptationFactorExcelAddDodgeFactor(builder, DodgeFactor):
    """This method is deprecated. Please switch to AddDodgeFactor."""
    return AddDodgeFactor(builder, DodgeFactor)
def AddAttackPowerFactor(builder, AttackPowerFactor): builder.PrependInt64Slot(6, AttackPowerFactor, 0)
def TerrainAdaptationFactorExcelAddAttackPowerFactor(builder, AttackPowerFactor):
    """This method is deprecated. Please switch to AddAttackPowerFactor."""
    return AddAttackPowerFactor(builder, AttackPowerFactor)
def End(builder): return builder.EndObject()
def TerrainAdaptationFactorExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)