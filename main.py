Web VPython 3.2
b = box(texture = "https://i.postimg.cc/wBmMBzDh/wilseen2.png", pos = vec(0, 1, 0))
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
    if 'w' in k :
        b.pos.y = b.pos.y + 0.1
    if 's' in k :
        while b.pos.y < 0.1 and b.pos.y > -5 :
            rate(250)
            b.pos = b.pos + b.v*dt
        
