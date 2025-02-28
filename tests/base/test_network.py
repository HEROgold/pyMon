from hypothesis import given, strategies as st
from pymon.base.network import NetworkMeter, NetworkStats

@given(st.none())
def test_network_stats_validate(_):
    stats = NetworkStats()
    assert stats.validate()

@given(st.none())
def test_network_meter_validate(_):
    meter = NetworkMeter()
    assert meter.validate()

@given(st.none())
def test_network_meter_render(_):
    meter = NetworkMeter()
    assert meter.render()
