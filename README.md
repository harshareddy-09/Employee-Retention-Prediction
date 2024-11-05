# Employee Retention Prediction

## Project Overview
This project aims to predict employee retention using machine learning models. Based on various factors like satisfaction level, last evaluation, number of projects, average monthly hours, time spent at the company, and salary, the model predicts whether an employee will stay with or leave the company. After evaluating different models, the **RandomForestClassifier** was chosen for its high accuracy.

## Dataset
The dataset used in this project was downloaded from [Kaggle](https://www.kaggle.com/), containing various features that may influence employee retention.

### Features in the Dataset
- `satisfaction_level`: Employee's job satisfaction level.
- `last_evaluation`: Last performance evaluation score.
- `number_of_projects`: Number of projects the employee has worked on.
- `average_monthly_hours`: Average monthly hours worked by the employee.
- `time_spend_company`: Years spent by the employee in the company.
- `salary`: Employee's salary level, categorized as low, medium, or high.

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis (EDA) was performed to understand the data distribution and relationships between variables. Key steps in the EDA process included:
1. **Feature Engineering**: Transforming features to improve model accuracy.
2. **Feature Selection**: Selecting features that contribute most to the predictive power of the model.

## Model Selection and Performance
Several machine learning models were trained and evaluated using **Cross-Validation**. The accuracy of each model was as follows:
- **Logistic Regression**: 77%
- **Gaussian Naive Bayes**: 78%
- **Decision Tree Classifier**: 97.3%
- **Random Forest Classifier**: 98.6%

Based on these results, **RandomForestClassifier** was selected as the final model due to its high accuracy of **98.6%**.

## Predicting New Samples
The **RandomForestClassifier** model can be used to predict employee retention for new samples based on the selected features. Simply provide new sample data in the required format to obtain predictions.

## Conclusion
This project successfully implemented an employee retention prediction model with a high accuracy of 98.6% using the **RandomForestClassifier**. This model can assist HR departments in identifying employees who might be at risk of leaving, allowing proactive strategies for employee retention.



