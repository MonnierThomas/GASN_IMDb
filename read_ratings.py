import csv

def read_ratings():
    with open('moviegalaxydataset.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        id_movie = []
        rating = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                id_movie.append(int(row[0][1:4]))
                if row[-1][1:3] == '?"':
                    rating.append(0.0)
                else:
                    rating.append(float(row[-1][1:4]))
    return [[id_movie[i], rating[i]] for i in range(len(rating))]