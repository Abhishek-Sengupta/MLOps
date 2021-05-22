# NOTE: For windows users only-
# This file is to be executed to add the batch data files to dvc
# Execute this file after running git rm -r --cached 'Training_Batch_Files/*.csv' && git rm -r --cached 'Prediction_Batch_files/*.csv',
# to prevent git scm from tracking the data files as they would be tracked by dvc.

import os
from glob import glob


data_dirs = ["Training_Batch_Files","Prediction_Batch_files"]

for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        os.system(f"dvc add {filePath}")

print("\n---- all files added to dvc ----")