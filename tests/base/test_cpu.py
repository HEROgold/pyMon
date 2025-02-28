from hypothesis import given, strategies as st
from pymon.base.cpu import CPUMeter, CPUStats

@given(st.none())
def test_cpu_stats_validate(_):
    stats = CPUStats()
    assert stats.validate()

@given(st.none())
def test_cpu_meter_validate(_):
    meter = CPUMeter()
    assert meter.validate()

@given(st.none())
def test_cpu_meter_render(_):
    meter = CPUMeter()
    assert meter.render()
