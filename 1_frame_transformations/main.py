from transformation import *
from visualize import *
import numpy as np

if __name__ == "__main__":
    matrix1 = trans1(1,2,3)
    print("----trans1 function----")
    print(matrix1)
    print()

    matrix2 = rotr(np.pi/2)
    print("----rotx function----")
    print(matrix2)
    print()

    matrix3 = rotp(np.pi/2)
    print("----roty function----")
    print(matrix3)
    print()


    matrix4 = roty(np.pi/2)
    print("----rotz function----")
    print(matrix4)
    print()

    matrix5 = rpy2tr(np.pi/2, np.pi/2, np.pi/2)
    print("----rpy2tr function----")
    print(matrix5)
    print()

    r,p,y = tr2rpy(matrix5)
    print("----tr2rpy function----")
    print("Roll Angle:  {}\nPitch angle:  {}\nYaw angle:  {}".format(r,p,y))
    print()

    transformation = rpy2tr(np.pi/3,0,0)
    transformation = trans1(0.05,0.05,0.05)
    plot_transformation(transformation)