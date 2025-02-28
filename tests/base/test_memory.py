from hypothesis import given, strategies as st
from pymon.base.memory import MemoryMeter, MemoryStats

@given(st.none())
def test_memory_stats_validate(_):
    stats = MemoryStats()
    assert stats.validate()

@given(st.none())
def test_memory_meter_validate(_):
    meter = MemoryMeter()
    assert meter.validate()

@given(st.none())
def test_memory_meter_render(_):
    meter = MemoryMeter()
    assert meter.render()
