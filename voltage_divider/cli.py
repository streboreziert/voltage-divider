import argparse, json
from voltage_divider.lib import divide

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--vin", type=float, default=5)
    p.add_argument("--r1", type=float, default=10000)
    p.add_argument("--r2", type=float, default=10000)
    p.add_argument("--bits", type=int, default=12)
    p.add_argument("--vref", type=float, default=3.3)
    a = p.parse_args()
    print(json.dumps(divide(a.vin, a.r1, a.r2, a.bits, a.vref), indent=2))
