from hypothesis import given, strategies as st
from pymon.base.miscellaneous import MiscellaneousMeter, MiscellaneousStats

@given(st.none())
def test_miscellaneous_stats_validate(_):
    stats = MiscellaneousStats()
    assert stats.validate()

@given(st.none())
def test_miscellaneous_meter_validate(_):
    meter = MiscellaneousMeter()
    assert meter.validate()

@given(st.none())
def test_miscellaneous_meter_render(_):
    meter = MiscellaneousMeter()
    assert meter.render()
