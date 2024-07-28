from true_math import divide as tr_dv
from feke_math import divide as fk_dv

result1 = tr_dv(25, 5)
result2 = tr_dv(5, 0)
result3 = fk_dv(30, 10)
result4 = fk_dv(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)