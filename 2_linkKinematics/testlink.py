"""
Unit Testing Rigid Body Transformations

MATLAB
....

Robotics Toolbox
(Used these matlab functions to get the values of transformations)
---
trvec2tform
eul2tform
tform2eul
---

"""

import unittest
from link import Link
import numpy as np


class TestLink(unittest.TestCase):

    def test_transform_theta(self):

        link = Link(name="link1", alpha=np.pi/3, a = 0.1, d = 0.1)          # why joint_type is not passed, bcz default joint type is revolute joint

        transformation = link.transform(np.pi/2)
        actual_transformation = np.array([[0.0000, -1.0000, 0, 0.1000],
                                          [0.5000, 0.0000, -0.8660, -0.0866],
                                          [0.8660, 0.0000, 0.5000, 0.0500],
                                          [0, 0, 0, 1.0000]])
        
        np.testing.assert_almost_equal(actual_transformation,transformation,decimal=4)

    def test_transform_a(self):
        link = Link(name='Link1', alpha = np.pi/3, theta = np.pi / 2,
                    d = 0.1, joint_type='prismatic')
        
        transformation = link.transform(0.1)
        actual_transformation = np.array([[0.0000, -1.0000, 0, 0],
                                          [0.5000, 0.0000, -0.8660, -0.0866],
                                          [0.8660, 0.0000, 0.5000, 0.0500],
                                          [0, 0, 0, 1.0000]])

        np.testing.assert_almost_equal(actual_transformation, transformation, decimal=4)
        
    




if __name__ == "__main__":
    unittest.main()