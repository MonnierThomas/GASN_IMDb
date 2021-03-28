import glob
import csv
from matplotlib import pyplot as plt

def plot(x):
    index = ['2-3', '3-4', '4-5', '5-6', '6-7', '-7-8', '8-9', '9-10']
    index_full = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '-7-8', '8-9', '9-10']
    count = []
    
    mean_relations = []
    mean_number = []
    mean_betweenness = []
    mean_eccentricity = []
    mean_closeness = []
    mean_degree = []
    
    std_relations = []
    std_number = []
    std_betweenness = []
    std_eccentricity = []
    std_closeness = []
    std_degree = []
    
    one_relations = []
    one_number = []
    one_betweenness = []
    one_eccentricity = []
    one_closeness = []
    one_degree = []
    
    two_relations = []
    two_number = []
    two_betweenness = []
    two_eccentricity = []
    two_closeness = []
    two_degree = []
    
    three_relations = []
    three_number = []
    three_betweenness = []
    three_eccentricity = []
    three_closeness = []
    three_degree = []
    for filename in glob.glob('descriptions_by_ratings/*.csv'): #assuming csv
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            a = False
            b = False
            c = False
            d = False
            e = False
            f = False
            for row in csv_reader:
                if row[0] == "mean":
                    mean_relations.append(float(row[2]))
                    mean_number.append(float(row[3]))
                    mean_betweenness.append(float(row[4]))
                    mean_eccentricity.append(float(row[5]))
                    mean_closeness.append(float(row[6]))
                    mean_degree.append(float(row[7]))
                    a = True
                elif row[0] == "count":
                    count.append(float(row[2]))
                    b = True
                elif row[0] == "std":
                    if row[2] != '':
                        std_relations.append(float(row[2]))
                        std_number.append(float(row[3]))
                        std_betweenness.append(float(row[4]))
                        std_eccentricity.append(float(row[5]))
                        std_closeness.append(float(row[6]))
                        std_degree.append(float(row[7]))
                        c = True
                    else:
                        std_relations.append(0.0)
                        std_number.append(0.0)
                        std_betweenness.append(0.0)
                        std_eccentricity.append(0.0)
                        std_closeness.append(0.0)
                        std_degree.append(0.0)
                        c = True
                elif row[0] == "25%":
                    one_relations.append(float(row[2]))
                    one_number.append(float(row[3]))
                    one_betweenness.append(float(row[4]))
                    one_eccentricity.append(float(row[5]))
                    one_closeness.append(float(row[6]))
                    one_degree.append(float(row[7]))
                    d = True
                elif row[0] == "50%":
                    two_relations.append(float(row[2]))
                    two_number.append(float(row[3]))
                    two_betweenness.append(float(row[4]))
                    two_eccentricity.append(float(row[5]))
                    two_closeness.append(float(row[6]))
                    two_degree.append(float(row[7]))
                    e = True
                elif row[0] == "75%":
                    three_relations.append(float(row[2]))
                    three_number.append(float(row[3]))
                    three_betweenness.append(float(row[4]))
                    three_eccentricity.append(float(row[5]))
                    three_closeness.append(float(row[6]))
                    three_degree.append(float(row[7]))
                    f = True
            # if s == False:
            #         mean_relations.append(0.0)
            #         mean_number.append(0.0)
            #         mean_betweenness.append(0.0)
            #         mean_eccentricity.append(0.0)
            #         mean_closeness.append(0.0)
            #         mean_degree.append(0.0)    
    if x == 0:
        return index_full, count
    elif x == 1:       
        return index, mean_betweenness, mean_closeness, mean_degree, mean_eccentricity, mean_number, mean_relations
    elif x == 2:
        return index, std_betweenness, std_closeness, std_degree, std_eccentricity, std_number, std_relations
    elif x == 3:
        return index, one_betweenness, one_closeness, one_degree, one_eccentricity, one_number, one_relations
    elif x == 4:
        return index, two_betweenness, two_closeness, two_degree, two_eccentricity, two_number, two_relations
    elif x == 5:
        return index, three_betweenness, three_closeness, three_degree, three_eccentricity, three_number, three_relations
