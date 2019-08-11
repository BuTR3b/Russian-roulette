# max level 7

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import playsound
from random import randint
from os import system

level = 0

def chargeGun(level):
	pistolDrum = [0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(0, level):
		pistolDrum[i] = 1
	# print(pistolDrum)
	return pistolDrum

def lose():
	system(" shutdown /s /t 5 /c \" Вы проиграли\" ")
	# print("LOSE\n")

def spinDrumAndShot(drum, level):
	Vince = 13
	shot = randint(0, 7)
	# print("Bullet in ", shot + 1)
	if (drum[shot] == 1):
		return False
	elif ((drum[shot] == 0) and level < 7):
		return True
	elif ((drum[shot] == 0) and level == 7):
		return Vince

def mainGame():
	global level
	level += 1
	alive = True
	if ((level <= 7) and (alive)):
		game = spinDrumAndShot(chargeGun(level), level)
		if (game == True):
			soundNotShot()
		elif (game == 13):
			soundNotShot()
			win()
		else:
			soundShot()
			lose()
			alive = False

def twoFunc():
	soundSpin()
	mainGame()

def win():  
    messagebox.showinfo('', "Вы выиграли")

def soundSpin():
	playsound.playsound("spin.mp3", False)

def soundShot():
	playsound.playsound("shot.mp3", True)

def soundNotShot():
	playsound.playsound("notshot.mp3", True)


class mainWindow(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background = "#FFF0F5")   
		self.parent = parent
		self.initUI()
		self.drawGun()
		self.drawDrum()
		self.drawShot()
		self.showLevel()

	def initUI(self):
		self.parent.title("Русская рулетка")
		winX = 250
		winY = 350
		scrnX = int((self.parent.winfo_screenwidth() - winX) / 2)
		scrnY = int((self.parent.winfo_screenheight() - winY) / 2)
		self.parent.geometry("{}x{}+{}+{}".format(winX, winY, scrnX, scrnY))
		self.parent.resizable(False, False)
		self.pack(fill = BOTH, expand = 0)

	def drawGun(self):
		self.gunImage = ImageTk.PhotoImage(Image.open("gun.png"))
		self.myLabel = Label(image = self.gunImage)
		self.myLabel.pack()
		
	def drawDrum(self):
		self.drumImage = ImageTk.PhotoImage(Image.open("drum.png"))
		self.drumButton = Button(self.parent, bd = 0, image = self.drumImage, 
			command = lambda: playsound.playsound("spin.mp3", False))
		self.drumButton.place(x = 10, y = 180)
		self.caption = Label(self.parent, bd = 0, text = "крутить",
			padx = 0, pady = 0, font = ("Helvetica", 14, "bold"))
		self.caption.place(x = 20, y = 272)

	def drawShot(self):
		self.shotImage = ImageTk.PhotoImage(Image.open("shot.png"))
		self.shotButton = Button(self.parent, bd = 0, image = self.shotImage, 
			command = mainGame)
		self.shotButton.place(x = 155, y = 180)
		self.caption = Label(self.parent, bd = 0, text = "нажать",
			padx = 0, pady = 0, font = ("Helvetica", 14, "bold"))
		self.caption.place(x = 170, y = 272)
		
	def showLevel(self):
		global level
		levelText = "Уровень: {} (не обновляется)".format(level + 1) #как наладить?
		self.levelCaption = Label(self.parent, text = levelText, font = ("Helvetica", 10, "bold"))
		# self.levelCaption.configure(text = levelText)
		self.levelCaption.pack(side = BOTTOM)


def main():
	root = Tk()
	app = mainWindow(root)
	root.mainloop()

if __name__ == '__main__':
	main()
	


# опа
