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

sus_df = raw_df[['Region',
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

sus_df['Region'] = sus_df['Region'].astype(str)
sus_df['Top_Account_Nme'] = sus_df['Top_Account_Nme'].astype(str)
sus_df['Claim_Office_Cde'] = sus_df['Claim_Office_Cde'].astype(str)
sus_df['Marital_Status_Cde'] = sus_df['Marital_Status_Cde'].astype(str)
sus_df['Primary_Part_Of_Body_Cde'] = sus_df['Primary_Part_Of_Body_Cde'].astype(str)
sus_df['Trtm_Cde'] = sus_df['Trtm_Cde'].astype(str)
sus_df['Tenure_Bucket'] = sus_df['Tenure_Bucket'].astype(str)
sus_df['Report_Bucket'] = sus_df['Report_Bucket'].astype(str)
sus_df['Primary_Nature_Of_Injury_Cde'] = sus_df['Primary_Nature_Of_Injury_Cde'].astype(str)
sus_df['Occurrence_Cde'] = sus_df['Occurrence_Cde'].astype(str)
sus_df['Age_Bucket'] = sus_df['Age_Bucket'].astype(str)


#%% Rank Feature