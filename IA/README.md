# Soil recognition and classification

As part of the AI module covered in this class, this project integrates both the technical aspects learnt about ML and the methodological approach we've been following to address a classification task.

Ramona Najera, A01423596

## Introduction

### Initial Dataset

🗃 [Landstat Satellite](https://archive.ics.uci.edu/dataset/146/statlog+landsat+satellite) (Climate & environment) <br>
Srinivasan, A. (1993). Statlog (Landsat Satellite) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55887.

- `4435 training` instances 🦾 <br>
- `2000 testing` instances 📊

### Task: Classification

- `36 numerical attributes` (4 spectral bands x 9 pixels, ranging between 0 and 255)
- `7 class labels` (starting with #1, with no data for #6)

### Feature scaling and preprocessing

1. For each record, `separate` class label from pixels info
2. Class numbers will go from 0 to 5 to `remove` unused ones
3. Pixels will be `normalized` (going from 0 to 1)

## State of the art

### 1. A comparative study of soil classification ML models

ML has propelled development in multiple disciplines, one of them being Geotechnical engineering (a branch of Civil engineering). In particular, soil classification problems have proven to be solved faster and more accurately when using AI, hence the focus on comparing the perfomance among different models to select the most appropriate one.

This paper analyzes the models below:

1. `Multinomial Logistic Regression` (MLR)
2. `Gaussian Naive Bayes` (GNB)
3. `Extreme Gradient Boosting` (XGBoost)
4. `Random Forest`
5. Artificial Neural Network-`Multilayer Perceptron` (ANN-MLP)

And states that future work on this area could include feature selection, data preprocessing and some deep learning techniques to improve results and enhance performance.

#### Metrics

To compare and evaluate the models, following metrics were used:

- `Balanced accuracy` (overall correctness of a model) <br>
  Misleading with imbalanced datasets <br><br>
- `Precision` (accuracy of positive predictions) <br>
  How good is the model avoiding false positives <br><br>
- `Recall` (how well the model identifies positive instances) <br>
  How good is the model avoiding false negatives <br><br>
- `F1-score` (represents precision and recall in a single value) <br><br>
- `Matthews Correlation Coefficient` (considers all elements of the confusion matrix) <br>
  Helpful with imbalanced datasets

#### ANN-MLP model

> Identify complex relations

This model with densely connected layers used ReLU activation functions in two hidden layers and softmax in the output layer, resulting in high scores regarding precision, recall and consequently, F1 score, presenting a balanced accuracy of around 90%.

#### MLR model

> Probability of belonging to each class

### References

1. Obasi, S. N. N., Pemberton, J., & Awe, O. O. (2024). _A comparative study of soil classification machine learning models for construction management_. International Journal of Construction Management, 25(5), 584–593. https://doi.org/10.1080/15623599.2024.2341500

## Model analysis

https://www.youtube.com/watch?v=gkNccYwtAbU <br>
https://www.evidentlyai.com/classification-metrics/multi-class-metrics

### 1st model:
