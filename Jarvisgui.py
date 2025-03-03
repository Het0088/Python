from new_gui import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import jarvis
import os
import webbrowser as net
import sys
import datetime



class Mainthread(QThread):

    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        jarvis.TaskExe()
        
startexe = Mainthread()
        
        
class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.gui = Ui_Dialog()
        self.gui.setupUi(self)
        
        self.gui.pushstart.clicked.connect(self.startTask)
        self.gui.pushexit.clicked.connect(self.close)
        self.gui.pushchrome.clicked.connect(self.chrome_app)
        self.gui.pushyoutube.clicked.connect(self.youtube_app)
        self.gui.pushinstagram.clicked.connect(self.Instagram_app)
        self.gui.pushprimevideo.clicked.connect(self.primevideo_app)
        self.gui.pushstackoverflow.clicked.connect(self.stack_app)
        self.gui.pushfacebook.clicked.connect(self.facebook_app)
        
        
    def chrome_app(self):
        jarvis.Speak("Opening Chrome!")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
    def youtube_app(self):
        jarvis.Speak("Opening youtube!")
        net.open("https://www.youtube.com/")
        
        
    def facebook_app(self):
        jarvis.Speak("Opening Facebook!")
        net.open("https://www.facebook.com/")
        
    def Instagram_app(self):
        jarvis.Speak("Opening Instagram!")
        net.open("https://www.instagram.com/")
        
    def primevideo_app(self):
        jarvis.Speak("Opening Prime video")
        net.open("https://primevideo.com/")
        
    def stack_app(self):
        jarvis.Speak("Opening Stackoverflow!")
        net.open("https://www.stackoverflow.com/")
        
    def startTask(self):
        self.gui.label = QtGui.QMovie("C://GUI JARVIS//hud_lo.gif")
        self.gui.gif1.setMovie(self.gui.label)
        self.gui.label.start()
        
        self.gui.label_2 = QtGui.QMovie("C://GUI JARVIS//ExtraGui//program_load.gif")
        self.gui.gif3.setMovie(self.gui.label_2)
        self.gui.label_2.start()
        
        self.gui.label_7 = QtGui.QMovie("C://GUI JARVIS//ExtraGui//Earth_Template.gif")
        self.gui.gif4.setMovie(self.gui.label_7)
        self.gui.label_7.start()
        
        self.gui.label_8 = QtGui.QMovie("C://GUI JARVIS//ExtraGui//Hero_Template.gif")
        self.gui.gif5.setMovie(self.gui.label_8)
        self.gui.label_8.start()
        
        self.gui.label_9 = QtGui.QMovie("C://GUI JARVIS//ExtraGui//Jarvis_Gui (1).gif")
        self.gui.gif6.setMovie(self.gui.label_9)
        self.gui.label_9.start()
        
        self.gui.label_10 = QtGui.QMovie("C://GUI JARVIS//ExtraGui//B.G_Template_1.gif")
        self.gui.gif7.setMovie(self.gui.label_10)
        self.gui.label_10.start()

        # self.gui.bg1 = QtGui.QMovie("C://GUI JARVIS//B.G//Black_Template.jpg")
        # self.gui.bg1.start()
        
        self.gui.label_11 = QtGui.QMovie("C://GUI JARVIS//IuNL.gif")
        self.gui.gif9.setMovie(self.gui.label_11)
        self.gui.label_11.start()
        
        self.gui.label_12 = QtGui.QMovie("C://GUI JARVIS//ExtraGui//Jarvis_Gui (2).gif")
        self.gui.gif10.setMovie(self.gui.label_12)
        self.gui.label_12.start()
        
        # Timer = QTimer(self)
        # Timer.timeout.connect(self.showTimeLive)
        # Timer.start(999)
        # startexe.start()
        
    # def showTimeLive(self):
    #     t_ime = QTime.currentTime()
    #     time =t_ime.toString()    
    #     D_ate = QDate.currentDate()
    #     date = D_ate.toString()
    #     label_time = "Time  :" + time
    #     label_date = "Date  :" + date
        
    #     self.gui.Text_time.setText(label_time)
    #     self.gui.Text_date.setText(label_date)
        
        
        
        

GuiAAApp = QApplication(sys.argv)
Jarvis_hi = Gui_start()
Jarvis_hi.show()
exit(GuiAAApp.exec_())






    