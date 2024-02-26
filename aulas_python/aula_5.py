"""
Conversão de tipos, coereção.
type convertion, typecasting, coercion -> é um ato de converter um tipo em outro :
str, int, float e bool
"""
print(int("1"), type(int("1")))
print(str(10 == 10), type(str(10 == 10)))
print(int("2") + 1.8, type(int("2") + 1.8))
print(int(3.3) + float(1), type(int(3.3) + float(1)))
print(bool(1), type(bool(1)))