import re
import csv
import math
import numpy as np
from numpy.linalg import norm

print("ACTIVIDAD: Similitud en textos mediante Tf-IDF y Cadenas de Markov\nRamona Najera, A01423596")

cols = ["question1", "question2", "BoW cosine", "q1_vec_BoW", "q2_vec_BoW", "TfIDF cosine", "q1_vec_TfIDF", "q2_vec_TfIDF", "Markov cosine", "q1_vec_Markov", "q2_vec_Markov"]

max_lines = 10000
with open("./questions.csv", 'r') as questions, open('./out/TfIDF_Markov_cut_a01423596.csv', 'w', newline='') as TfIDF_Markov:
    data = csv.reader(questions, delimiter=",")
    file = csv.writer(TfIDF_Markov)

    next(data) # Skip reading column names
    file.writerow(cols) # Write column names

    for line in data:
        # Ignore empty records
        if(not line[3] or not line[4]):
            continue
        elif max_lines < 1:
            break
        max_lines = max_lines - 1
        
        # Procesar el texto en minúscula
        q1 = line[3].lower()
        q2 = line[4].lower()

        bag = set()
        qs1 = q1.split(" ")
        qs2 = q2.split(" ")

        # BoW: Unique words in both texts
        for word in qs1:
            bag.add(word)
        
        for word in qs2:
            bag.add(word)
        
        # BoW: Vectorize text based on frequencies
        freq1 = []
        freq2 = []
        
        for word in bag:
            freq1.append(qs1.count(word))
            freq2.append(qs2.count(word))

        BoW_cosine = 0
        norm1 = norm(freq1)
        norm2 = norm(freq2)
        
        if norm1 and norm2:
            BoW_cosine = np.dot(freq1,freq2)/(norm1*norm2)

        # Tf-IDF: Compute term frequency and IDF
        TfIDF1 = []
        TfIDF2 = []

        for i in range(len(bag)):
            appear = 1

            Tf1 = freq1[i] / len(qs1)
            Tf2 = freq2[i] / len(qs2)

            if freq1[i]:
                appear = appear + 1
            if freq2[i]:
                appear = appear + 1

            IDF = math.log(2/appear) + 1

            TfIDF1.append(Tf1 * IDF)
            TfIDF2.append(Tf2 * IDF)

        TfIDF_cosine = 0
        norm1 = norm(TfIDF1)
        norm2 = norm(TfIDF2)

        if norm1 and norm2:
            TfIDF_cosine = np.dot(TfIDF1,TfIDF2)/(norm1*norm2)

        # Markov: generar matriz de probabilidad
        bag = sorted(list(bag))
        
        prob1 = [[0 for col in range(len(bag))] for row in range(len(bag))]
        prob2 = [[0 for col in range(len(bag))] for row in range(len(bag))]
        
        cnt1 = [0 for elem in range(len(bag))]
        cnt2 = [0 for elem in range(len(bag))]

        # Compute paths per word and total apparitions
        for idx in range(len(qs1) - 1):
            prob1[bag.index(qs1[idx])][bag.index(qs1[idx + 1])] += 1
            cnt1[bag.index(qs1[idx])] += 1
        
        for idx in range(len(qs2) - 1):
            prob2[bag.index(qs2[idx])][bag.index(qs2[idx + 1])] += 1
            cnt2[bag.index(qs2[idx])] += 1

        # Compute probabilities and flatten matrix
        flat1 = []
        flat2 = []

        for i in range(len(bag)):
            for j in range(len(bag)):
                #prob1[i][j] = prob1[i][j] / cnt1[i]
                #prob2[i][j] = prob2[i][j] / cnt2[i]

                # Don't divide by zero
                if cnt1[i]:
                    flat1.append(prob1[i][j] / cnt1[i])
                else:
                    flat1.append(0)
                
                if cnt2[i]:
                    flat2.append(prob2[i][j] / cnt2[i])
                else:
                    flat2.append(0)

        Markov_cosine = 0
        norm1 = norm(flat1)
        norm2 = norm(flat2)

        if norm1 and norm2: 
            Markov_cosine = np.dot(flat1,flat2)/(norm1*norm2)

        file.writerow([q1, q2, BoW_cosine, freq1, freq2, TfIDF_cosine, TfIDF1, TfIDF2, Markov_cosine, flat1, flat2])
