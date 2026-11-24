Web VPython 3.2
head = sphere(size = vec(2, 1.5, 1), pos = vec(0, 2, 0))
body = box(size = vec(1, 1, 1), pos = vec(0, 1, 0))
left_arm = box(size = vec(1, 0.1, 0.1), pos = vec(-0.4, 1, 0))
right_arm = box(size = vec(1, 0.1, 0.1), pos = vec(0.4, 1, 0))

left_leg = box(size = vec(0.1, 1, 0.1), pos = vec(-0.3, 0.3, 0))
right_leg = box(size = vec(0.1, 1, 0.1), pos = vec(0.3, 0.3, 0))
left_eye = sphere(size = vec(0.1, 0.1, 0.1), color = color.black, pos = vec(-0.45, 2, 0.5))
right_eye = sphere(size = vec(0.1, 0.1, 0.1), color = color.black, pos = vec(0.45, 2, 0.5))

wilseen = compound([head, body, left_arm, right_arm, left_leg, right_leg, left_eye, right_eye])
b = box(texture = "https://i.postimg.cc/FztGTcxQ/omg-jypapi.jpg", size = vec(3, 1, 4), pos = vec(3, 0, 0))

a = box(pos = vec(2.5, -1.5, 0), size = vec(5, 0.5 ,1), texture = "https://i.postimg.cc/26mPTQkq/38addbf8973ff8f99f524482e6676cee.jpg")
c = box(pos = vec(-2.5, -1.5, 0), size = vec(5, 0.5 ,1), texture = "https://i.postimg.cc/26mPTQkq/38addbf8973ff8f99f524482e6676cee.jpg")

g = vec(0,-9.8, 0)
wilseen.v = vec(0, 0, 0)
dt = 0.01
wilseen.pos = wilseen.pos + wilseen.v*dt
wilseen.v = wilseen.v + g*dt


while wilseen.pos.y >= 0 :
    rate(100)
    wilseen.pos = wilseen.pos + wilseen.v*dt
    wilseen.v = wilseen.v + g*dt

while True :
    rate(100)
    k = keysdown()
    if 'd' in k : 
        wilseen.pos.x = wilseen.pos.x + 0.1
    if 'a' in k :
        wilseen.pos.x = wilseen.pos.x - 0.1
    if 's' in k :
        while wilseen.pos.y < 0.1 and wilseen.pos.y > -5 :
            rate(250)
            wilseen.pos = wilseen.pos + wilseen.v*dt
        


