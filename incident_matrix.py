import numpy as np
from prettytable import PrettyTable
table = PrettyTable()


def amatrix():

    r = int(input("Rows in A matrix: "))
    c = int(input("Columns in A matrix: "))
    p = int(input("No of passive elements in A matrix: "))

    print("\n Enter The Incident Matrix ( A matrix). First number passive elements,Current dependent,"
          "then independent Current Source\n")

    a_matrix = []
    for i in range(0, r):
        t = input().strip().split(" ")
        a_matrix.append(t)
    a = np.matrix(a_matrix).astype(int)
    a_p, a_g = np.hsplit(a, np.array([p]))

    print("\n Enter The Y matrix in (Enter Resistance Value)\n")
    y_matrix = []
    for i in range(0, p):
        t = input().strip().split(" ")
        t_ = []
        for each in t:
            if each != "0":
                t_.append(1 / float(each))
            else:
                t_.append(int(each))
        y_matrix.append(t_)
    y = np.matrix(y_matrix).astype(float)

    print("\n Enter The Independent Ig matrix\n")
    ig_matrix = []
    t = input().strip().split(" ")
    ig_matrix.append(t)
    ig = np.matrix(ig_matrix).astype(float)

    a_pt = np.transpose(a_p)
    yp = np.dot(np.dot(a_p, y), a_pt)

    table.field_names = ["Ap", "Y", "Apt", "Ig"]
    table.add_row([a_p, y, a_pt, np.transpose(ig)])
    print(f"{table}\n")
    print(f"ap*y*ap_t\n{yp}")

    yp_in = np.linalg.inv(yp)
    print(f"\n(ap*y*ap_t)^-1\n{yp_in}")

    vn = np.dot(np.dot(yp_in, a_g), np.transpose(ig))
    vb = np.dot(np.transpose(a), vn)
    print("\nvn\n")
    print(vn)

    print("\nvb\n")
    print(vb)




