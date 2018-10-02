#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import pandas
import numpy
import math

def histogram_times(filename):
    df = pandas.read_csv(filename)
    arr = [0 for i in range(24)]
    #pandas.DataFrame(df, columns = ['Date', 'Time', 'Location', 'Operator', 'Flight #', 'Route', 'Type', 'Registration', 'cn/In', 'Aboard', 'Fatalities', 'Ground', 'Summary']
    for i in range(0, len(df)):
        s = df.loc[i].ix[1]
        try:
            int(s[:2])
        except:
            continue
        arr[int(s[:2]) % 24] = arr[int(s[:2]) % 24] + 1
    #print(arr);
    return arr

def weigh_pokemons(filename, weight):
    weighted = list()
    with open(filename) as json_data:
        pokeList = json.load(json_data)
    for i in range(len(pokeList['pokemon'])):
        if (weight == float(pokeList['pokemon'][i]['weight'][:4])):
            weighted.append(pokeList['pokemon'][i]['name'])
            #print(pokeList['pokemon'][i]['weight'])
    #print(weighted)
    return weighted

def single_type_candy_count(filename):
    count = 0;
    with open(filename) as json_data:
        pokeList = json.load(json_data)
        #print(pokeList)
    for i in range(len(pokeList['pokemon'])):
        if len(pokeList['pokemon'][i]['type']) == 1 :
            count += 1;
    print(count)
    return count

def reflections_and_projections(points):
    points = numpy.array(points)
    points[1] = (points[1] * -1) + 2
    print(points)
    for i in range(len(points)) :
        a = math.cos(math.pi/2) * points[i][0] - math.sin(math.pi/2) * points[i][1]
        b = math.sin(math.pi/2) * points[i][0] + math.cos(math.pi/2) * points[i][1]
        points[i][0] = a
        points[i][1] = b
    for i in range(len(points)) :
        a = points[i][0] + 3*points[i][1]
        b = 3*points[i][0] + 9*points[i][1]
        points[i][0] = a/10
        points[i][1] = b/10
    return points

def normalize(image):
    min = image.min()
    max = image.max()
    if min == max:
        return image
    image = (255/(max-min)) * (image-min)
    return image

def sigmoid_normalize(image, a):
    image = 255 / ( 1 + e ** (1/-a)*(image - 128))
    return image

filename = "pokedex.json"
#histogram_times(filename)
#weigh_pokemons(filename, 10)
#{'id': 151, 'num': '151', 'name': 'Mew', 'img': 'http://www.serebii.net/pokemongo/pokemon/151.png', 'type': ['Psychic'], 'height': '0.41 m', 'weight': '4.0 kg', 'candy': 'None', 'egg': 'Not in Eggs', 'spawn_chance': 0, 'avg_spawns': 0, 'spawn_time': 'N/A', 'multipliers': None, 'weaknesses': ['Bug', 'Ghost', 'Dark']}]}
#single_type_candy_count(filename)
print(reflections_and_projections([[1,2,3,4,5,6], [1,2,3,4,5,6]]))
