"""
"""


#%% Define Configuration
INPUT_PATH = ''


#%% Import Code
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn as sk
import seaborn as sns

from sklearn.feature_selection import mutual_info_classif


#%% Read Data
data = pd.read_excel(INPUT_PATH)
data = data[['Region',
             'Top_Account_Nme',
             'Marital_Status_Cde',
             'Primary_Part_Of_Body_Cde',
             'Trtm_Cde',
             'Tenure_Bucket',
             'Report_Bucket',
             'Primary_Nature_Of_Injury_Cde',
             'Occurrence_Cde',
             'Age_Bucket',
             'Year',
             'POP']]
for col in data.columns:
    data[col] = data[col].astype('category')

predictors = data[['Region',
                   'Top_Account_Nme',
                   'Marital_Status_Cde',
                   'Primary_Part_Of_Body_Cde',
                   'Trtm_Cde',
                   'Tenure_Bucket',
                   'Report_Bucket',
                   'Primary_Nature_Of_Injury_Cde',
                   'Occurrence_Cde',
                   'Age_Bucket']]
regressor = data['POP']


#%% Rank Features (filter approach)
scores = mutual_info_classif(predictors, regressor, discrete_features=True)
scores = dict(zip(predictors.columns, scores))
scores = list(sorted(scores, lambda x: x[1]))

print(scores)


#%%