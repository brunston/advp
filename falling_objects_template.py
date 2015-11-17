##===================================================================

## Ben MacBride
##modified by Brunston Poon
## falling_objects.py

## Model objects falling under the influence of linear air resistance

##===================================================================

## Modules-----------------------------------------------------------

from __future__ import print_function, division

from visual import *
from visual.graph import *

## Graphs -------------------------------------------------
scene1 = display(title = "Falling Objects", width = 600, height = 1000,
center=(0, 0, 0))
scene1.autoscale = True

graph1 = gdisplay(xtitle="Time (s)", ytitle="Y Velocity (m/s)",xmax = 20, xmin = 0,
ymax = 5, ymin = -25, x = 600, y = 400, width = 600)
vel1 = gcurve(color = color.yellow)
vel2 = gcurve(color = color.green)
vT = gcurve(color = color.blue)

graph2 = gdisplay(xtitle = "Time (s)", ytitle="Y Position (m)", xmax = 20, xmin = 0,
ymax = 35, ymin = 0, x = 600, y = 0, width = 600)
ypos1 = gcurve(color = color.yellow)
ypos2 = gcurve(color = color.green)

## Constants and Initial Values--------------------------------------

g = 9.8
COR = 1
d = .95           #drag force constant
m1 = 1
m2 = 1
vTlin = 0
if d!=0:
    vTlin = (m2*g)/d #from Fnet = 0 = mg-dVt
    print("vTlin:", vTlin)
floordepth = 0.2
floorpos = 0
r=1


## Objects ----------------------------------------------------------

floor=box(pos=vector(0,floorpos,0),size=(20,floordepth,12),color=color.blue)

myball1=sphere(pos=vector(-5,30,0),radius=r,color=color.yellow)
myball2=sphere(pos=vector(5,30,0),radius=r,color=color.green)

## Main program------------------------------------------------------

#scene.stereo = 'redcyan'

myball1.velocity = vector(0,-5,0)
myball2.velocity = vector(0,-5,0)

fdraglin = d

t = 0
dt = 0.01
while 1==1:#myball2.pos.y>(floorpos+floordepth/2+r):
    rate(100)
    myball1.velocity.y = myball1.velocity.y - g*dt
    myball2.velocity.y = myball2.velocity.y - g*dt - fdraglin*myball2.velocity.y*dt

    if myball1.y<(floorpos+floordepth/2+r):
        myball1.velocity.y = -COR*myball1.velocity.y

    if myball2.y<(floorpos+floordepth/2+r):
        myball2.velocity.y = -COR*myball2.velocity.y

    vel1.plot(pos = (t, myball1.velocity.y))
    vel2.plot(pos = (t, myball2.velocity.y))
    vT.plot(pos = (t, vTlin))
    ypos1.plot(pos = (t, myball1.pos.y))
    ypos2.plot(pos = (t, myball2.pos.y))
    myball1.pos = myball1.pos + myball1.velocity*dt
    myball2.pos = myball2.pos + myball2.velocity*dt

    t = t + dt
