# 💳 CreditWise Loan Approval Prediction

A supervised machine learning project that predicts whether a loan application should be **Approved or Rejected** based on an applicant's personal, financial, employment, and credit-related information.

The project compares three classification algorithms — **Logistic Regression, K-Nearest Neighbors (KNN), and Gaussian Naive Bayes** — and evaluates their performance before and after feature engineering.

---

## 📌 Project Overview

A financial company receives hundreds of loan applications from customers across different regions.

Traditionally, loan applications may require manual evaluation of:

* Income
* Employment information
* Credit score
* Existing loans
* Debt-to-income ratio
* Savings
* Collateral
* Loan amount
* Loan purpose
* Other applicant information

This manual process can be time-consuming and inconsistent.

This project uses machine learning to automatically predict whether a loan application should be **approved or rejected**, helping analyze historical application patterns and support the loan evaluation process.

---

## 🎯 Objective

The main objectives of this project are:

1. Explore and understand the loan application dataset.
2. Handle missing values.
3. Perform exploratory data analysis (EDA).
4. Encode categorical features.
5. Scale numerical features.
6. Train multiple classification models.
7. Evaluate the models using Accuracy, Precision, Recall, F1-score, and Confusion Matrix.
8. Perform feature engineering.
9. Compare model performance before and after feature engineering.
10. Identify the strongest-performing model based on the evaluation results.

---

## 📊 Dataset

The dataset contains **1,000 loan application records** with **20 original columns**.

Each row represents a loan applicant and contains personal, financial, employment, and credit-related information.

### Dataset Features

| Feature            | Description                    |
| ------------------ | ------------------------------ |
| Applicant_ID       | Unique applicant ID            |
| Applicant_Income   | Monthly income of applicant    |
| Coapplicant_Income | Monthly income of co-applicant |
| Employment_Status  | Employment type                |
| Age                | Applicant age                  |
| Marital_Status     | Marital status                 |
| Dependents         | Number of dependents           |
| Credit_Score       | Credit bureau score            |
| Existing_Loans     | Number of existing loans       |
| DTI_Ratio          | Debt-to-income ratio           |
| Savings            | Savings balance                |
| Collateral_Value   | Value of collateral provided   |
| Loan_Amount        | Requested loan amount          |
| Loan_Term          | Loan duration in months        |
| Loan_Purpose       | Purpose of the loan            |
| Property_Area      | Urban / Semiurban / Rural      |
| Education_Level    | Education level                |
| Gender             | Applicant gender               |
| Employer_Category  | Employer category              |
| Loan_Approved      | Target variable                |

### 🎯 Target Variable

`Loan_Approved`

* `1` → Approved
* `0` → Rejected

---

## 🔍 Exploratory Data Analysis

Several exploratory analyses were performed to understand the dataset and identify relationships between features and loan approval.

### EDA Performed

* Loan approval class distribution
* Gender distribution
* Education-level distribution
* Applicant income distribution
* Co-applicant income distribution
* Box plots for detecting potential outliers
* Credit score distribution by loan approval
* Correlation analysis
* Correlation heatmap

### 📌 Important Correlations

The strongest observed relationships with `Loan_Approved` included:

| Feature          | Correlation |
| ---------------- | ----------: |
| Credit_Score     |      0.4512 |
| DTI_Ratio        |     -0.4448 |
| Applicant_Income |      0.1198 |
| Loan_Amount      |     -0.1265 |

This showed that **Credit Score** and **DTI Ratio** had particularly strong relationships with the target compared with the other features in the dataset.

---

## 🧹 Data Preprocessing

### 1. Missing Value Analysis

The dataset initially contained **50 missing values in each column**.

The missing values were handled separately based on feature type.

### Numerical Features

Missing numerical values were replaced using the **mean**.

```text
SimpleImputer(strategy="mean")
```

### Categorical Features

Missing categorical values were replaced using the **most frequent value (mode)**.

```text
SimpleImputer(strategy="most_frequent")
```

After imputation, there were **no remaining missing values**.

---

## 🗑️ Feature Removal

`Applicant_ID` was removed because it is a unique identifier and does not provide meaningful information for predicting loan approval.

---

## 🔤 Feature Encoding

Categorical features were converted into numerical representations so that machine learning models could process them.

### Label Encoding

Label Encoding was applied to:

* `Education_Level`
* `Loan_Approved`

### One-Hot Encoding

One-Hot Encoding was applied to:

* `Employment_Status`
* `Marital_Status`
* `Loan_Purpose`
* `Property_Area`
* `Gender`
* `Employer_Category`

`drop="first"` was used to avoid redundant dummy variables.

After encoding, the dataset contained **28 columns**, including the target variable.

---

## 📊 Correlation Analysis

A correlation matrix was calculated to examine relationships between numerical features.

The correlation heatmap helped identify which features had stronger or weaker linear relationships with the loan approval target.

The analysis showed that:

* Higher `Credit_Score` had a positive relationship with loan approval.
* Higher `DTI_Ratio` had a negative relationship with loan approval.
* `Loan_Amount` also showed a negative relationship with loan approval.

---

## 🔄 Train-Test Split

The dataset was divided into training and testing sets using:

