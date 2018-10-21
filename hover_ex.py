import json
import requests
import unittest
import os
import time
from collections import namedtuple
from hoverpy import HoverPy, capture


class TestTime(unittest.TestCase):
    endpoint = 'http://localhost:8000/'

    def setUp(self):
        """set end-point for time api"""
        self.time_api_url = 'http://time.jsontest.com'

    def test_capture(self):
        with HoverPy(capture=True) as hp:
            # lets capture some traffic
            r = requests.get(self.time_api_url)
            j = r.json()
            print("Response time which have been captured:  {0}".format(j['milliseconds_since_epoch']))
            self.assertIn("milliseconds_since_epoch", j)

            # lets switch to simulation mode
            simulation_data = hp.simulation()
            body_data = simulation_data["data"]["pairs"][0]["response"]["body"]
            simulated_body_as_tuple = json.loads(body_data,
                                                 object_hook=lambda d: namedtuple('response_tuple', d.keys())(
                                                     *d.values()))
            print("Response time which have been simulated: {0}".format(simulated_body_as_tuple[1]))

            # lets check that simulation mode is working
            self.assertEquals(j['milliseconds_since_epoch'], simulated_body_as_tuple[1])
            print('-----')
            os.unlink("test_time.db")

    def test_playback(self):
        with HoverPy(capture=True) as hp:
            r1 = requests.get(self.time_api_url)
            print("Response time which have been captured:  {0}".format(r1.json()["milliseconds_since_epoch"]))
            hp.simulate()
            time.sleep(0.05)
            r2 = requests.get(self.time_api_url)
            print("Response time which have been captured:  {0}".format(r2.json()["milliseconds_since_epoch"]))
            self.assertEquals(r1.json()["milliseconds_since_epoch"], r2.json()["milliseconds_since_epoch"])

    @capture("test_time.db", recordMode="once")
    def test_time(self):
        captured_time = requests.get(self.time_api_url)
        self.assertTrue("time", captured_time.json()["milliseconds_since_epoch"])


if __name__ == '__main__':
    unittest.main()
