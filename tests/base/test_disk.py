from hypothesis import given, strategies as st
from pymon.base.disk import DiskMeter, DiskStats

@given(st.none())
def test_disk_stats_validate(_):
    stats = DiskStats()
    assert stats.validate()

@given(st.none())
def test_disk_meter_validate(_):
    meter = DiskMeter()
    assert meter.validate()

@given(st.none())
def test_disk_meter_render(_):
    meter = DiskMeter()
    assert meter.render()
