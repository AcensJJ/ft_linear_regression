import os

def price():
    x = -11
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
    FILENAME = ".data"
    # FILENAME = input("Choose your data : ")
    LEN = 2
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            for y in file.readlines():
                l.append(float(y.strip()))
            if len(l) < LEN:
                print("ERROR: data are corrupted")
                l.clear()
                while len(l) < LEN:
                    l.append(0)
            file.close()
    else:
        print("ERROR: data doesnt exist")
        while len(l) < LEN:
            l.append(0)
    return l

print("\n   Predict\n")
x = price()
l = file_value()
price = 0
price = l[0] + l[1] * x
print("\nThe price will be " + str(price) + "$ for " + str(x) + "km.")
