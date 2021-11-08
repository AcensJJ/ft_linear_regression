import os
import sys
import csv

RATIO = 0.1
ITER = 1000

def normalise_data(data, min, max):
    return ((data - min) / (max - min))

def estimated_price(t, km):
    return (t[0] + t[1] * km)

def calcul0(t, km, price):
    v2 = estimated_price(t, km) - price
    return v2
    
def calcul1(t, km, price):
    v2 = estimated_price(t, km) - price
    return v2 * km
    
def create_file(list):
    with open(".data", 'w+') as file:
        for l in list:
            file.write(str(l) + "\n")
        file.close()

def get_size_file(FILENAME):
    with open(FILENAME, 'r') as file:
        tmp = len(file.readlines()) - 1
        file.close()
        return (tmp)

def get_min_max(FILENAME):
    v = []
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
        return (v)

if (len(sys.argv) < 2):
    print("Error: no file data included")
    exit(-1)

FILENAME = str(sys.argv[1])
if os.path.exists(FILENAME):
    size = get_size_file(FILENAME)
    v = get_min_max(FILENAME)
    t = [0, 0]
    for i in range(ITER):
        with open(FILENAME, 'r') as file:
            c = csv.DictReader(file)
            somme = [0, 0]
            for l in c:
                km = normalise_data(float(l['km']), v[0], v[1])
                price = float(l['price'])
                somme[0] += calcul0(t, km, price)
                somme[1] += calcul1(t, km, price)
            t[0] -= RATIO * (1/size) * somme[0]
            t[1] -= RATIO * (1/size) * somme[1]
            file.close()
    create_file(t)
else:
    print("Error: file " + FILENAME + "doesn't exist")