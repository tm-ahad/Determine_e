from math import e
import numpy as np
import time

n = int(input("Precision: "))

se1 = time.perf_counter_ns()

z = np.exp2(1 / n)
x = (z - 1)*n
e1_l = np.exp2(1 / x)
e1_h = np.exp2(z / x)
e1 = (e1_h + e1_l) / 2

ee1 = time.perf_counter_ns()

se2 = time.perf_counter_ns()
e2 = np.power(1 + 1/n, n)
ee2 = time.perf_counter_ns()

print(f"Value of e (Determined by Ahad's law): {e1}")
print(f"Value of e (Determined by Eulers's law): {e2}")
print(f"Value of e (Python standard library): {e}")

d1 = abs(e-e1)
d2 = abs(e-e2)

print(f"Approximate error in calculating the value of e (Ahad's law): {d1}")
print(f"Approximate error in calculating the value of e (Euler's law): {d2}")

if d2 > d1:
    g = 100 - (100*d1/d2)
    t1 = ee1 - se1
    t2 = ee2 - se2
    gt = g * t2/t1

    print(f"Error comparison:")
    print(f"T.M. Ahad's method is more precize by {g}%")
    print(f"Time comparison:")
    print(f"T.M. Ahad's method is slower by {t1/t2}")
    print("T.M. Ahad wins!")
elif d1 > d2:
    g = 100 - (100*d2/d1)
    t1 = ee1 - se1
    t2 = ee2 - se2
    gt = g * t1/t2

    print(f"Error comparison:")
    print(f"Euler's method is more precize by {g}%")
    print("\n")
    print(f"Error & time comparison:")
    print(f"Euler's method is better by {gt}%")
    print("Euler wins!")
else:
    print("Tie!")