```text
Training Set → 80%
Testing Set  → 20%
random_state = 42
```

---

## ⚖️ Feature Scaling

Feature scaling was performed using **StandardScaler**.

The scaler was fitted only on the training data and then used to transform both the training and testing data.

This was especially useful for distance-based algorithms such as **KNN** and for ensuring that numerical features operate on comparable scales.

---

## 🤖 Machine Learning Models

Three classification algorithms were trained and evaluated.

### 1. Logistic Regression

Logistic Regression was used as a linear classification model for predicting whether a loan would be approved or rejected.

### 2. K-Nearest Neighbors (KNN)

KNN predicts the class of an applicant based on the classes of nearby observations.

The model was configured with:

```text
n_neighbors = 5
```

### 3. Gaussian Naive Bayes

Gaussian Naive Bayes was used as a probabilistic classification model assuming continuous features follow a Gaussian distribution.

---

# 📈 Initial Model Performance

Before feature engineering, the models produced the following results:

| Model                | Accuracy |  Precision | Recall | F1-Score |
| -------------------- | -------: | ---------: | -----: | -------: |
| Logistic Regression  |   86.50% |     78.33% | 77.05% |   77.69% |
| KNN                  |   76.00% |     62.75% | 52.46% |   57.14% |
| Gaussian Naive Bayes |   86.50% | **80.36%** | 73.77% |   76.92% |

### Initial Best Result

**Gaussian Naive Bayes** achieved the highest **Precision: 80.36%**.

---

# 🧪 Feature Engineering

Feature engineering was performed to create additional representations of important features.

Two squared features were created:

```text
DTI_Ratio_sq = DTI_Ratio²
Credit_Score_sq = Credit_Score²
```

The original:

* `DTI_Ratio`
* `Credit_Score`

were then removed from the feature set.

The data was subsequently split again and standardized using `StandardScaler`.

---

# 📈 Model Performance After Feature Engineering

| Model                |   Accuracy | Precision |     Recall |   F1-Score |
| -------------------- | ---------: | --------: | ---------: | ---------: |
| Logistic Regression  | **87.50%** |    79.03% | **80.33%** | **79.67%** |
| KNN                  |     75.50% |    62.00% |     50.82% |     55.86% |
| Gaussian Naive Bayes |     86.50% |    78.33% |     77.05% |     77.69% |

### 🏆 Best Overall Model

**Logistic Regression** performed the strongest overall after feature engineering.

It achieved:

* **Accuracy:** 87.50%
* **Precision:** 79.03%
* **Recall:** 80.33%
* **F1-Score:** 79.67%

Feature engineering improved Logistic Regression from **86.50% to 87.50% accuracy**.

---

## 🔀 Confusion Matrix Results

### Logistic Regression — After Feature Engineering

```text
[[126  13]
 [ 12  49]]
```

### KNN — After Feature Engineering

```text
[[120  19]
 [ 30  31]]
```

### Gaussian Naive Bayes — After Feature Engineering

```text
[[126  13]
 [ 14  47]]
```

These confusion matrices were used alongside Accuracy, Precision, Recall, and F1-score to evaluate the classification models.

---

## 🔄 Machine Learning Workflow

```text
Loan Dataset
     ↓
Data Exploration
     ↓
Missing Value Analysis
     ↓
Missing Value Imputation
     ↓
Exploratory Data Analysis
     ↓
Remove Applicant_ID
     ↓
Feature Encoding
     ↓
Correlation Analysis
     ↓
Train-Test Split
     ↓
Feature Scaling
     ↓
Train ML Models
     ↓
Model Evaluation
     ↓
Feature Engineering
     ↓
Retrain Models
     ↓
Compare Results
     ↓
Select Best Performing Model
```

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

### Scikit-learn Components

* `train_test_split`
* `SimpleImputer`
* `LabelEncoder`
* `OneHotEncoder`
* `StandardScaler`
* `LogisticRegression`
* `KNeighborsClassifier`
* `GaussianNB`
* `accuracy_score`
* `precision_score`
* `recall_score`
* `f1_score`
* `confusion_matrix`

---

## 📂 Project Structure

```text
loan-approval-classification/
│
├── loan-approval-classification.ipynb
├── README.md
└── dataset/
    └── loan_approval_data.csv
```

---

## 🚀 Key Learning Outcomes

Through this project, I explored:

* Supervised Machine Learning
* Binary Classification
* Missing Value Handling
* Mean and Mode Imputation
* Exploratory Data Analysis
* Label Encoding
* One-Hot Encoding
* Feature Scaling
* Correlation Analysis
* Logistic Regression
* K-Nearest Neighbors
* Gaussian Naive Bayes
* Model Evaluation
* Confusion Matrix
* Feature Engineering
* Model Comparison

---

## ⚠️ Important Note

The model results in this project are based on the provided dataset and experimental setup.

Although the model can identify patterns in historical loan applications, these results should **not be interpreted as proof that the system is unbiased or suitable for real-world automated loan decisions**.

Real-world financial decision systems require additional considerations such as larger and more representative datasets, fairness analysis, explainability, regulatory requirements, privacy, and careful validation before deployment.

---

## 👨‍💻 Author

**Parth Jaiswal**

B.Tech CSE — AI/ML & Robotics

