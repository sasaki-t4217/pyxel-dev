import pyxel

def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(60,50,"Hello Pyxel!",pyxel.rndi(0,7))

pyxel.init(160,120)
pyxel.run(update,draw)