# voltage-divider

Vout and Thevenin. For ADC rails and bias networks.

Live: [https://robertstreize.com/lab.html#divider](https://robertstreize.com/lab.html#divider) · part of [treize-lab](https://github.com/streboreziert/treize-lab)

## Extra

ADC counts, load error, Johnson noise, E24 pair search for a target Vout.

Was a one-function calculator. This is the product.

Maps Vout onto an N-bit ADC: counts, LSB, and whether you are railing.

## Install

```bash
python3 -m pip install -e .
voltage_divider --vin 3.3 --r1 10000 --r2 4700 --bits 12 --vref 3.3
```

MIT · Roberts Treize · [robertstreize.com](https://robertstreize.com)
