import cortex_connect as c
import sys

def main():

    # init the class. File 1 has credentials to connect to the headset
    # File 2 is the filename we want to name the output
    test = c.CortexConnection("Programs/Resources/cortex_creds", "Programs/Resources/temp_down.txt")

    # init the connection
    test.init_connection()

    # read
    desired_count = 500 # int(sys.argv[1])
    current_count = 0
    while current_count < desired_count:
        # read the number of responses you want
        responses = test.read(1)
        # be sure to check and make sure you got the number you asked for
        current_count = current_count + len(responses)
        # print out as debug
        print(f"RECEIVED {current_count}")

    print("CLOSING CONNECTION")

    # close the connection
    test.close_connection()


if __name__ == "__main__":
    main()
