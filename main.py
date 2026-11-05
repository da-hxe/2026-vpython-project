Web VPython 3.2
b = box(texture = "https://i.postimg.cc/wBmMBzDh/wilseen2.png")
a = box(pos = vec(2.5, -0.75, 0), size = vec(5, 0.5 ,1), texture = "https://i.postimg.cc/26mPTQkq/38addbf8973ff8f99f524482e6676cee.jpg")
c = box(pos = vec(-2.5, -0.75, 0), size = vec(5, 0.5 ,1), texture = "https://i.postimg.cc/26mPTQkq/38addbf8973ff8f99f524482e6676cee.jpg")
while True :
    rate(100)
    k = keysdown()
    if 'd' in k : 
        b.pos.x = b.pos.x + 0.1
    if 'w' in k :
        b.pos.y = b.pos.y +0.1
    if 'a' in k :
        b.pos.x = b.pos.x -0.1
    if 's' in k :
        b.pos.y = b.pos.y -0.1

