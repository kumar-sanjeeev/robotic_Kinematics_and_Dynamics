"""

Description: 

Rigid Body transformations

Pose of a rigid body in a space can be defined through translation and orientation. 
-----------------------------------------------------------------------------------
For Orientation we have different types of representations that we can use for example:
-Euler Angle 
-Angle and Axis
-Unit Quaternion
-----------------------------------------------------------------------------------
For our case we are using the Euler angle that is also called minimal angle representation. 

Main Functions:
1. rpy2transform : 
---
Given : Roll(x), pitch(y) and yaw(z)
Return: transformation matrix

2. tranform2rpy :
---
Given : Transformation matrix is given
Return: roll, pitch and yaw angle

"""

import numpy as np

def trans1 (x,y,z):
    """
    Returns a 4x4 transformation matrix given x,y,z 
    ...
    Parameters
    ---
    x, y and z position in space

    Returns
    ---
    4X4 transformation matrix
    """
    temp = np.eye(4)
    temp[0][3] = x
    temp[1][3] = y
    temp[2][3] = z

    return temp

def rotr(roll_angle):
    """
    Returns the elementary rotation matrix in which
    rotation takes place around x axis

    ....
    Parameters
    ---
    roll angle

    Returns
    ---
    3x3 rotation matrix

    """

    rot = np.eye(3)
    rot[1][1] = np.cos(roll_angle)
    rot[1][2] = -1*np.sin(roll_angle)
    rot[2][1] = np.sin(roll_angle)
    rot[2][2] = np.cos(roll_angle)

    return rot

def rotp(pitch_angle):
    """
    Returns the elementary rotation matrix in which 
    rotation take place about y axis
    ....
    Parameters
    ---
    pitch angle

    Returns
    ---
    3x3 rotation matrix
    """

    rot = np.eye(3)
    rot[0][0] = np.cos(pitch_angle)
    rot[0][2] = np.sin(pitch_angle)
    rot[2][0] = -1*np.sin(pitch_angle)
    rot[2][2] = np.cos(pitch_angle)

    return rot

def roty(yaw_angle):
    """
    Returns the elementary  matrix in which 
    rotation take place about z axis
    ....
    Parameters
    ---
    yaw angle

    Returns
    ---
    3x3 rotation matrix
    """

    rot = np.eye(3)
    rot[0][0] = np.cos(yaw_angle)
    rot[0][1] = -1*np.sin(yaw_angle)
    rot[1][0] = np.sin(yaw_angle)
    rot[1][1] = np.cos(yaw_angle)

    return rot



def rpy2tr (roll, pitch, yaw):

    """
    Returns the homogenous transformation matrix
    ....
    Parameters
    ---
    roll_angle, pitch_angle, yaw_angle

    Returns
    ---
    4x4 rotation matrix
    """

    rotation_x = rotr(roll)
    rotation_y = rotp(yaw)
    rotation_z = roty(pitch)

    final_rot = rotation_z @ rotation_y @ rotation_x         # fixed frame rotation

    trans = np.eye(4)
    trans[0:3,0:3] = final_rot

    return trans


def tr2rpy(transformation):
    """
    Returns the roll,pitch and yaw angle given the transformation matrix
    ...

    Parameters: transformation matrix(3x3)
    ---

    Returns:
    ---
    roll angle
    pitch angle
    yaw angle
    ---

    """

    rotation  = transformation[0:3,0:3]

    yaw = np.arctan2(rotation[1][0], rotation[0][0])

    pitch = np.arctan2(-1*rotation[2][0], np.sqrt(rotation[2][1]**2+rotation[2][2]**2))

    roll = np.arctan2(rotation[2][1], rotation[2][2])

    return roll,pitch,yaw
