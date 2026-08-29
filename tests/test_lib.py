from voltage_divider.lib import divide

def test_half():
    d = divide(5, 10000, 10000, 12, 5)
    assert abs(d["Vout"] - 2.5) < 1e-9
    assert d["counts"] == 2048 or abs(d["counts"] - 2047) <= 1
