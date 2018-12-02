from pathlib import Path

import numpy as np
import sklearn as sk
import pandas as pd

#%% Configuration
INPUT_PATH = Path('')

#%% Import Dataset
SUS = pd.read_excel('C:\\Users\\n0253665\\Desktop\\SUS_EDA.xlsx', 
                    dtype={"Region",
                    "Top_Account_Nme",
                    "Claim_Office_Cde",
                    "Marital_Status_Cde",
                    "Primary_Part_Of_Body_Cde",
                    "Trtm_Cde",
                    "Tenure_Bucket",
                    "Report_Bucket",
                    "Primary_Nature_Of_Injury_Cde",
                    "Occurrence_Cde",
                    "Age_Bucket",
                    "Year",
                    "POP"
})
