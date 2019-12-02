from python import cortex_connection
import asyncio


def main():
    print("Hehe")

    # init the class. File 1 has credentials to connect to the headset
    # File 2 is the filename we want to name the output
    test = cortex_connection.CortexConnection("./cortex_creds", "./output_sample1.txt")

    # init the connection
    test.init_connection()

    # read
    desired_count = 50
    while desired_count > 0:
        # read the number of responses you want
        responses = test.read(desired_count)
        # be sure to check and make sure you got the number you asked for
        # desired_count = desired_count - len(responses)
        desired_count = desired_count - len(responses)
        # print out as debug
        print(f"RECEIVED {len(responses)}")
        for x in range(len(responses)):
            print(responses[x])
        # print(x for x in responses)

    print("CLOSING CONNECTION")

    # close the connection
    test.close_connection()


if __name__ == "__main__":
    main()
