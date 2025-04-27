# Soil recognition and classification

As part of the AI module covered in this class, this project integrates both the technical aspects learnt about ML and the methodological approach we've been following to address a classification task.

April 27th, 2025 <br>
Ramona Najera, A01423596

## Introduction

### Initial Dataset

🗃 [Landstat Satellite](https://archive.ics.uci.edu/dataset/146/statlog+landsat+satellite) (Climate & environment) <br>
Srinivasan, A. (1993). Statlog (Landsat Satellite) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55887.

- `4435 training` instances 🦾 <br>
- `2000 testing` instances 📊

### Task: Classification

#### Variables

- `36 numerical attributes` (4 spectral bands x 9 pixels, ranging between 0 and 255)
- `7 class labels` (starting with #1, with no data for #6)

#### Objectives

- Create a **supervised ML model** that identifies types of soils <br>
- **Enhance** the model **with DL techniques**, such as recognizing input's features before starting the classification <br>
- **Sustain each** model **proposal** and metric selection **with reliable articles** and other sources

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

> Identifies complex relations

This model with densely connected layers used ReLU activation functions in two hidden layers and softmax in the output layer, resulting in high scores regarding precision, recall and consequently, F1 score, presenting a balanced accuracy of around 90%.

#### Reference

Obasi, S. N. N., Pemberton, J., & Awe, O. O. (2024). _A comparative study of soil classification machine learning models for construction management_. International Journal of Construction Management, 25(5), 584–593. https://doi.org/10.1080/15623599.2024.2341500

### 2. Convolutional Neural Networks based classifications of soil images

The agriculture sector has been vastly benefited by ML image processing when it comes to detecting anomalies, installing intelligent systems, tracking cattle and using smart-farming techniques. This paper compares the performance of a CNN model vs six different DCNN models, using confusion matrix and K-fold technique to evaluate their performance.

#### CNN model

> Feature selection

This model consists of the following layers:

- `Convolution layers` (collection of filters/kernels) <br><br>
- `Activation layers` (transforms inputs to outputs of a certain range) <br>
  They used ReLU as their activation function <br><br>
- `Batch normalization layers` (improves network stability) <br>
  Performs normalization and standardization <br><br>
- `Pooling layers` (reduces network parameters) <br>
  Average pooling was used <br><br>
- `Fully connected layers` (classifier layer) 

#### DCNN models

> Pretrained models

Due to their excellent performance, following models were analyzed:

- Rsnet152V2
- VGG-16 and VGG-19
- Inception-ResNetV2
- Xception
- DenseNet201

CNN model achieved a 99.86% accuracy that decreased to 97.68% during validation, while the DCNN's models accuracies ranged between 97.58% and 99.15%, so the CNN model ended up outperforming these proposals.

#### Reference

Lanjewar, M.G., Gurav, O.L. _Convolutional Neural Networks based classifications of soil images_. Multimed Tools Appl 81, 10313–10336 (2022). https://doi.org/10.1007/s11042-022-12200-y

## Model analysis

### Architecture and hyperparameters

**Artificial Neural Network** proposal of a **Multilayer Perceptron model** <br>
As suggested by _Obasi, S. N. N., Pemberton, J., & Awe, O. O. (2024)_, with the following components:

- 1 `Flatten` layer
- 1 `Dense` layer with _128 nodes_ and _ReLu activation_
- 1 `Dense` layer with _67 nodes_ and _ReLu activation_
- 1 `Dense` layer with _6 nodes_ and _softmax activation_ (for multiclass classification)

Compilation was done using 
- `adam` optimizer (variant of gradient descent)
- `sparse_categorical_crossentropy` (for error presentation)
- `accuracy` (to evaluate model's behavior)

The model was trained with `50 epochs`

### Enhancements

**Convolutional Neural Network** <br>
As suggested by _Lanjewar, M.G., Gurav, O.L. (2022)_, with the following changes added before the base model configuration:

- 1 `Conv2D` layer with _4 filters_ of _size (1,3)_, using _ReLu activation_
- 1 `Conv2D` layer with _2 filters_ of _size (1,2)_

### Results

| Model     | Train acc | Test acc | Precision | Recall | F1 Score | Matthews Correlation Coeff |
|-----------|-----------|----------|-----------|--------|----------|----------------------------|
| ANN - MLP | 86.32%    | 85.28%   | 81.70%    | 81.36% | 81.03%   | 81.97%                     |
| CNN       | 89.56%    | 90%      | 88.82%    | 88.31% | 88.50%   | 87.73%                     |

- Both models had a training and a test accuracy separated by 1%
- Enhancements made the base model increase its perfomance by, at least, 5% in all the metrics
- Precision and recall were almost the same, being slightly better at avoiding false positives than false negatives
- Performance is lower when analyzing the models with MCC, but there is not a huge gap compared to the other the metrics, so class imbalance proved not to be a crucial factor

### Discussion and conclusions

It would be interesting to work on class imbalance and see how much does the performance change per metric. Additionally, none of the pretrained alternatives could be applied because the input shape did not reach the minimum size for being processed with those models and, although that seems reasonable beacuse smaller images take less resources to be analyzed, I would like witness the advantages these tools offer.

However, a couple of convolution layers were enough for the base model's accuracy to increase significantly. In fact, adding batch normalization layers, pooling layers or increasing the number of intermediate neurons decreased the model's performance (because it implied adding more complexity than needed to achieve the specified task).

Small changes proved to make huge differences and this work contains a solid basis to increase the scope of the project from an introduction to ML to a deeper understanding of other common techniques and arquitectures used within the industry.

### References

1. Huddar, M. (2023) _Confusion Matrix for Multiclass Classification Precision Recall Weighted F1 Score by Mahesh Huddar_. YouTube. https://www.youtube.com/watch?v=gkNccYwtAbU

2. Evidently AI Team (2025) _Accuracy, precision, and recall in multi-class classification_. Evidently AI - Open-Source ML Monitoring and Observability. https://www.evidentlyai.com/classification-metrics/multi-class-metrics