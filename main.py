from incident_matrix import *
from circuit_matrix import *
from cutset_matrix import *

print("Welcome to the Graph theory Calculator\n")
print("Select your choice")
print("1.A matrix Analysis")
print("2.Bf matrix Analysis")
print("3.Qf matrix Analysis")

choice = int(input())
print("\n")
if choice == 1:
    print("1.A matrix Analysis\n")
    amatrix()
elif choice == 2:
    print("2.Bf matrix Analysis\n")
    bfmatrix()
elif choice == 3:
    print("3.Qf matrix Analysis\n")
    qfmatrix()
else:
    print("Invalid!")
