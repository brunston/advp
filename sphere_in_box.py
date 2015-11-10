#Brunston Poon (c) 2015, MIT License
#do not forget to source activate python2
from visual import *

#initialize *things*
ball = sphere(pos=(-5,0,0), radius=0.5, color=color.orange)
otheractive = True
if otheractive:
    ball2 = sphere(pos=(0,2,4), radius=0.5, color=color.yellow)
    ball3 = sphere(pos=(-2,-4,3), radius=0.5, color=color.magenta)

wallR = box(pos=(6,0,0), size = (0.2,12,12), color=color.red)
wallL = box(pos=(-6,0,0), size = (0.2,12,12), color=color.green)
wallT = box(pos=(0,6,0), size = (12,0.2,12), color=color.cyan)
wallB = box(pos=(0,-6,0), size = (12,0.2,12), color=color.cyan)
wallX = box(pos=(0,0,-6), size = (12,12,0.2), color=color.blue)

#set values
ball.velocity = vector(25,5,15)
if otheractive:
    ball2.velocity = vector(4,8,12)
    ball3.velocity = vector(1,2,3)

#time and dt
dt = 0.005
t = 0

#visualizations
vscale = 0.1
arrow_v = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=ball.color)
ball.trail = curve(color=ball.color)
if otheractive:
    arrow_v2 = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=ball2.color)
    ball2.trail = curve(color=ball2.color)
    arrow_v3 = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=ball3.color)
    ball3.trail = curve(color=ball3.color)

#do *stuff* to *things*
scene.autoscale = False
while t < 10:

    if (ball.pos.x > wallR.pos.x) or (ball.pos.x < wallL.pos.x):
        ball.velocity.x = -ball.velocity.x
    if (ball.pos.y > wallT.pos.y) or (ball.pos.y < wallB.pos.y):
        ball.velocity.y = -ball.velocity.y
    if (ball.pos.z > 6) or (ball.pos.z < wallX.pos.z):
        ball.velocity.z = -ball.velocity.z
    if otheractive:
        if (ball2.pos.x > wallR.pos.x) or (ball2.pos.x < wallL.pos.x):
            ball2.velocity.x = -ball2.velocity.x
        if (ball2.pos.y > wallT.pos.y) or (ball2.pos.y < wallB.pos.y):
            ball2.velocity.y = -ball2.velocity.y
        if (ball2.pos.z > 6) or (ball2.pos.z < wallX.pos.z):
            ball2.velocity.z = -ball2.velocity.z

        if (ball3.pos.x > wallR.pos.x) or (ball3.pos.x < wallL.pos.x):
            ball3.velocity.x = -ball3.velocity.x
        if (ball3.pos.y > wallT.pos.y) or (ball3.pos.y < wallB.pos.y):
            ball3.velocity.y = -ball3.velocity.y
        if (ball3.pos.z > 6) or (ball3.pos.z < wallX.pos.z):
            ball3.velocity.z = -ball3.velocity.z

    #update ball position and visualizations
    ball.pos = ball.pos + ball.velocity*dt
    arrow_v.pos = ball.pos
    arrow_v.axis = vscale*ball.velocity
    ball.trail.append(pos=ball.pos)
    if otheractive:
        ball2.pos = ball2.pos + ball2.velocity*dt
        arrow_v2.pos = ball2.pos
        arrow_v2.axis = vscale*ball2.velocity
        ball2.trail.append(pos=ball2.pos)

        ball3.pos = ball3.pos + ball3.velocity*dt
        arrow_v3.pos = ball3.pos
        arrow_v3.axis = vscale*ball3.velocity
        ball3.trail.append(pos=ball3.pos)

    rate(100)
    t += dt
