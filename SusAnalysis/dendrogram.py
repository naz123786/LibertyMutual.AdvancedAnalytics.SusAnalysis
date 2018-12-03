"""
"""


#%% Define Configuration
INPUT_PATH = ''


#%% Import Code
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram
from sklearn.feature_selection import mutual_info_classif
from sklearn.cluster import FeatureAgglomeration
import matplotlib.pyplot as plt



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

scores = {k: v for k, v in zip(predictors.columns, scores)}
scores = list(reversed(sorted(scores.items(), key=lambda x: x[1])))

print(scores)


#%% Feature Agglomeration (filter approach)
model = FeatureAgglomeration()
model = model.fit(predictors)

def plot_dendrogram(model, **kwargs):
    """https://github.com/scikit-learn/scikit-learn/blob/70cf4a676caa2d2dad2e3f6e4478d64bcb0506f7/examples/cluster/plot_hierarchical_clustering_dendrogram.py"""

    # Children of hierarchical clustering
    children = model.children_

    # Distances between each pair of children
    # Since we don't have this information, we can use a uniform one for plotting
    distance = np.arange(children.shape[0])

    # The number of observations contained in each cluster level
    no_of_observations = np.arange(2, children.shape[0]+2)

    # Create linkage matrix and then plot the dendrogram
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)

plt.title('Feature Agglomeration')
plot_dendrogram(model, labels=model.labels_)
plt.show()