#%% Plotting the mean by ratings
def plot_mean_relations():
    index, _, _, _, _, _, mean_relations = plot(1)
    plt.plot(index, mean_relations, "d", color='black')
    plt.title("Number of relations by ratings")
    plt.savefig('relations_by_ratings.jpg')
    
def plot_mean_characters():
    index, _, _, _, _, mean_number, _ = plot(1)
    plt.plot(index, mean_number, "d", color='red')
    plt.title("Number of characters by ratings")
    plt.savefig('characters_by_ratings.jpg')
    
def plot_mean_betweenness():
    index, mean_betweenness, _, _, _, _, _ = plot(1)
    plt.plot(index, mean_betweenness, "d", color='cyan')
    plt.title("Betweenness centrality by ratings")
    plt.savefig('betweenness_by_ratings.jpg')
    
def plot_mean_eccentricity():
    index, _, _, _, mean_eccentricity, _, _ = plot(1)
    plt.plot(index, mean_eccentricity, "d", color='orange')
    plt.title("Eccentricity by ratings")
    plt.savefig('eccentricity_by_ratings.jpg')
    
def plot_mean_closeness():
    index, _, mean_closeness, _, _, _, _ = plot(1)
    plt.plot(index, mean_closeness, "d", color='green')
    plt.title("Closeness centrality by ratings")
    plt.savefig('closeness_by_ratings.jpg')
    
def plot_mean_degree():
    index, _, _, mean_degree, _, _, _ = plot()
    plt.plot(index, mean_degree, "d", color='purple')
    plt.title("Degrees by ratings")
    plt.savefig('degree_by_ratings.jpg')
    
#%% Count number movies by ratings
def plot_count():
    index, count = plot(0)
    plt.plot(index, count, "d", color='red')
    plt.title('Number of movies by ratings')
    plt.savefig('number_movies_by_ratings.jpg')

#%% Plotting the standard deviation by ratings
def plot_std_relations():
    index, _, _, _, _, _, std_relations = plot(2)
    plt.plot(index, std_relations, "d", color='black')
    plt.title("Standard deviation of the number relations by ratings")
    plt.savefig('std_relations_by_ratings.jpg')
    
def plot_std_characters():
    index, _, _, _, _, std_number, _ = plot(2)
    plt.plot(index, std_number, "d", color='red')
    plt.title("Standard deviation of the number of characters by ratings")
    plt.savefig('std_characters_by_ratings.jpg')
    
def plot_std_betweenness():
    index, std_betweenness, _, _, _, _, _ = plot(2)
    plt.plot(index, std_betweenness, "d", color='cyan')
    plt.title("Standard deviation of the betweenness centrality by ratings")
    plt.savefig('std_betweenness_by_ratings.jpg')
    
def plot_std_eccentricity():
    index, _, _, _, std_eccentricity, _, _ = plot(2)
    plt.plot(index, std_eccentricity, "d", color='orange')
    plt.title("Standard deviation of the eccentricity by ratings")
    plt.savefig('std_eccentricity_by_ratings.jpg')
    
def plot_std_closeness():
    index, _, std_closeness, _, _, _, _ = plot(2)
    plt.plot(index, std_closeness, "d", color='green')
    plt.title("Standard deviation of the closeness centrality by ratings")
    plt.savefig('std_closeness_by_ratings.jpg')
    
def plot_std_degree():
    index, _, _, std_degree, _, _, _ = plot(2)
    plt.plot(index, std_degree, "d", color='purple')
    plt.title("Standard deviation of the degrees by ratings")
    plt.savefig('std_degree_by_ratings.jpg')
#%%
plot_mean_relations()

#%% 
plot_mean_characters()

#%%
plot_mean_betweenness()

#%%
plot_mean_eccentricity()

#%%
plot_mean_closeness()

#%%
plot_mean_degree()

#%%
plot_count()

#%%
plot_std_relations()

#%%
plot_std_characters()

#%%
plot_std_betweenness()

#%%
plot_std_eccentricity()

#%%
plot_std_closeness()

#%%
plot_std_degree()











