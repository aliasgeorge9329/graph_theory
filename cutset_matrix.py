import numpy as np
from prettytable import PrettyTable
table = PrettyTable()


def qfmatrix():

    r = int(input("Rows in Qf matrix: "))
    c = int(input("Columns in Qf matrix: "))
    g = int(input("No of passive elements in Qf matrix: "))

    print("\n Enter The Incident Matrix ( Qf matrix). First number Voltage independent elements,passive,"
          "then dependent Voltage Source\n")

    qf_matrix = []
    for i in range(0, r):
        t = input().strip().split(" ")
        qf_matrix.append(t)
    qf = np.matrix(qf_matrix).astype(int)
    qf_g, qf_p = np.hsplit(qf, np.array([g]))

    print("\n Enter The Y matrix\n")
    y_matrix = []
    for i in range(0, c-g):
        t = input().strip().split(" ")
        y_matrix.append(t)
    y = np.matrix(y_matrix).astype(float)

    print("\n Enter The Independent Ig matrix\n")
    ig_matrix = []
    t = input().strip().split(" ")
    ig_matrix.append(t)
    ig = np.matrix(ig_matrix).astype(int)

    qf_pt = np.transpose(qf_p)
    yp = np.dot(np.dot(qf_p, y), qf_pt)

    table.field_names = ["Qfp", "Y", "Qfp_t", "Ig"]
    table.add_row([qf_p, y, qf_pt, np.transpose(ig)])
    print(f"{table}\n")
    print(f"qfp*y*qfp_t\n{yp}")

    yp_in = np.linalg.inv(yp)
    print(f"\n(qfp*y*qfp_t)^-1\n{yp_in}")

    vn = np.dot(np.dot(yp_in, qf_g), np.transpose(ig))*-1
    vb = np.dot(np.transpose(qf), vn)
    print("\nvn\n")
    print(vn)

    print("\nvb\n")
    print(vb)




