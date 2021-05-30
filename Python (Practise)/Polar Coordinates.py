# Enter your code here. Read input from STDIN. Print output to STDOUT

# z = x + y*j

import cmath

my_num = input()

print(abs(complex(my_num)))
print(cmath.phase(complex(my_num)))
