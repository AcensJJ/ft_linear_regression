import os
import csv

def normalise_data(data, min, max):
    return ((data - min) / (max - min))

def mileage():
    x = -1
    while x < 0:
        tmp = input("choose the mileage : ")
        try:
            x = float(tmp)
            if x < 0:
                x = -1
                print("ERROR: needing a positive value")
        except:
            print("ERROR: put a int value")
    return x

def file_value():
    l = []
    v = []
    THETA = ".data"
    # THETA = input("Choose your data : ")
    LEN = 4
    if os.path.exists(THETA):
        with open(THETA, 'r') as file:
            for y in file.readlines():
                if (len(l) < LEN - 2):
                    l.append(float(y.strip()))
                else:
                    v.append(float(y.strip()))
            if len(l) < LEN - 2 or len(v) < 2:
                print("ERROR: data are corrupted")
                l.clear()
                v.clear()
                while len(l) < LEN - 2:
                    l.append(0)
                v = [1, 2]
            file.close()
    else:
        while len(l) < LEN - 2:
            l.append(0)
        v = [1, 2]
    return l, v

print("\n   Predict\n")
val = mileage()
l, normalise = file_value()
x = normalise_data(val, normalise[0], normalise[1])
price = 0
price = round(l[0] + l[1] * x, 2)
print("\nThe price will be " + str(price) + "$ for " + str(val) + "km.")
