import datetime
import pyglet

while True:
    currentDT = datetime.datetime.now()
    print(currentDT.strftime("%H:%M:%S"))
    h = int(currentDT.strftime("%H"))
    m = int(currentDT.strftime("%M"))
    s = int(currentDT.strftime("%S"))

    if h == 9 and m == 34  and s == 00:
        print("It's time")
        music = pyglet.resource.media("sample.wav")
        music.play()

        pyglet.app.run()

        break


