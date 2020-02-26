# Import necessary Python modules
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from pynput.keyboard import Key, Controller
import time
import json
import pickle

# directions
UP = 0  # red
DOWN = 1  # green
LEFT = 2  # blue
RIGHT = 3  # orange

def convertdata():
    txtpaths = ['Programs/Resources/temp_up.txt', 'Programs/Resources/temp_down.txt', 'Programs/Resources/temp_left.txt', 'Programs/Resources/temp_right.txt']
    dirs = [UP, DOWN, LEFT, RIGHT]
    csvpath = 'Data_sets/new_data.csv'
    with open(csvpath, 'w+') as cp:
        cp.write(
            "AF3/theta,AF3/alpha,AF3/betaL,AF3/betaH,AF3/gamma,F7/theta,F7/alpha,F7/betaL,F7/betaH,F7/gamma,F3/theta,F3/alpha,F3/betaL,F3/betaH,F3/gamma,FC5/theta,FC5/alpha,FC5/betaL,FC5/betaH,FC5/gamma,T7/theta,T7/alpha,T7/betaL,T7/betaH,T7/gamma,P7/theta,P7/alpha,P7/betaL,P7/betaH,P7/gamma,O1/theta,O1/alpha,O1/betaL,O1/betaH,O1/gamma,O2/theta,O2/alpha,O2/betaL,O2/betaH,O2/gamma,P8/theta,P8/alpha,P8/betaL,P8/betaH,P8/gamma,T8/theta,T8/alpha,T8/betaL,T8/betaH,T8/gamma,FC6/theta,FC6/alpha,FC6/betaL,FC6/betaH,FC6/gamma,F4/theta,F4/alpha,F4/betaL,F4/betaH,F4/gamma,F8/theta,F8/alpha,F8/betaL,F8/betaH,F8/gamma,AF4/theta,AF4/alpha,AF4/betaL,AF4/betaH,AF4/gamma,direction\n")
        for i in range(0, 4):
            with open(txtpaths[i]) as tp:
                dir = dirs[i]
                sample = tp.readline()
                while sample:
                    if (sample != "\n"):
                        sample = sample.split('[')
                        sample = sample[1].split(']')
                        if (dir != -1):
                            cp.write(sample[0])
                            cp.write(',' + str(dir) + '\n')
                    sample = tp.readline()


def main():

    # ML parameters to be set in Settings game menu
    bootstrap = False # (bool) sample with replacement = true
    max_depth = 60 # (int) max depth
    max_features = 3 # (int)
    min_samples_leaf = 1 # (int)
    min_samples_split = 2 # (int > 1)
    n_estimators = 80 # (int) number of decision trees in forest
    
    # delete the temporary files
    convertdata()
    eeg_data = pd.read_csv('Data_Sets/new_data.csv')

    print(eeg_data.shape)
    eeg_data.head()

    # Create X, y
    X = eeg_data.drop('direction', axis=1)
    y = eeg_data['direction']

    print(X.shape)
    print(y.shape)

    # Split the data to train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=42)

    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)

    # Create a random forest classifier with 100 estimators    
    rf = RandomForestClassifier(bootstrap=bootstrap,max_depth=max_depth,max_features=max_features,min_samples_leaf=min_samples_leaf,min_samples_split=min_samples_split,n_estimators=n_estimators)
    # Fit the model to X_train and y_train
    rf.fit(X_train, y_train)
    # Make predictions on X_test
    y_pred = rf.predict(X_test)

    # Compute accuracy
    print("Accuracy: ", accuracy_score(y_test, y_pred))

    # store model
    pickle.dump(rf, open("stored_model.pickle", 'wb'))


if __name__ == '__main__':
    main()





