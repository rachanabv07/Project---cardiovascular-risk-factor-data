
# Project : Cardiovascular Risk Factor Data

## Dataset
- DataSet is taken from Kaggle - https://www.kaggle.com/datasets/mamta1999/cardiovascular-risk-data
- DataSet provided information on over 4,000 patients and included 15 attributes, each representing a potential risk factor for CHD. These attributes included demographic, behavioral, and medical risk factors.

## Variables Description
### Demographic:
- Sex: male or female ("M" or "F") Age: Age of the patient (Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
- Education: The level of education of the patient (categorical values - 1,2,3,4)
###  Behavioral:
- is_smoking: whether or not the patient is a current smoker ("YES" or "NO")
 - Cigs Per Day: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes, even half a cigarette.)
###  Medical (history):
- BP Meds: whether or not the patient was on blood pressure medication (Nominal)
- Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)
- Prevalent Hyp: whether or not the patient was hypertensive (Nominal)
- Diabetes: whether or not the patient had diabetes (Nominal)
###  Medical (current):
- Tot Chol: total cholesterol level (Continuous)
- Sys BP: systolic blood pressure (Continuous)
- Dia BP: diastolic blood pressure (Continuous)
- BMI: Body Mass Index (Continuous)
- Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)
- Glucose: glucose level (Continuous)
###  Predict variable (desired target):
- 10-year risk of coronary heart disease CHD(binary: “1”, means “Yes”, “0” means “No”)

## SKills

- Python - 3.11
- Pandas
- Numpy
- Matplotlib
- scikit-learn
- Treating missing values in dataset
- Data visualization
- Data Preprocessing
- Data Modeling
- Framework - Flask
- Frontend - HTML, CSS




## Installation
```bash
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix, auc, roc_curve
from flask import Flask, render_template, request
import pickle
```
## Deployment
![Deployment Image 1](https://github.com/rachanabv07/Project---cardiovascular-risk-factor-data/raw/main/images/1.png)
![Deployment Image 2](https://github.com/rachanabv07/Project---cardiovascular-risk-factor-data/raw/main/images/2.png)
![Deployment Image 3](https://github.com/rachanabv07/Project---cardiovascular-risk-factor-data/raw/main/images/3.png)

