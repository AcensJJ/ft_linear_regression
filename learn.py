import os
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import array

RATIO = 0.1
ITER = 1000
PRECI = True
DRAW = True

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

def learn(FILENAME, v, size):
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
    return t

def calc_precision(FILENAME, v, t, size):
    preci = 0
    with open(FILENAME, 'r') as file:
        c = csv.DictReader(file)
        for l in c:
            calc = estimated_price(t, normalise_data(float(l['km']), v[0], v[1]))
            calc = 100 / float(l['price']) * calc
            if calc > 100:
                calc = 200 - calc
            preci += calc
        file.close()
    return round((preci/size), 2)

def draw_graph(FILENAME, v, t):
    # plt.xkcd()
    # plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(facecolor=(.18, .31, .31))
    ax.set_title("ft_linear_regression")
    ax.set_xlabel("mileage (km)", color='peachpuff')
    ax.set_ylabel("price ($)", color='c')
    ax.tick_params(labelcolor='tab:orange')
    data = pd.read_csv(FILENAME, index_col=False)
    ax.scatter(data['km'], data['price'], label="data", color='C4')
    with open(FILENAME, 'r') as file:
        c = csv.DictReader(file)
        ylist = []
        for l in c:
            calc = estimated_price(t, normalise_data(float(l['km']), v[0], v[1]))
            ylist.append(calc)
        ax.plot(data['km'], ylist, label="linear", color='tab:red')
        ax.legend()
        plt.tight_layout()
        plt.savefig('ft_linear_regression.png')
        plt.show()
        file.close()


if (len(sys.argv) < 2):
    print("Error: no file data included")
    exit(-1)
FILENAME = str(sys.argv[1])
if os.path.exists(FILENAME):
    size = get_size_file(FILENAME)
    v = get_min_max(FILENAME)
    print("\n  Welcome to the learning part  \n\nStarting learning", ITER, "time")
    t = learn(FILENAME, v, size) 
    print("End\n")
    create_file(learn(FILENAME, v, size))
    if (PRECI):
        print("- precision = ", calc_precision(FILENAME, v, t, size), "%")
    if (DRAW):
        draw_graph(FILENAME, v, t)
else:
    print("Error: file " + FILENAME + "doesn't exist")