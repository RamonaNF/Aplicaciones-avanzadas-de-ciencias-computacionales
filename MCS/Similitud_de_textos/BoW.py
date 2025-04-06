import csv
import numpy as np
from numpy.linalg import norm

print("ACTIVIDAD: Similitud en textos mediante BoW\nRamona Najera, A01423596")

cols = ["question1", "question2", "cosine", "q1_vector", "q2_vector"]

with open("./questions.csv", 'r') as questions, open('./out/BoW_a01423596.csv', 'w', newline='') as BoW:
    data = csv.reader(questions, delimiter=",")
    file = csv.writer(BoW)

    next(data) # Skip reading column names
    file.writerow(cols)

    for line in data:
        q1 = line[3].lower()
        q2 = line[4].lower()

        bag = set()
        qs1 = q1.split(" ")
        qs2 = q2.split(" ")

        # Unique words in both texts
        for word in qs1:
            bag.add(word)
        
        for word in qs2:
            bag.add(word)

        # Vectorize text based on frequencies
        freq1 = []
        freq2 = []
        for word in bag:
            freq1.append(qs1.count(word))
            freq2.append(qs2.count(word))

        cosine = np.dot(freq1,freq2)/(norm(freq1)*norm(freq2))

        file.writerow([q1, q2, cosine, freq1, freq2])

"""
import numpy as np
import pandas as pd
from numpy.linalg import norm

print("ACTIVIDAD: Similitud en textos mediante BoW\nRamona Najera, A01423596")

# Read data and stay with selected columns
questions = pd.read_csv('questions.csv')
data = questions[["question1", "question2"]]

data["cosine"] = np.nan
data["q1_vector"] = None
data["q2_vector"] = None

#print(data.head())

for i in range(len(data)):
    q1 = data["question1"][i].lower()
    q2 = data["question2"][i].lower()

    data["question1"][i] = q1
    data["question2"][i] = q2

    #print("Q1:",q1)
    #print("Q2:",q2)

    bag = set()
    qs1 = q1.split(" ")
    qs2 = q2.split(" ")

    # Unique words in both texts
    for word in qs1:
        bag.add(word)
    
    for word in qs2:
        bag.add(word)

    #print("Bag",bag)

    # Vectorize text based on frequencies
    freq1 = []
    freq2 = []
    for word in bag:
        freq1.append(qs1.count(word))
        freq2.append(qs2.count(word))

    #print("V1",freq1)
    #print("V2",freq2)

    data["q1_vector"][i] = "["+"".join(str(freq)+" " for freq in freq1)+"]"
    data["q2_vector"][i] = "["+"".join(str(freq)+" " for freq in freq2)+"]"

    cosine = np.dot(freq1,freq2)/(norm(freq1)*norm(freq2))
    #print("Cosine",cosine)
    data["cosine"][i] = cosine

data.to_csv('BoW_output_a01423596.csv')
"""