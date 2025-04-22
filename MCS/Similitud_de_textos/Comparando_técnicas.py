import os
import re
import csv
import math
import string
import numpy as np
from numpy.linalg import norm

def readText(filename):
    with open(f'./texts/{filename}', 'r') as file:
        data = file.read().replace('\n', '').lower()
        data = data.translate(str.maketrans('', '', string.punctuation))
        return data
    return " "

def getInterval(cosine):
    if cosine < 0.45:
        return "low" # [0 a 0.45)
    elif cosine < 0.85:
        return "moderate" # [0.45 a 0.85)
    else:
        return "high" # [0.85 a 1.00]

print("ACTIVIDAD: Comparación entre técnicas de semejanza\nRamona Najera, A01423596")

cols = ["texto_original", "texto_similar", "grado_similitud", "BoW_cosine", "TfIDF_cosine", "Markov_cosine", "BoW_acc", "TfIDF_acc", "Markov_acc"]
original = "original.txt"
originalTxt = readText(original)

with open('./out/compare_a01423596.csv', 'w', newline='') as output:
    file = csv.writer(output)
    file.writerow(cols)

    qs1 = originalTxt.split(" ")
    BoW_score = 0
    TFIDF_score = 0
    Markov_score = 0
    
    for text in os.listdir("./texts"):
        if text != original:
            similitud = text.split("_")[0]
            compareTxt = readText(text)

            bag = set()
            qs2 = compareTxt.split(" ")

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

            BoW_acc = getInterval(BoW_cosine)
            BoW_score += (BoW_acc == similitud)

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

            TfIDF_acc = getInterval(TfIDF_cosine)
            TFIDF_score += (TfIDF_acc == similitud)

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

            Markov_acc = getInterval(Markov_cosine)
            Markov_score += (Markov_acc == similitud)

            file.writerow([original, text, similitud, BoW_cosine, TfIDF_cosine, Markov_cosine, BoW_acc, TfIDF_acc, Markov_acc])

print("BoW score", BoW_score)
print("TFIDF score", TFIDF_score)
print("Markov score", Markov_score)
