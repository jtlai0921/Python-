import decimal  #匯入decimal模組
d1=decimal.Decimal.from_float(123.4567)
d2=decimal.Decimal.from_float(34.5678)
print(d1+d2)
print(decimal.getcontext())
print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)
decimal.getcontext().prec=8
print(d1+d2)