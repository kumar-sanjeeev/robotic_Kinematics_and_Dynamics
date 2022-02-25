"""
Unit Testing Rigid Body Transformations

MATLAB
....

Robotics Toolbox
(Used these matlab functions to get the values of transformations for preparing the unit test cases)
---
trvec2tform
eul2tform
tform2eul
---

"""

import unittest
from transformation import *
import numpy as np
class TestTransformations(unittest.TestCase):

    def test_trans1(self):
        x = 1
        y = 2
        z = 3

        cal_trans = trans1(x,y,z)
        actual_trans = np.array([[1,0,0,1],
                                [0,1,0,2],
                                [0,0,1,3],
                                [0,0,0,1]])

        np.testing.assert_almost_equal(actual_trans,cal_trans)

    def test_rpy2tr(self):

        roll= np.pi / 3
        pitch= np.pi / 3
        yaw= np.pi / 3

        cal_trans_matrix = rpy2tr(roll,pitch, yaw)
        actual_trans_matrix = np.array([[0.2500, -0.0580, 0.9665, 0],
                                          [0.4330, 0.8995, -0.0580, 0],
                                          [-0.8660, 0.4330, 0.2500, 0],
                                          [0, 0, 0, 1.0000]])
        
        np.testing.assert_almost_equal(actual_trans_matrix,cal_trans_matrix, decimal=4)

    
    def test_tr2rpy(self):

        transformation = np.array([[0.2500, -0.0580, 0.9665, 0],
                                          [0.4330, 0.8995, -0.0580, 0],
                                          [-0.8660, 0.4330, 0.2500, 0],
                                          [0, 0, 0, 1.0000]])
        
        r, p, y = tr2rpy(transformation)
        cal_angles = np.array([r,p,y])

        actual_angles = np.array([np.pi/3, np.pi/3, np.pi/3])

        np.testing.assert_almost_equal(actual_angles,cal_angles, decimal=4)



    def test_rot(self):
        rotation_x = rotr(np.pi/3)
        rotation_y = rotp(np.pi/3)
        rotation_z = roty(np.pi/3)

        actual_rot_x = np.array([[1.0000, 0, 0],
                                      [0, 0.5000, -0.8660],
                                      [0, 0.8660, 0.5000]])
        actual_rot_y = np.array([[0.5000, 0, 0.8660],
                                      [0, 1.0000, 0],
                                      [-0.8660, 0, 0.5000]]) 
        
        actual_rot_z = np.array([[0.5000, -0.8660, 0],
                                      [0.8660, 0.5000, 0],
                                      [0, 0, 1.0000]])
        np.testing.assert_almost_equal(actual_rot_x,rotation_x,decimal=4)
        np.testing.assert_almost_equal(actual_rot_y,rotation_y,decimal=4)
        np.testing.assert_almost_equal(actual_rot_z,rotation_z,decimal=4)

if __name__ == "__main__":
    unittest.main()