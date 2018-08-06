import sys
#sys.path.append("/home/dsbrown/Documents/ACES/github/Python2/")
#print(sys.path)
from package_test import module_test

added = module_test.my_add(3,5)
print(added)
multiplied = module_test.my_mult(5,6)
print(multiplied)
divided = module_test.my_divide(5,2)
print(divided)
