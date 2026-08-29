from voltage_divider.lib import divide, pick


def test_half():
    d = divide(5, 10000, 10000, 12, 5)
    assert abs(d["Vout"] - 2.5) < 1e-6
    assert pick(5, 2.5)["err"] < 0.05
