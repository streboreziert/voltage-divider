def divide(vin, r1, r2, bits=12, vref=3.3):
    vout = (vin * r2) / (r1 + r2) if (r1 + r2) else 0
    rth = (r1 * r2) / (r1 + r2) if (r1 + r2) else 0
    levels = (1 << bits) - 1
    lsb = vref / levels if levels else 0
    counts = round(vout / lsb) if lsb else 0
    return {
        "Vout": vout,
        "Rth": rth,
        "lsb": lsb,
        "counts": max(0, min(levels, counts)),
        "railing": vout >= vref or vout <= 0,
    }
