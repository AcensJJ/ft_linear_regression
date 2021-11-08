import os
import csv

FILENAME = "data.csv"

def normalise_data(data, min, max):
    return ((data - min) / (max - min))

def get_min_max():
    v = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            c = csv.DictReader(file)
            for l in c:
                if (len(v) == 0):
                    v = [0, 0]
                    v[0] = (float(l['km']))
                    v[1] = (float(l['km']))
                else :
                    if (v[0] > float(l['km'])):
                        v[0] = float(l['km'])
                    if (v[1] < float(l['km'])):
                        v[1] = float(l['km'])
            file.close()
    else:  
        print("Error: file " + FILENAME + "doesn't exist")
        exit(-1)
    return (v)

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
    THETA = ".data"
    # THETA = input("Choose your data : ")
    LEN = 2
    if os.path.exists(THETA):
        with open(THETA, 'r') as file:
            for y in file.readlines():
                l.append(float(y.strip()))
            if len(l) < LEN:
                print("ERROR: data are corrupted")
                l.clear()
                while len(l) < LEN:
                    l.append(0)
            file.close()
    else:
        while len(l) < LEN:
            l.append(0)
    return l

print("\n   Predict\n")
val = mileage()
normalise = get_min_max()
x = normalise_data(val, normalise[0], normalise[1])
l = file_value()
price = 0
price = round(l[0] + l[1] * x, 2)
print("\nThe price will be " + str(price) + "$ for " + str(val) + "km.")
