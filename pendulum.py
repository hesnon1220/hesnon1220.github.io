import math
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def next_statu(length:float,theta:float,vel:float,delta_time:float,g:float=9.80665)->tuple:
    acc = -g/length*math.sin(theta)
    vel_new = vel + delta_time*acc
    theta_new = theta + vel*delta_time + (1/2)*acc*(pow(delta_time,2))
    return theta_new,vel_new

def cartesian_trans(length:float,theta:float)->tuple:
    y = -length*math.cos(theta)
    x = length*math.sin(theta)
    return x,y

delta_time = pow(10,-2)
vel = 0
theta = math.pi/2
length = 250
point_x = [cartesian_trans(length,theta)[0]]
point_y = [cartesian_trans(length,theta)[1]]
for i in range(10000):
    theta,vel = next_statu(length,theta,vel,delta_time)
    x,y = cartesian_trans(length,theta)
    point_x.append(x)
    point_y.append(y)

print(point_x)
print(point_y)
fig = plt.figure(figsize=(8,6),tight_layout=True)
#plt.plot(point_x,point_y)
plt.xlim(-length-20,length+20)
plt.ylim(-length-20,length+20)


line, = plt.plot([], [], color='black', linestyle='-')
dot, = plt.plot([], [], color='red', marker='o', markersize=10, markeredgecolor='black', linestyle='')

plt.grid(ls="--")
def update(i):
    line.set_data([0,point_x[i]], [0,point_y[i]])
    dot.set_data(point_x[i], point_y[i])

    return dot,

def init():
    line.set_data([0,point_x[0]], [0,point_y[0]])
    dot.set_data(point_x[0], point_y[0])
    return dot,

N = len(point_x)
ani = animation.FuncAnimation(fig=fig, func=update, frames=N, init_func=init, interval=1000/N, blit=True, repeat=True)
ani.save('01.mp4',writer='ffmpeg',fps=1000)
#ani.save('sin_test2.gif', writer='pillow', fps=1/0.04)
plt.show()