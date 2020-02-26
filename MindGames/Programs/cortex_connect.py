# File: cortex_connection.py
# Author: Alex Miu ale18@umbc.edu
# Last Updated: 11/28/2019
# Description: This program utilizes the pre-made cortex class to interface with the headset. Note that the class used
# may have been modified slightly to increase robustness.

import multiprocessing
import Resources.cortex as Cortex
import asyncio


async def child_subfunc(cf, sf, pipe1, q):
    obj = Cortex.Cortex(cf, output_filename=sf)  # Cortex holder

    print("** INIT CONNNECTION **")
    await obj.get_user_login()
    await obj.get_cortex_info()
    await obj.has_access_right()
    await obj.request_access()
    await obj.authorize(debit=5)
    await obj.get_license_info()
    await obj.query_headsets()
    if len(obj.headsets) > 0:
        print("** CREATE SESSION **")
        await obj.create_session(activate=True, headset_id=obj.headsets[0])
        await obj.create_record(title="test record 1")
        await obj.subscribe(['pow'])
        while pipe1.poll() is False:
            x = await obj.get_data()
            q.put(x)

    # quit
    await obj.close_session()
    await obj.close()
    pipe1.close()


# @desc runs as the child thread
# Uses pipes to communicate
def child_proc(cf, sf, pipe1, output_queue):
    asyncio.run(child_subfunc(cf, sf, pipe1, output_queue))  # should be async


class CortexConnection:
    # init, sets up variables
    def __init__(self, config_filename, sample_filename):
        self.q = None
        self.is_connected = False
        self.proc = None
        self.config_filename = config_filename
        self.sample_filename = sample_filename
        self.control_send = None

    # @desc called to connect to the cortex program and to the headset.
    # Note: Spawns child thread
    # @return negative on error, 0 on success
    def init_connection(self):
        self.q = multiprocessing.SimpleQueue()
        control_out, self.control_send = multiprocessing.Pipe(duplex=False)
        self.proc = multiprocessing.Process(target=child_proc, args=[self.config_filename, self.sample_filename, control_out, self.q])
        self.proc.start()

    # @desc called to close connection and output file.
    # Note: closes child thread
    # @return negative on error, 0 on success
    def close_connection(self):
        # close process
        self.control_send.send("exit")
        self.control_send.close()
        self.proc.join()


    # @desc called to grab a set of data
    # @param num_points - integer number of data points you would like to read.
    # @return a list with the json data point objects.
    # Note: check returned list length to ensure successful return
    def read(self, num_points):
        return_list = []
        for x in range(num_points):
            self._wait_for_data()
            temp = self.q.get()
            return_list.append(temp)

        return return_list

    def _wait_for_data(self):
        while True:
            if self.q.empty() is False:
                return True





