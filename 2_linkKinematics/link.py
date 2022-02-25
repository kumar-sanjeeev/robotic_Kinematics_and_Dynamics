"""
   Robot Links

    - Kinematic parameters
    - Inertial parameters

    Parameters:
    - name
    - dh params : alpha, a , d , theta
    - inertia_matrix, cog, mass

    Functions:
    - transform
    - str
    -repr
"""

import numpy as np


class Link:

    """
    Robot Link Class

    Parameters
    -----------------------------------------------------------------------------
    ---Joint Parameters---
    name:           name of the link
    theta:          rotation about z axis of frame i needed to make x axis of frame i parellel with x axis of frame i+1.
    d:              translational along z axis of frame i needed to make x axis of frame i interesect with x axis of frame i+1.

    ----Link Parameters----Always constant.Can be part of mechanical design of robot structure
    alpha:          rotation about x axis of frame i needed to make z axis of frame i parallel with z axis of farme i+1.
    a:              translational along x axis of frame i needed to make z axis of frame i intersect with z axis of frame i+1.

    inertia_matrix: inertia matrix of the link
    joint_type      joint type of the link
    cog:            centre of gravity of base frame
    mass:           mass of link

    Methods
    ---
    tranform(q)  get the transformation of the link

    """

    def __init__(self, name="", alpha = 0, a = 0, d = 0, theta = 0,
                joint_type = 'revolute', inertia_matrix = np.zeros((3,3)),
                cog = np.zeros(3), mass= 0):

        """
        Initialization Function

        ---
        Parameters
        ---
        Refer Class definition
        """     
        self.__name = name
        self.__alpha = alpha
        self.__a = a
        self.__d = d
        self.__theta = theta
        self.__joint_type = joint_type
        self.__inertia_matrix = inertia_matrix
        self.__cog = cog
        self.__mass = mass

    
    def __str__(self):
        string = f"{self.name}\n"
        string += "Parameters\tValue\n"
        string += "--\t\t--\n"
        string += f"joint\t\t{self.joint_type}\n"
        string += f"d\t\t{self.d}\n"
        string += f"alpha\t\t{self.alpha}\n"
        string += f"a\t\t{self.a}\n"

        return string

    def __repr__(self):
        string = f"Link Name = {self.name}, theta={self.theta}"
        string += f", d={self.d}, alpha={self.alpha}, a={self.a})"

        return string

    def transform(self, q):
        """
        Function to generate Transformation matrix from link and joint parameters

        Parameters:
        ---
        q : variable parameter for particular link (theta: in case of revolute joint, d:in case of prismatic joint)

        Returns:
        ---
        4x4 transformation matrix

        """

        alpha = self.__alpha
        a = self.__a

        if self.__joint_type == 'revolute':
            theta = q
            d = self.__d
        else:
            theta = self.__theta
            d = q
        
        # DH Parameters
        # transformation = np.array([[np.cos(theta), -np.sin(theta)* np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        #                            [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta),
        #                            [0, np.sin(alpha), np.cos(alpha), d],
        #                            [0,0,0,1]]])


        # Modified DH parameters
        transformation = np.array([
            [np.cos(theta), - np.sin(theta), 0, a],
            [np.sin(theta) * np.cos(alpha), np.cos(theta) *
             np.cos(alpha), - np.sin(alpha), - np.sin(alpha) * d],
            [np.sin(theta) * np.sin(alpha), np.cos(theta) *
             np.sin(alpha), np.cos(alpha), np.cos(alpha) * d],
            [0, 0, 0, 1]
        ])

        return transformation


    # Getters and Setters 
    # with property decorator : attributes will now only be in read mode.
    # that's why getter and setter is needed
    @property
    def name(self):
        """For getting the Name of the link"""
        return self.__name

    @name.setter
    def name(self,name):
        """
        For Setting the Name of the link
        ---
        Parameters
        name
        ---   
        """
        self.__name = name

    
    @property
    def alpha(self):
        """For getting the alpha angle  of the link"""
        return self.__alpha

    @alpha.setter
    def alpha(self,alpha):
        """
        For Setting the alpha angle of the link
        ---
        Parameters
        angle value
        ---   
        """
        self.__alpha = alpha

    
    @property
    def a(self):
        """For getting the length of the link"""
        return self.__a

    @a.setter
    def a(self,a):
        """
        For Setting the length of the link
        ---
        Parameters
        a
        ---   
        """
        self.__a = a

    
    @property
    def d(self):
        """For getting the distance d """
        return self.__d

    @d.setter
    def d(self,d):
        """
        For Setting the distance d
        ---
        Parameters
        d
        ---   
        """
        self.__d = d
        
    
    @property
    def theta(self):
        """For getting the theta of the joint"""
        return self.__theta

    @theta.setter
    def theta(self,theta):
        """
        For Setting the theta of the joint
        ---
        Parameters
        theta
        ---   
        """
        self.__theta = theta

    @property
    def joint_type(self):
        """For getting the type  of the joint"""
        return self.__joint_type

    @joint_type.setter
    def joint_type(self,joint_type):
        """
        For Setting the type of the joint
        ---
        Parameters
        type of the joint
        ---   
        """
        joint_type_considered = ['revolute', 'prismatic']

        try:
            assert( joint_type in joint_type_considered)
            self.__joint_type = joint_type

        except AssertionError:
            raise(f"joint type {joint_type} not considered/available")
    
    @property
    def inertia_matrix(self):
        """For getting the inertia matrix of the link"""
        return self.__inertia_matrix

    @inertia_matrix.setter
    def inertia_matrix(self,inertia_matrix):
        """
        For Setting the inertia matrix of the link
        ---
        Parameters
        Inertia values
        ---   
        """

        try:
            assert(inertia_matrix.shape == (3,3))
            self.__inertia_matrix = inertia_matrix

        except AssertionError:
            raise("Shape of inertia matrix is incorrect")
    
    @property
    def cog(self):
        """For getting the cog of the link"""
        return self.__cog

    @cog.setter
    def cog(self,cog):
        """
        For Setting the cog value of the link
        ---
        Parameters
        Cog Values
        ---   
        """

        try:
            assert(cog.shape == (3,))
            self.__cog = cog

        except AssertionError:
            raise("Shape of cog matrix is incorrect")
    
    @property
    def mass(self):
        """For getting the mass value of the link"""
        return self.__mass

    @mass.setter
    def mass(self,mass):
        """
        For Setting the mass of the link
        ---
        Parameters
        mass value
        ---   
        """
        self.__mass = mass

