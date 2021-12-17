from day17 import *


def test_simulate_shot():
    probe = Probe.create(Point(7, 2))
    target = TargetRange.from_str("target area: x=20..30, y=-10..-5")

    assert simulate_shot(probe, target) == 3


def test_brute_force():
    target = TargetRange.from_str("target area: x=20..30, y=-10..-5")

    shot_results = brute_force(target)
    assert max(shot_results) == 45
    assert len(shot_results) == 112
