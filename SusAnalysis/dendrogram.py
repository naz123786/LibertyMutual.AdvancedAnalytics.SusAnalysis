"""
"""

#%% Import Code
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import sklearn as sk

#%% Define Configuration
INPUT_PATH = Path('')

#%% Import Data
SUS = pd.read_excel(INPUT_PATH)

SUS['Region'] = SUS['Region'].astype(str)
SUS['Top_Account_Nme'] = SUS['Top_Account_Nme'].astype(str)
SUS['Claim_Office_Cde'] = SUS['Claim_Office_Cde'].astype(str)
SUS['Marital_Status_Cde'] = SUS['Marital_Status_Cde'].astype(str)
SUS['Primary_Part_Of_Body_Cde'] = SUS['Primary_Part_Of_Body_Cde'].astype(str)
SUS['Trtm_Cde'] = SUS['Trtm_Cde'].astype(str)
SUS['Tenure_Bucket'] = SUS['Tenure_Bucket'].astype(str)
SUS['Report_Bucket'] = SUS['Report_Bucket'].astype(str)
SUS['Primary_Nature_Of_Injury_Cde'] = SUS['Primary_Nature_Of_Injury_Cde'].astype(str)
SUS['Occurrence_Cde'] = SUS['Occurrence_Cde'].astype(str)
SUS['Age_Bucket'] = SUS['Age_Bucket'].astype(str)
