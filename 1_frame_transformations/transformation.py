"""
Rigid Body transformations

translation ---->trans
rotation    ---->
rpy2tr --> roll-pitch-yaw (given)---> return transformation matriz
tr2rpy --> given --> transformation matrix --return---> roll,pitch,yaw 

"""

from logging.handlers import RotatingFileHandler
from typing import final
import numpy as np
from zmq import THREAD_NAME_PREFIX


def trans1 (x,y,z):
    """
    Returns a 4x4 transformation matrix given x,y,z 
    """

    temp = np.eye(4)
    temp[0][3] = x
    temp[1][3] = y
    temp[2][3] = z

    return temp

def rotr(angle_val):
    """
    Returns the rotation matrix in which
    rotation takes place around x axis
    """

    rot = np.eye(3)
    rot[1][1] = np.cos(angle_val)
    rot[1][2] = -1*np.sin(angle_val)
    rot[2][1] = np.sin(angle_val)
    rot[2][2] = np.cos(angle_val)

    return rot

def rotp(angle_val):
    """
    Returns the rotation matrix in which 
    rotation take place arounf y axis
    """

    rot = np.eye(3)
    rot[0][0] = np.cos(angle_val)
    rot[0][2] = np.sin(angle_val)
    rot[2][0] = -1*np.sin(angle_val)
    rot[2][2] = np.cos(angle_val)

    return rot

def roty(angle_val):
    """
    Returns the rotation matrix in which 
    rotation take place arounf z axis
    """

    rot = np.eye(3)
    rot[0][0] = np.cos(angle_val)
    rot[0][1] = -1*np.sin(angle_val)
    rot[1][0] = np.sin(angle_val)
    rot[1][1] = np.cos(angle_val)

    return rot



def rpy2tr (roll, pitch, yaw):

    rotation_x = rotr(roll)
    rotation_y = rotp(yaw)
    rotation_z = roty(pitch)

    final_rot = rotation_z @ rotation_y @ rotation_x

    trans = np.eye(4)
    trans[0:3,0:3] = final_rot

    return trans


def tr2rpy(transformation):
    """
    Returns the roll,pitch and yaw anglw given the transformation matrix
    
    ---
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

x = rpy2tr(np.pi/3,0,0)
print(x)
print(x[0,3])