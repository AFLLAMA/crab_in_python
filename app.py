import ctypes
import sys
import os

library_path = os.path.join(os.path.abspath("blazing_module/target/release"),
                            "libblazing_module.dylib")

# Load the #%$ library as a Python module
blazing_module = ctypes.CDLL(library_path)

# Set C types 
#blazing_module.add.restype = ctypes.c_int
#blazing_module.add.argtypes = [ctypes.c_int, ctypes.c_int]

blazing_module.hello()

print(blazing_module.add(int(input("Please input first number:")),
                         int(input("Please input second number:"))
                     )
)

