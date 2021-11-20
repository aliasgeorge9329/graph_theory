import numpy as np
from prettytable import PrettyTable
table = PrettyTable()


def bfmatrix():

    r = int(input("Rows in Bf matrix: "))
    c = int(input("Columns in Bf matrix: "))
    g = int(input("No of active elements in Bf matrix: "))

    print("\n Enter The Incident Matrix ( Bf matrix). First number Voltage independent elements,passive,"
          "then dependent Voltage Source\n")

    bf_matrix = []
    for i in range(0, r):
        t = input().strip().split(" ")
        bf_matrix.append(t)
    bf = np.matrix(bf_matrix).astype(int)
    bf_g, bf_p = np.hsplit(bf, np.array([g]))

    print("\n Enter The Z matrix\n")
    z_matrix = []
    for i in range(0, c-g):
        t = input().strip().split(" ")
        z_matrix.append(t)
    z = np.matrix(z_matrix).astype(int)

    print("\n Enter The Independent Vg matrix: ")
    vg_matrix = []
    v_ = input().strip().split(" ")
    vg_matrix.append(v_)
    vg = np.matrix(vg_matrix).astype(float)

    bf_pt = np.transpose(bf_p)
    zp = np.dot(np.dot(bf_p, z), bf_pt)

    table.field_names = ["Bfp", "Z", "Bfp_t", "Vg"]
    table.add_row([bf_p, z, bf_pt, np.transpose(vg)])
    print(f"{table}\n")
    print(f"bfp*z*bfp_t\n{zp}")

    zp_in = np.linalg.inv(zp)
    print(f"\n(bfp*z*bfp_t)^-1\n{zp_in}")

    il = np.dot(np.dot(zp_in, bf_g), np.transpose(vg))*-1
    i = np.dot(np.transpose(bf), il)
    print("\nil\n")
    print(il)

    print("\ni\n")
    print(i)




