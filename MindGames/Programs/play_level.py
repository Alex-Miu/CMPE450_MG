# Import necessary Python modules

import pandas as pd
from pynput.keyboard import Key, Controller
import json
import pickle

import cortex_connect as c


def main():
    # load the model from file
    rf = pickle.load(open("stored_model.pickle", 'rb'))


    keyboard = Controller()

    # init the cortex thing
    # init the class. File 1 has credentials to connect to the headset
    #  File 2 is the filename we want to name the output
    test = c.CortexConnection("./cortex_creds", "./output_sample1.txt")
    print("INIT CONNECTION")

    # init the connection
    test.init_connection()

    # read
    desired_count = 50
    while desired_count > 0:
        # read the number of responses you want
        responses = test.read(1)
        # be sure to check and make sure you got the number you asked for
        # desired_count = desired_count - len(responses)
        # print out as debug
        print(f"RECEIVED {len(responses)}")
        for x in range(len(responses)):
            resp = json.loads(responses[x])
            # convert the datasample into a pandas DataFrame
            dataSample = pd.DataFrame([resp["pow"]])
            print("DATASAMPLE", dataSample)

            test_pred = rf.predict(dataSample)
            print("Predicted class: ", end='')
            print(test_pred[0])

            # Keyboard press
            if (test_pred[0] == 0):
                keyboard.press(Key.up)
                keyboard.release(Key.up)
            elif (test_pred[0] == 1):
                keyboard.press(Key.down)
                keyboard.release(Key.down)
            elif (test_pred[0] == 2):
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif (test_pred[0] == 3):
                keyboard.press(Key.right)
                keyboard.release(Key.right)

    print("CLOSING CONNECTION")

    # close the connection
    test.close_connection()

if __name__ == '__main__':
    main()





