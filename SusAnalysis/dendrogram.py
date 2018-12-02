from pathlib import Path

import numpy as np
import pandas as pd
import sklearn as sk

#%% Configuration
INPUT_PATH = Path('')

#%% Import Dataset
SUS = pd.read_excel(INPUT_PATH,
                    dtype={'Region': str,
                           'Top_Account_Nme': str,
                           'Claim_Office_Cde': str,
                           'Marital_Status_Cde': str,
                           'Primary_Part_Of_Body_Cde': str,
                           'Trtm_Cde': str,
                           'Tenure_Bucket': str,
                           'Report_Bucket': str,
                           'Primary_Nature_Of_Injury_Cde': str,
                           'Occurrence_Cde': str,
                           'Age_Bucket': str})
