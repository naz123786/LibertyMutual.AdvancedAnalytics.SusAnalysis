"""
"""


#%% Import Code
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn as sk
import seaborn as sns


#%% Define Configuration
INPUT_PATH = Path('')


#%% Read Data
raw_df = pd.read_excel(INPUT_PATH)

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

regressors = raw_df[['Year', 'POP']]

predictors['Region'] = predictors['Region'].astype(str)
predictors['Top_Account_Nme'] = predictors['Top_Account_Nme'].astype(str)
predictors['Claim_Office_Cde'] = predictors['Claim_Office_Cde'].astype(str)
predictors['Marital_Status_Cde'] = predictors['Marital_Status_Cde'].astype(str)
predictors['Primary_Part_Of_Body_Cde'] = predictors['Primary_Part_Of_Body_Cde'].astype(str)
predictors['Trtm_Cde'] = predictors['Trtm_Cde'].astype(str)
predictors['Tenure_Bucket'] = predictors['Tenure_Bucket'].astype(str)
predictors['Report_Bucket'] = predictors['Report_Bucket'].astype(str)
predictors['Primary_Nature_Of_Injury_Cde'] = predictors['Primary_Nature_Of_Injury_Cde'].astype(str)
predictors['Occurrence_Cde'] = predictors['Occurrence_Cde'].astype(str)
predictors['Age_Bucket'] = predictors['Age_Bucket'].astype(str)


#%% Rank Feature