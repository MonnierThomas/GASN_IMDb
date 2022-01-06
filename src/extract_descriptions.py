#%% Extract all the features from all files

from features_using_networkx import get_features

features = get_features()

#%% Extract all ratings

from read_ratings import read_ratings

ratings = read_ratings()

#%% Deleting features whose id has no rating

id_ratings = []
for i in ratings:
    id_ratings.append(i[0])
    
id_features = []
for j in features:
    id_features.append(j[0])

for k in features:
    if k[0] not in id_ratings:
        features.remove(k)

for l in ratings:
    if l[0] not in id_features:
        ratings.remove(l)

#We have to do it twice
id_ratings = []
for i in ratings:
    id_ratings.append(i[0])
    
id_features = []
for j in features:
    id_features.append(j[0])

for k in features:
    if k[0] not in id_ratings:
        features.remove(k)

for l in ratings:
    if l[0] not in id_features:
        ratings.remove(l)

#%% Mean of betweeness, centrality, eccentricity and degree

def mean(liste):
    return sum(liste)/len(liste)

new_features = []
for i, y in enumerate(features):
    new_features.append([])
    new_features[i].append(y[0])
    new_features[i].append(y[1])
    new_features[i].append(y[2])
    new_features[i].append(mean(y[3]))
    new_features[i].append(mean(y[4]))
    new_features[i].append(mean(y[5]))
    new_features[i].append(mean(y[6]))

#%% Ranged by ratings

first_range = []
second_range = []
third_range = []
fourth_range = []
fifth_range = []
sixth_range = []
seventh_range = []
eigth_range = []
ninth_range= []
tenth_range = []

def ranged(features):
    for i in range(len(features)):
        if 0.0 < ratings[i][1] < 1.0:
            first_range.append(features[i])
        elif 1.0 < ratings[i][1] < 2.0:
            second_range.append(features[i])
        elif 2.0 < ratings[i][1] < 3.0:
            third_range.append(features[i])
        elif 3.0 < ratings[i][1] < 4.0:
            fourth_range.append(features[i])
        elif 4.0 < ratings[i][1] < 5.0:
            fifth_range.append(features[i])
        elif 5.0 < ratings[i][1] < 6.0:
            sixth_range.append(features[i])
        elif 6.0 < ratings[i][1] < 7.0:
            seventh_range.append(features[i])
        elif 7.0 < ratings[i][1] < 8.0:
            eigth_range.append(features[i])
        elif 8.0 < ratings[i][1] < 9.0:
            ninth_range.append(features[i])
        else:
            tenth_range.append(features[i])
        
ranged(new_features)
#%% Showing pandas
    
import pandas as pd
import csv

one = pd.DataFrame(first_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
two = pd.DataFrame(second_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
three = pd.DataFrame(third_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
four = pd.DataFrame(fourth_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
five = pd.DataFrame(fifth_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
six = pd.DataFrame(sixth_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
seven = pd.DataFrame(seventh_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
eight = pd.DataFrame(eigth_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
nine = pd.DataFrame(ninth_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
ten = pd.DataFrame(tenth_range, columns=["id", "relationships", "number of characters", "betweenness centrality", "eccentricity", "closeness centrality", "degree"])
    
print("Movies with ratings from 0 to 1: ")
print(one.describe())
print(" ")
print("Movies with ratings from 1 to 2: ")
print(two.describe())
print(" ")
print("Movies with ratings from 2 to 3: ")
print(three.describe())
print(" ")
print("Movies with ratings from 3 to 4: ")
print(four.describe())
print(" ")
print("Movies with ratings from 4 to 5: ")
print(five.describe())
print(" ")
print("Movies with ratings from 5 to 6: ")
print(six.describe())
print(" ")
print("Movies with ratings from 6 to 7: ")
print(seven.describe())
print(" ")
print("Movies with ratings from 7 to 8: ")
print(eight.describe())
print(" ")
print("Movies with ratings from 8 to 9: ")
print(nine.describe())
print(" ")
print("Movies with ratings from 9 to 10: ")
print(ten.describe())
print(" ")

#%% Saving to csv the description of the pandas

one_describe = one.describe().to_csv('0-1.csv')
two_describe = two.describe().to_csv('1-2.csv')
three_describe = three.describe().to_csv('2-3.csv')
four_describe = four.describe().to_csv('3-4.csv')
five_describe = five.describe().to_csv('4-5.csv')
six_describe = six.describe().to_csv('5-6.csv')
seven_describe = seven.describe().to_csv('6-7.csv')
eight_describe = eight.describe().to_csv('7-8.csv')
nine_describe = nine.describe().to_csv('8-9.csv')
ten_describe = ten.describe().to_csv('9-10.csv')

    
    
    
    
    
    
    
    
    
    

