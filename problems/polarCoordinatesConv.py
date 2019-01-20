#polar coordinates conversion from complex numbers
import cmath
import re

complex_input = input()
complex_input = complex_input.split("+")
real = float(complex_input[0])
imag = float(complex_input[1][0] )

phase = cmath.phase(complex(real,imag))
abs_mod  = abs(complex(real,imag))

print(abs_mod)
print(phase)