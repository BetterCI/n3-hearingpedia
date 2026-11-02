from decimal import Decimal, localcontext
import numpy as np
x = np.float64(1e-16)
naive = np.log(1+x)
stable = np.log1p(x)
with localcontext() as ctx:
    ctx.prec = 80
    reference = (Decimal(1)+Decimal.from_float(float(x))).ln()
    error = abs(Decimal.from_float(float(stable))-reference)
assert naive == 0
assert float(error) < 1e-30
print(naive, stable, error)
