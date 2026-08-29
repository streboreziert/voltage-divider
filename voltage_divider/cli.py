import argparse
import json

from voltage_divider.lib import divide, pick


def main() -> None:
    p = argparse.ArgumentParser(description="Divider + ADC + E24 pick")
    p.add_argument("--vin", type=float, default=5)
    p.add_argument("--r1", type=float, default=10000)
    p.add_argument("--r2", type=float, default=10000)
    p.add_argument("--bits", type=int, default=12)
    p.add_argument("--vref", type=float, default=3.3)
    p.add_argument("--load", type=float, default=1e12)
    p.add_argument("--pick", type=float, help="target Vout")
    a = p.parse_args()
    if a.pick is not None:
        print(json.dumps(pick(a.vin, a.pick), indent=2))
    else:
        print(json.dumps(divide(a.vin, a.r1, a.r2, a.bits, a.vref, a.load), indent=2))
