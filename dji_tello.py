from djitellopy import Tello


def example(drohne):

    #Drohne abheben
    drohne.takeoff()

    #Drohne landen
    drohne.land()

    #Drohne nach links bewegen (100cm). Du kannst einen Abstand von 20-500cm angeben.
    drohne.move_left(100)

    #Drohne nach rechts bewegen (100cm). Du kannst einen Abstand von 20-500cm angeben.
    drohne.tello.move_right(100)

    #Drohne nach vorne bewegen (100cm). Du kannst einen Abstand von 20-500cm angeben.
    drohne.tello.move_forward(100)

    #Drohne nach hinten bewegen (100cm). Du kannst einen Abstand von 20-500cm angeben.
    drohne.tello.move_back(100)

    #Drohne nach oben bewegen (100cm). Du kannst einen Abstand von 20-500cm angeben.
    drohne.tello.move_up(100)

    #Drohne nach unten bewegen (100cm). Du kannst einen Abstand von 20-500cm angeben.
    drohne.tello.move_down(100)

    #Drohne im Uhrzeigersinn (um 360 Grad) drehen. Du kannst einen Winkel von 1-360 Grad angeben.
    drohne.rotate_clockwise(360)

    #Drohne gegen den Uhrzeigersinn (um 360 Grad) drehen. Du kannst einen Winkel von 1-360 Grad angeben.
    drohne.rotate_counter_clockwise(360)

    #Drohne nach hinten flippen lassen
    drohne.flip_back()

    #Drohne nach vorne flippen lassen
    drohne.flip_forward()

    #Drohne nach links flippen lassen
    drohne.flip_left()

    #Drohne nach rechts flippen lassen
    drohne.flip_right()

    #Drohne fliegt zu den angegebenen Koordinaten. Die ersten drei Werte sind die x (vorne/hinten), y (rechts/links), z (oben/unten) Achsen.
    #Der vierte Wert ist die Geschwindigkeit. Die Achsen kannst du mit -500-500 angeben und die Geschwindigkeit mit 10-100 (Prozentanzahl)
    drohne.go_xyz_speed(100, 30, 50, 80)

    #Drohne fliegt zu den angegebenen Koordinaten nachdem sie das richtige Pad erkennt. Angaben siehe oben. Letzer Wert ist die Zahl des zu erkennenden Pads (1-8)
    drohne.go_xyz_speed_mid(100, 30, 50, 80, 3)

def action(drohne):

    #Verbinde dich mit der Drohne
    drohne.connect()

    """
    Schreibe hier deinen Code
    ----------------------------------------------------------------------------------------
    """



    #Lande die Drohne am Ende deines Code
    drohne.land()
    
    """
    Ab hier nicht mehr schreiben
    ----------------------------------------------------------------------------------------
    """



if __name__ == "__main__":

    tello = Tello()
    action(tello)
