# Loan_Default_Risk_Prediction

To build a predictive model on loan default risk that can improve overall lending operations.

## Introduction
In the world of finance, predicting loan default risk is a crucial task for lenders to minimize losses and make informed decisions. In this project, a predictive model  was developed using machine learning algorithms to identify loan default risk.  A dataset that combines demographic and performance data of customers was utilized , with the target variable being the good_bad_flag, indicating whether a loan was settled on time or not.

## Data Description
The dataset consists of two parts: Demographics and Performance. The Demographics dataset contains information about customers, including their demographic characteristics, while the Performance dataset contains information about loan performance. The two datasets were merged together based on the customerid column to create a comprehensive dataset.

## Tool Used
•  Python: Data cleaning, EDA, Modeling
•  Power BI: Dashboarding & Insights
•  Libraries: Pandas, Scikit-learn, XGBoost, Matplotlib

## Data Preprocessing
The following steps were taken to preprocess the data:
•  Data Cleaning: Both datasets were cleaned separately to handle missing values, outliers, and inconsistencies.
•  Exploratory Data Analysis:  The target distribution was imbalanced, with a higher number of good loans than bad loans. The numerical columns were skewed and contained outliers, which were treated using log transformation.
•  Feature Engineering: Several feature engineering techniques were applied to extract relevant information from the data, including:
    - Age Calculation: The age column was calculated based on the birthdate column.
    - Age Category: The age_category column was created to categorize customers into different age groups.
    - Interest Calculation: The interest column was calculated based on the loan_amount and total_due columns.
    - Employment Risk: The employment_risk column was created to assess the risk associated with the customer's employment status.

## Model Building
The following steps were taken to build the model:
•  Data Split: The dataset was split into training and testing sets using a 90:10 ratio.
•  SMOTE Oversampling: The training data was oversampled using SMOTE to handle class imbalance.
•  Model Selection: A Random Forest Classifier was selected as the model due to its ability to handle complex datasets and perform well on imbalanced data.                                                         •  Hyperparameter Tuning: The model's hyperparameters were tuned using GridSearchCV to optimize its performance.

## Model Evaluation
The model was evaluated using the following metrics:
•  Accuracy: The model's accuracy was calculated to assess its overall performance.
•  Classification Report: A classification report was generated to evaluate the model's performance on both classes (good and bad loans).
•  Confusion Matrix: A confusion matrix was created to visualize the model's performance and identify areas for improvement.

## Model Performance
Several machine learning models were trained and evaluated,which are Logistic Regression, Decision Tree, Random Forest, SVM, and XGBoost. The results show that XGBoost performs the best, with an accuracy of 72% and an F1-score of 82% for the positive class. Random Forest also performs well, but not as well as XGBoost.

## Insights from Power BI Visualization
The Power BI visualization provides valuable insights into customer behavior and loan trends. Which are:
•  The sum of loan amount is 78 million, with a total due of 93 million and interest of 15 million.
•  Savings account holders have the highest loan amount, while permanent employees have the highest sum of loan amount collected.
•  The age group of 38-48 collected the most loans, with 64%.

## Loan Default Risk Dashboard

<img width="1380" height="808" alt="Screenshot 2025-08-21 224006" src="https://github.com/user-attachments/assets/0f7dc456-b8a5-4e49-8ecb-7ff1b01a732c" />


<img width="1364" height="772" alt="Screenshot 2025-08-21 224554" src="https://github.com/user-attachments/assets/60a05c57-3076-44a9-8a42-a5910903d792" />


## Recommendations
Based on the findings, i recommend that financial institutions use the XGBoost model to predict loan default risk and make informed lending decisions. Additionally, lenders can use insights from the Power BI visualization to identify high-risk customers and develop targeted marketing strategies.

## Conclusion
The project demonstrates the potential of machine learning in predicting loan default risk. By using XGBoost and insights from Power BI visualization, financial institutions can make informed lending decisions and minimize losses. This project highlights the importance of machine learning in finance and its potential to drive business value.
