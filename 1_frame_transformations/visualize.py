from turtle import color
from matplotlib import projections
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d


# u = np.array([3,0,0])
# v = np.array([0,3,0])
# q = np.array([0,0,3])
# test = np.array([5,5,5])
# fig = plt.figure()
# ax = plt.gca(projection= '3d')
# ax.set_xlim([-1,10])
# ax.set_ylim([-10,10])
# ax.set_zlim([0,10])

# start_point = np.array([0,0,0])

# ax.quiver(start_point[0],start_point[1],start_point[2],u[0],u[1],u[2])
# ax.quiver(start_point[0],start_point[1],start_point[2],v[0],v[1],v[2])
# ax.quiver(start_point[0],start_point[1],start_point[2],q[0],q[1],q[2], color='r')
# ax.quiver(start_point[0],start_point[1],start_point[2],test[0],test[1],test[2], color='b')



def plot_transformation(transformation):

    fig = plt.figure()
    ax = fig.gca(projection='3d')



    x = np.array([0,0,0, transformation[0,3], transformation[0,3], transformation[0,3]])
    y = np.array([0,0,0, transformation[1,3], transformation[1,3], transformation[1,3]])
    z = np.array([0,0,0, transformation[1,3], transformation[2,3], transformation[2,3]])


    i_unitVector = np.concatenate([np.array([1,0,0]), transformation[0:3, 0]])
    j_unitVector = np.concatenate([np.array([0,1,0]), transformation[0:3, 1]])
    k_unitVector = np.concatenate([np.array([0,0,1]), transformation[0:3, 2]])

    red_channel = np.array([1,0,0])
    green_channel = np.array([0,1,0])
    blue_channel = np.array([0,0,1])

    color_rgb = np.array([red_channel, blue_channel, green_channel, red_channel, blue_channel, green_channel])

    q = ax.quiver(x,y,z,i_unitVector,j_unitVector,k_unitVector,length= 0.05, color=color_rgb, lw=1)

    plt.plot([x[0],x[3]],[y[0],y[3]],[z[0],z[3]], '--',color='black')

    plt.show()


