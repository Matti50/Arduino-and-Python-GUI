from tkinter import *
import serial
class Interface:
    def __init__(self):
        self.turned = 0
        self.root = Tk()
        self.state = StringVar(self.root)
        self.arduino = serial.Serial("/dev/ttyACM0",9600)
        self.state.set("Encender")
    def create(self):
        but = Button(self.root,textvariable=self.state,command=self.change)
        but.pack()
        self.root.mainloop()
    def change(self):
        self.turned = not self.turned
        dato = "0"
        if self.turned == 0:
            self.state.set("Encender")
            dato = '0'
        else:
            self.state.set("Apagar")
            dato = '1'
        self.arduino.write(dato.encode())
             
    def value(self):
        return self.turned    
