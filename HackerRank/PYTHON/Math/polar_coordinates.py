#!/usr/bin/env python3
from cmath import phase

if __name__ == '__main__':
    # 1. Distance from  to origin, i.e., sqrt(x^2 + y^2)
    # 2. Counter clockwise angle measured
    #    from the positive x-axis to the line segment that joins z to the origin.
    z = complex(input())
    print(abs(complex(z.real, z.imag)))
    print(phase(complex(z.real, z.imag)))
