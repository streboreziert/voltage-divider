"""Divider + ADC + Johnson noise + E24 pair search for a target Vout."""
from __future__ import annotations

import math

E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]


def divide(vin: float, r1: float, r2: float, bits: int = 12, vref: float = 3.3, load: float = 1e12, temp_c: float = 25) -> dict:
    rpar = (r2 * load) / (r2 + load) if load else r2
    vout = (vin * rpar) / (r1 + rpar) if (r1 + rpar) else 0
    rth = (r1 * rpar) / (r1 + rpar) if (r1 + rpar) else 0
    levels = (1 << bits) - 1
    lsb = vref / levels if levels else 0
    counts = round(vout / lsb) if lsb else 0
    # Johnson noise density
    kb = 1.380649e-23
    vn = math.sqrt(4 * kb * (temp_c + 273.15) * rth)  # V/√Hz
    return {
        "Vout": vout,
        "Rth": rth,
        "lsb": lsb,
        "counts": max(0, min(levels, counts)),
        "railing": vout >= vref * 0.999 or vout <= 0,
        "load_error_pct": ((vin * r2 / (r1 + r2) - vout) / max(vout, 1e-12)) * 100,
        "johnson_nV_rtHz": vn * 1e9,
    }


def pick(vin: float, vout: float, decade: float = 10000) -> dict:
    best = None
    for a in E24:
        for b in E24:
            r1, r2 = a * decade, b * decade
            vo = vin * r2 / (r1 + r2)
            err = abs(vo - vout)
            if best is None or err < best["err"]:
                best = {"r1": r1, "r2": r2, "Vout": vo, "err": err}
    return best
