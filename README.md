
# CardioVascular Detection System

## Motivation

Heart disease encompasses a range of conditions that impact the heart, including blood vessel diseases, heart attacks, strokes, heart failure, arrhythmias, and more. While "heart disease" is often used interchangeably with "cardiovascular disease," the latter specifically refers to conditions leading to heart attacks, chest pain, or strokes.

Early detection and prediction of cardiovascular disease are critical for individuals at high risk, allowing for timely intervention and management to prevent sudden heart failure.

### Key Facts from WHO:
- 17.9 million people die from cardiovascular diseases each year, accounting for 32% of all global deaths.
- Heart attacks and strokes constitute 85% of these fatalities.
- Over 75% of cardiovascular disease deaths occur in low- and middle-income countries.
- Early detection and treatment through counselling and medication are essential.

## Dataset

We utilized the [CardioVascular Disease dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) from Kaggle. This dataset includes 13 features:
- Age
- Height
- Weight
- Gender
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Cholesterol
- Glucose
- Smoking
- Alcohol Intake
- Physical Activity
- Presence Of Cardiovascular Disease

## Methodology

Link to google collab where we have carried out EDA and Model training : [GOOGLE COLLAB](https://colab.research.google.com/drive/1INnsy09sq5fadERpZbL2Uh7r-AJZDj96#scrollTo=WtomZnepdmgd)

### Step 1: Data Exploration and Preprocessing
We performed Exploratory Data Analysis (EDA) to understand and clean the dataset. This included normalization and handling missing values to prepare the data for training.

### Step 2: Model Training and Evaluation
We evaluated multiple machine learning models:
- Logistic Regression
- K-Nearest Neighbors Classifier
- Decision Tree Classifier
- Random Forest Classifier

Additionally, we implemented various ensemble strategies:
- Bagging
- Boosting (AdaBoost, XGBoost)
- Stacking

#### Validation Accuracy Scores:
```json
[
 {'LogisticRegression': 0.7262079352771299},
 {'KNeighborsClassifier': 0.6930779278503095},
 {'DecisionTreeClassifier': 0.6363570260259298},
 {'RandomForest': 0.6834661211426618},
 {'bagging LogisticRegression': 0.7260800330066066},
 {'bagging (default)': 0.6745121290263117},
 {'AdaBoosting (LogisticRegression)': 0.7244170981168467},
 {'XgBoosting (Logistic Regression)': 0.7330422263497177},
 {'Stacking (LR and RF)': 0.6838132815860269},
 {'bagging LogisticRegression Tuned': 0.7259703838837995},
 {'Stacking (LR and RF Tuned)': 0.7320555361870491}
]
```

#### Testing Accuracy Scores:
```json
[
 {'LogisticRegression': 0.7290600789358281},
 {'RandomForest': 0.6811869609706184},
 {'Bagging (LogisticRegression)': 0.6811869609706184},
 {'Bagging (Default)': 0.6811869609706184},
 {'XgBoosting (Logistic Regression)': 0.7361496857184622},
 {'Stacking (LR and RF)': 0.40885835404180676},
 {'Bagging (LogisticRegression Tuned)': 0.6811869609706184},
 {'Stacking (LR and RF Tuned)': 0.4932027481362374}
]
```

### Step 3: Model Selection
Based on the evaluation, XGBoost with Logistic Regression yielded the best results. We trained our final model using this configuration and saved it as a pickle file for deployment.

### Step 4: Deployment
We created a Flask application that accepts input data from a form, processes it through the trained model, and predicts the presence of cardiovascular disease. This application was deployed on an EC2 instance using Amazon Web Services (AWS). Files were uploaded via WinSCP, and the Flask app was run on the EC2 instance using PuTTY.

## Conclusion
The project successfully demonstrates the use of machine learning algorithms for early detection of cardiovascular disease. The XGBoost model provided the highest accuracy, indicating its potential for real-world applications in healthcare.

## GLIMPSES OF OUR PROJECT


![image](https://github.com/vrajpatel1411/Research-Methodology_project/assets/56471759/3506caf4-73a0-40ae-9617-47fcd013f179)

![image](https://github.com/vrajpatel1411/Research-Methodology_project/assets/56471759/e8519362-f166-4b6c-afcf-1cee8b99099e)


