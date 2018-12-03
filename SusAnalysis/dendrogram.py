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
raw_df = pd.read_excel(INPUT_PATH)
raw_df = raw_df[['Region',
                 'Top_Account_Nme',
                 'Claim_Office_Cde',
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
raw_df = raw_df.astype('category')

predictors = raw_df[['Region',
                     'Top_Account_Nme',
                     'Claim_Office_Cde',
                     'Marital_Status_Cde',
                     'Primary_Part_Of_Body_Cde',
                     'Trtm_Cde',
                     'Tenure_Bucket',
                     'Report_Bucket',
                     'Primary_Nature_Of_Injury_Cde',
                     'Occurrence_Cde',
                     'Age_Bucket']]

regressors = raw_df[['POP']]


#%% Rank Features (filter approach)
scores = mutual_info_classif(predictors, regressors, discrete_features=True)
scores = dict(zip(predictors.columns, scores))
scores = list(sorted(scores, lambda x: x[1]))
print(scores)