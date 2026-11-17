Web VPython 3.2
head = sphere(size = vec(2, 1.5, 1), texture = "https://i.postimg.cc/prNzKfg8/image.png", pos = vec(0, 3, 0))
body = cone(size = vec(1, 3, 1))
body.axis = vec(0, 2, 0)
left_arm = box(size = vec(1, 0.1, 0.1), pos = vec(-1, 1, 0))
left_arm.axis = vec(1, 1, 0)
right_arm = box(size = vec(1, 0.1, 0.1), pos = vec(1, 1, 0))
right_arm.axis = vec(-1, 1, 0)

left_leg = box(size = vec(0.1, 1, 0.1), pos = vec(-0.5, -0.5, 0))
right_leg = box(size = vec(0.1, 1, 0.1), pos = vec(0.5, -0.5, 0))

wilseen = compound([head, body, left_arm, right_arm, left_leg, right_leg, body.axis, left_arm.axis, right_arm.axis])

a = box(pos = vec(2.5, -0.75, 0), size = vec(5, 0.5 ,1), texture = "https://i.postimg.cc/26mPTQkq/38addbf8973ff8f99f524482e6676cee.jpg")
c = box(pos = vec(-2.5, -0.75, 0), size = vec(5, 0.5 ,1), texture = "https://i.postimg.cc/26mPTQkq/38addbf8973ff8f99f524482e6676cee.jpg")


g = vec(0,-9.8, 0)
b.v = vec(0, 0, 0)
dt = 0.01
b.pos = b.pos + b.v*dt
b.v = b.v + g*dt


while b.pos.y >= 0 :
    rate(100)
    b.pos = b.pos + b.v*dt
    b.v = b.v + g*dt

while True :
    rate(100)
    k = keysdown()
    if 'd' in k : 
        b.pos.x = b.pos.x + 0.1
    if 'a' in k :
        b.pos.x = b.pos.x - 0.1
    if 's' in k :
        while b.pos.y < 0.1 and b.pos.y > -5 :
            rate(250)
            b.pos = b.pos + b.v*dt
        


