Web VPython 3.2
b = box(texture = "https://i.postimg.cc/wBmMBzDh/wilseen2.png")
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
