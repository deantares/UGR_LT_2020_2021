# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:26:08 2020

@author: Antonio
"""

import unittest

from selfDrivingCar import SelfDrivingCar 

class selfDrivingCarTest(unittest.TestCase):
 
    def setUp(self):
 
        self.car = SelfDrivingCar()
  
 
    def test_stop(self):
 
        self.car.speed = 5
 
        self.car.stop()
 
        # Verify the speed is 0 after stopping
 
        self.assertEqual(0, self.car.speed)
        
        # Verify it is Ok to stop again if the car is already stopped
 
        self.car.stop()
 
        self.assertEqual(0, self.car.speed)


if __name__ == '__main__':
    unittest.main()