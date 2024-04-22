import pygame as pg
from time import sleep

while True:
    try:
        N = int(input("Ingrese el número de discos: "))
        if N > 0: break
    except ValueError:
        pass

pg.init()
CLOCK = pg.time.Clock()

screen = pg.display.set_mode((800,600))
pg.display.set_caption("Torres de Hanoi")

lineW = 4
colores = {
    "Fondo": "#9DFFFF",
    "Torres": "#FFD402",
    "Linea": "#6F6C37",
    "Suelo": "#D99A3B"
}
coloresDisco = ["#A5D742","#A500DF","#FC016B", "#FFA500", "#FF0000", "#00FF99", "#1111FF", "#FF00FF", "#00FFFF", "#FFFF00"]

def rectangulo(x:int, y:int, w:int, h:int, color:str, lineColor:str) -> None:
    pg.draw.rect(screen, color, (x, y, w, h), border_bottom_left_radius=lineW, border_bottom_right_radius=lineW, border_top_left_radius=lineW, border_top_right_radius=lineW)
    pg.draw.rect(screen, lineColor, (x, y, w, h), lineW, lineW, lineW, lineW, lineW, lineW)

class Disco():
    def __init__(self, x, y, w, h, index, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.position = 0
        self.index = index

        self.lastPosition = 0
        self.animation = 0

    def draw(self):
        rectangulo(self.x, self.y, self.w, self.h, self.color, colores["Linea"])

    def findmove(self, find = 0):
        if find >= 3: return False
        if find == self.position: return self.findmove(find+1)

        if N % 2 == 1 and self.index == N-1 and len(positions[2]) == 0 and find != self.lastPosition:
            self.move(2)
            return True

        if self.index == 0 and len(positions[2]) == 0 and find != self.lastPosition:
            self.move(2)
            return True

        if (len(positions[find]) == 0 or positions[find][-1] < self.index) and find != self.lastPosition:
            self.move(find)
            return True

        return self.findmove(find+1)


    def move(self, position:int):
        speed = 15
        if self.y >= lineW and self.animation == 0: self.y -= speed; return False

        self.animation = 1
        posX = 40+250*position + (60//N)*positions[self.position][-1]
        if self.x < posX-5 or self.x > posX+5:
            if self.x < posX: self.x += speed
            else: self.x -= speed
            return False
        if self.x !=  posX: self.x = posX

        downH = len(positions[position])*(self.h-lineW)
        if self.y <= 515-self.h - downH + lineW:
            self.y += speed
            return False
        if self.y != 515-self.h - downH + lineW: self.y = 515-self.h - downH + lineW
        self.animation = 0
        
        positions[position].append(positions[self.position].pop())
        self.lastPosition = self.position
        self.position = position
        return True

discos:list[Disco] = []
positions = [[],[],[]]

for i in range(N):
    h = 260//N
    disco = Disco(40 + (60//N)*i, 515 - (h-lineW)*(i+1), 220-(60//N)*i*2, h, i, coloresDisco[i] if len(coloresDisco) > i else "#FFFFFF")
    discos.append(disco)
    positions[0].append(i)

focus = False

while True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.ACTIVEEVENT and event.gain:
            focus = True

    screen.fill(colores["Fondo"])
    for i in range(1,4):
        rectangulo(125 + 250 * (i-1), 250, 50, 300, colores["Torres"], colores["Linea"])
    for disco in discos:
        disco.draw()
    rectangulo(-20, 515, 850, 100, colores["Suelo"], colores["Linea"])

    if focus:
        mindis = []
        for pos in positions:
            if len(pos) > 0:
                mindis.append(pos[-1])

        mindis.sort(reverse=True)

        if not discos[mindis[-1]].findmove():
            if not discos[mindis[-2]].findmove():
                discos[mindis[-3]].findmove()

        if len(positions[2]) == N:
            print("Programa terminado")
            sleep(3)
            break
    pg.display.flip()
    CLOCK.tick(60)