#Brunston Poon (c) 2015, MIT License
#adapted from falling_objects_template
#do not forget to source activate python2
from __future__ import print_function, division
from visual import *
from visual.graph import *

#Displays
displayer = display(title = "Display", width=500, height=500, center=(0,0,0))
graphVelocity = gdisplay(xtitle="Time (s)", ytitle="Y Velocity (m/s)",\
                          xmax = 10, xmin = 0, ymax = 5, ymin = -25,\
                          x = 600, y = 400, width = 500)

velocityA = gcurve(color = color.orange)
velocityB = gcurve(color = color.cyan)
velocityTime = gcurve(color = color.green)

graphPosition = gdisplay(xtitle = "Time (s)", ytitle="Y Position (m)",\
                          xmax = 10, xmin = 0, ymax = 35, ymin = 0, x = 600,\
                          y = 0, width = 500)

positionYA = gcurve(color = color.orange)
positionYB = gcurve(color = color.cyan)

#Constants
constant = {'g': 9.81, 'cor': 1, 'd': 0.2, 'ma': 1, 'mb': 2, 'linear': 0,\
            'fdepth': 0.2, 'fpos': 0, 'r': 1}

#Objects
floor=box(pos=vector(0,constant['fpos'],0),size=(20,constant['fdepth'],12),\
          color=color.blue)

ballA=sphere(pos=vector(-5,30,0),radius=constant['r'],color=color.orange)
ballB=sphere(pos=vector(5,30,0),radius=constant['r'],color=color.cyan)

def main():
    ballA.velocity = vector(0,-5,0)
    ballA.velocity = vector(0,-5,0)

    #fdraglin =         #determine an expression for the linear drag force

    t = 0
    dt = 0.01
    while ballA.pos.y>(constant['fpos']+constant['fdepth']/2+constant['r']):
        rate(100)
        ballA.velocity.y = ballA.velocity.y
        ballB.velocity.y = ballB.velocity.y #make the necessary change to include the drag force and force of gravity acting on ball2

        if ballA.y<(constant['fpos']+constant['fdepth']/2+constant['r']):
            ballA.velocity.y = -constant['cor']*ballA.velocity.y

        if ballB.y<(constant['fpos']+constant['fdepth']/2+constant['r']):
            ballB.velocity.y = -constant['cor']*ballB.velocity.y

        velocityA.plot(pos = (t, ballA.velocity.y))
        velocityB.plot(pos = (t, ballB.velocity.y))
        velocityTime.plot(pos = (t, constant['linear']))
        positionYA.plot(pos = (t, ballA.pos.y))
        positionYB.plot(pos = (t, ballB.pos.y))
        ballA.pos = ballA.pos + ballA.velocity*dt
        ballB.pos = ballB.pos + ballB.velocity*dt

        t = t + dt

if __name__== "__main__":
    main()
