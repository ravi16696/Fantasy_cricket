# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FantasyCricket.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NewTeam import Ui_NewTeam
from OpenTeam import Ui_OpenTeam
from TeamEvaluation import Ui_TeamEvaluation
import sqlite3
batplayers=[]
bwlplayers=[]
wkplayers=[]
arplayers=[]
teamplayers={}
batflag=0
bat1_no = 0
bwl1_no = 0
ar1_no = 0
wk1_no = 0
player_point={}
point=1000
point1=0
teamname=''

class Ui_MainWindow(object):

#opening new window-------------------

    def New_Team(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_NewTeam()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        self.toggleclickable()
#------------------------------------

    def Open_Team(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OpenTeam()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

#-------------------------------------

    def Team_Evaluation(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_TeamEvaluation()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

#---------------------------------------
#making radio button not clickable----------------
    def togglenotclickable(self):
        _translate = QtCore.QCoreApplication.translate
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_2.addItem("")
        self.listWidget_2.addItem("")
        self.radio_bat.setEnabled(False)
        self.radio_bow.setEnabled(False)
        self.radio_ar.setEnabled(False)
        self.radio_wk.setEnabled(False)
        self.label_bat.setText(_translate("MainWindow", "##"))
        self.label_bow.setText(_translate("MainWindow", "##"))
        self.label_ar.setText(_translate("MainWindow", "##"))
        self.label_wk.setText(_translate("MainWindow", "##"))
        self.label_points_availabel.setText(_translate("MainWindow", "####"))
        self.label_points_used.setText(_translate("MainWindow", "####"))

#-----------------------------------------------
    def initialize(self):
        global bat1_no
        global bwl1_no
        global ar1_no
        global wk1_no
        global point
        global point1
        global teamname
        bat1_no=0
        bwl1_no=0
        ar1_no=0
        wk1_no=0
        point=1000
        point1=0
        teamname=''
        batplayers.clear()
        bwlplayers.clear()
        wkplayers.clear()
        arplayers.clear()
        teamplayers.clear()
        player_point.clear()
    def initbat(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT Player,Value FROM Stats WHERE Ctg='BAT';")
        record=cur.fetchall()
        for i in record:
            #print(i[0])
            player_point[i[0]]=i[1]
            batplayers.append(i[0])

    def initbwl(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT Player,Value FROM Stats WHERE Ctg='BWL';")
        record=cur.fetchall()
        for i in record:
            #print(i[0])
            player_point[i[0]]=i[1]
            bwlplayers.append(i[0])

    def initar(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT Player,Value FROM Stats WHERE Ctg='AR';")
        record=cur.fetchall()
        for i in record:
            #print(i[0])
            player_point[i[0]]=i[1]
            arplayers.append(i[0])

    def initwk(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT Player,Value FROM Stats WHERE Ctg='WK';")
        record=cur.fetchall()
        for i in record:
            #print(i[0])
            player_point[i[0]]=i[1]
            wkplayers.append(i[0])
        
        #--tootle clickable----------------
        
    def toggleclickable(self):
        self.listWidget_2.clear()
        self.listWidget_2.addItem("")
        self.listWidget_2.addItem("")
        
        self.listWidget.clear()
        
        self.initialize()
        self.initbat()
        self.initbwl()
        self.initwk()
        self.initar()
        teamplayers.clear()
        _translate = QtCore.QCoreApplication.translate
        self.radio_bat.setEnabled(True)
        self.radio_bow.setEnabled(True)
        self.radio_ar.setEnabled(True)
        self.radio_wk.setEnabled(True)
        
        self.radio_bat.setChecked(True)
        self.showbat()
        
        self.label_bat.setText(_translate("MainWindow", "0"))
        self.label_bow.setText(_translate("MainWindow", "0"))
        self.label_ar.setText(_translate("MainWindow", "0"))
        self.label_wk.setText(_translate("MainWindow", "0"))
        self.label_points_availabel.setText(_translate("MainWindow", "1000"))
        self.label_points_used.setText(_translate("MainWindow", "0"))

        #-------------------------------------------
        #showing players list on toggle click--------------
    def showbat(self):
        self.listWidget.clear()
        self.listWidget.addItem("")
        self.listWidget.addItem("")
        for i in batplayers:
            self.listWidget.addItem(i.ljust(20)+str(player_point[i]))
        #-------------------------------------------------
    def showbwl(self):
        self.listWidget.clear()
        self.listWidget.addItem("")
        self.listWidget.addItem("")
        for i in bwlplayers:
            self.listWidget.addItem(i.ljust(20)+str(player_point[i]))

        #---------------------------------------------------
    def showwk(self):
        self.listWidget.clear()
        self.listWidget.addItem("")
        self.listWidget.addItem("")
        for i in wkplayers:
            self.listWidget.addItem(i.ljust(20)+str(player_point[i]))
        #--------------------------------------------------
    def showar(self):
        self.listWidget.clear()
        self.listWidget.addItem("")
        self.listWidget.addItem("")
        for i in arplayers:
            self.listWidget.addItem(i.ljust(20)+str(player_point[i]))

    #-----------------------------------------------------------
    def cutitem(self,a):
        s=''
        for i in a:
            if(i==' '):
                break
            else:  
                s=s+i
        return s
    def addplayer(self,item):
        pname=self.cutitem(item.text())
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT * FROM checktable;")
        record=cur.fetchall()
        a=record[0][1]
        if a==0:
            self.togglenotclickable()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("First create team")
            msg.setWindowTitle("Team not created")
            msg.exec_()
            return
            
        global bat1_no
        global bwl1_no
        global wk1_no
        global ar1_no
        if (pname in batplayers) == True:
            categ='BAT'
        elif (pname in bwlplayers) == True:
            categ='BWL'
        elif (pname in wkplayers) == True:
            categ='WK'
        else:
            categ='AR'
        global point1
        global point

        point1=point1+player_point[pname]
        
        if point1>1000:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Your points cannot exceed 1000")
            msg.setWindowTitle("Invalid selection")
            msg.exec_()
            point1=point1-player_point[pname]
            return
        if len(teamplayers) == 11:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You canno select more then 11 players")
            msg.setWindowTitle("Invalid selection")
            msg.exec_()
            point1=point1-player_point[pname]
            return
        if categ=='BAT' and bat1_no==5:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You canno select more then 5 batsman")
            msg.setWindowTitle("Invalid selection")
            msg.exec_()
            point1=point1-player_point[pname]
            return
        if categ=='BWL' and bwl1_no==3:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You canno select more then 3 bowleres")
            msg.setWindowTitle("Invalid selection")
            msg.exec_()
            return

        if categ=='AR' and ar1_no==3:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You canno select more then 3 all rounder")
            msg.setWindowTitle("Invalid selection")
            msg.exec_()
            point1=point1-player_point[pname]
            return
        if categ=='WK' and wk1_no>=1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You canno select more then 1 wicket-keeper")
            msg.setWindowTitle("Invalid selection")
            msg.exec_()
            point1=point1-player_point[pname]
            return
            
        
        self.listWidget.takeItem(self.listWidget.row(item))
        point=point-player_point[pname]
        self.listWidget_2.addItem(pname.ljust(20)+str(player_point[pname]))
        
        self.label_points_availabel.setText(str(point))

        
        self.label_points_used.setText(str(point1))

        
        if self.radio_bat.isChecked()==True:
            batplayers.remove(pname)
            teamplayers[pname]='BAT'
            bat1_no=bat1_no+1
            self.label_bat.setText(str(bat1_no))
            
        elif self.radio_bow.isChecked()==True:
            bwlplayers.remove(pname)
            teamplayers[pname]='BWL'
            bwl1_no=bwl1_no+1
            self.label_bow.setText(str(bwl1_no))
            
        elif self.radio_ar.isChecked()==True:
            arplayers.remove(pname)
            teamplayers[pname]='AR'
            ar1_no=ar1_no+1
            self.label_ar.setText(str(ar1_no))
            
        else:
            wkplayers.remove(pname)
            teamplayers[pname]='WK'
            wk1_no=wk1_no+1
            self.label_wk.setText(str(wk1_no))
        if point1<1000 and len(teamplayers)==11:
            if wk1_no==0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have to select atleast one wicket-keeper")
                msg.setWindowTitle("Inalid Selection")
                msg.exec_()
                return
            if ar1_no==0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have to select atleast one All rounder")
                msg.setWindowTitle("Inalid Selection")
                msg.exec_()
                return
            if bat1_no<3:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have to select atleast 3 batsman")
                msg.setWindowTitle("Inalid Selection")
                msg.exec_()
                return
            if bwl1_no<2:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have to select atleast two bowler")
                msg.setWindowTitle("Inalid Selection")
                msg.exec_()
                return
            else:
                
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You canno save your team now")
                msg.setWindowTitle("Valid Selection")
                msg.exec_()
            

    #-------------------------------------------------------------------

    def removeplayer(self,item):
        pname=self.cutitem(item.text())
        global bat1_no
        global bwl1_no
        global wk1_no
        global ar1_no
        global point
        global point1
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        point1=point1-player_point[pname]
        self.label_points_used.setText(str(point1))
        point=point+player_point[pname]
        self.label_points_availabel.setText(str(point))
        
        if teamplayers[pname]=='BAT':
            bat1_no=bat1_no-1
            batplayers.append(pname)
            if self.radio_bat.isChecked()==True:
                self.listWidget.addItem(pname.ljust(20)+str(player_point[pname]))
            self.label_bat.setText(str(bat1_no))

        elif teamplayers[pname]=='BWL':
            bwl1_no=bwl1_no-1
            bwlplayers.append(pname)
            if self.radio_bow.isChecked()==True:
                self.listWidget.addItem(pname.ljust(20)+str(player_point[pname]))
            self.label_bow.setText(str(bwl1_no))

        elif teamplayers[pname]=='AR':
            ar1_no=ar1_no-1
            arplayers.append(pname)
            if self.radio_ar.isChecked()==True:
                self.listWidget.addItem(pname.ljust(20)+str(player_point[pname]))
            self.label_ar.setText(str(ar1_no))

        else:
            wkplayers.append(pname)
            wk1_no=wk1_no-1
            if self.radio_wk.isChecked()==True:
                self.listWidget.addItem(pname.ljust(20)+str(player_point[pname]))
            self.label_wk.setText(str(wk1_no))

        del teamplayers[pname]


    def saveteam(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT * FROM checktable;")
        record=cur.fetchall()
        a=record[0][1]
        if a==0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("First create team")
            msg.setWindowTitle("Team no created")
            msg.exec_()
            self.togglenotclickable()
            return
            
        global teamplayers
        name_list=[]
        for i in teamplayers.keys():
            name_list.append(i)

        global teamname

        
        if len(teamplayers)<11:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Number of player is less than 11")
            msg.setWindowTitle("Invalid Team")
            msg.exec_()
            return
        else:
##            con=sqlite3.connect('fantasy_cricket.db')
##            cur=con.cursor()
            cur.execute("SELECT Team_name FROM Team WHERE Player1='';")
            record=cur.fetchall()
            teamname=record[0][0]
            
            sql="UPDATE Team SET Player1='"+name_list[0]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player2='"+name_list[1]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player3='"+name_list[2]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player4='"+name_list[3]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player5='"+name_list[4]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player6='"+name_list[5]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player7='"+name_list[6]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player8='"+name_list[7]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player9='"+name_list[8]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player10='"+name_list[9]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            sql="UPDATE Team SET Player11='"+name_list[10]+"' WHERE Team_name='"+teamname+"';"
            cur.execute(sql)
            con.commit()
            self. togglenotclickable()
            self.initialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Saved sucessfully")
            msg.setWindowTitle("Saving Team")
            msg.exec_()
            #self.togglenotclickable()
        
        
            
        
        
            
        
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 40, 731, 111))
        self.label_11.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_bat = QtWidgets.QLabel(self.centralwidget)
        self.label_bat.setGeometry(QtCore.QRect(160, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_bat.setFont(font)
        self.label_bat.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.label_bat.setObjectName("label_bat")
        self.label_bow = QtWidgets.QLabel(self.centralwidget)
        self.label_bow.setGeometry(QtCore.QRect(320, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_bow.setFont(font)
        self.label_bow.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.label_bow.setObjectName("label_bow")
        self.label_ar = QtWidgets.QLabel(self.centralwidget)
        self.label_ar.setGeometry(QtCore.QRect(510, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ar.setFont(font)
        self.label_ar.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.label_ar.setObjectName("label_ar")
        self.label_wk = QtWidgets.QLabel(self.centralwidget)
        self.label_wk.setGeometry(QtCore.QRect(720, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_wk.setFont(font)
        self.label_wk.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.label_wk.setObjectName("label_wk")
        self.label_points_availabel = QtWidgets.QLabel(self.centralwidget)
        self.label_points_availabel.setGeometry(QtCore.QRect(210, 210, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_points_availabel.setFont(font)
        self.label_points_availabel.setStyleSheet("color: rgb(3, 190, 159);")
        self.label_points_availabel.setObjectName("label_points_availabel")
        self.label_points_used = QtWidgets.QLabel(self.centralwidget)
        self.label_points_used.setGeometry(QtCore.QRect(550, 210, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_points_used.setFont(font)
        self.label_points_used.setStyleSheet("color: rgb(3, 190, 159);")
        self.label_points_used.setObjectName("label_points_used")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 240, 261, 311))
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color: rgb(3, 190, 159);")
        #--------------------------------------------------
        self.listWidget.itemDoubleClicked.connect(self.addplayer)
        #--------------------------------------------------
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(460, 240, 261, 311))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setStyleSheet("color: rgb(3, 190, 159);")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_2.setFont(font)
        self.listWidget_2.addItem("")
        self.listWidget_2.addItem("")
        
        #----------------------------------------------------
        self.listWidget_2.itemDoubleClicked.connect(self.removeplayer)
        #---------------------------------------------------
        self.label_team_name = QtWidgets.QLabel(self.centralwidget)
        self.label_team_name.setGeometry(QtCore.QRect(570, 250, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_team_name.setFont(font)
        self.label_team_name.setStyleSheet("color: rgb(3, 190, 159);")
        self.label_team_name.setObjectName("label_team_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(60, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(220, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(390, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(580, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(90, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label5.setFont(font)
        self.label5.setStyleSheet("")
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(460, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label6.setFont(font)
        self.label6.setStyleSheet("")
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(480, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label7.setFont(font)
        self.label7.setStyleSheet("")
        self.label7.setObjectName("label7")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(400, 370, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.radio_bat = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_bat.setEnabled(False)
        self.radio_bat.setGeometry(QtCore.QRect(100, 250, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radio_bat.setFont(font)
        self.radio_bat.setObjectName("radio_bat")
        #-------------------------------------
        self.radio_bat.toggled.connect(self.showbat)
        #--------------------------------------
        self.radio_bow = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_bow.setEnabled(False)
        self.radio_bow.setGeometry(QtCore.QRect(160, 250, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radio_bow.setFont(font)
        self.radio_bow.setObjectName("radio_bow")
        #--------------------------------------------
        self.radio_bow.toggled.connect(self.showbwl)
        #-------------------------------------------------
        self.radio_ar = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_ar.setEnabled(False)
        self.radio_ar.setGeometry(QtCore.QRect(230, 250, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radio_ar.setFont(font)
        self.radio_ar.setObjectName("radio_ar")
        #------------------------------------------------
        self.radio_ar.toggled.connect(self.showar)
        #------------------------------------------------------
        self.radio_wk = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_wk.setEnabled(False)
        self.radio_wk.setGeometry(QtCore.QRect(290, 250, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radio_wk.setFont(font)
        self.radio_wk.setObjectName("radio_wk")
        #--------------------------------------------
        self.radio_wk.toggled.connect(self.showwk)
        #---------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.menuBar.setFont(font)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("")
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.manage_teams = QtWidgets.QMenu(self.menuBar)
        self.manage_teams.setGeometry(QtCore.QRect(211, 251, 164, 138))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.manage_teams.setFont(font)
        self.manage_teams.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.manage_teams.setObjectName("manage_teams")
        MainWindow.setMenuBar(self.menuBar)
        self.new_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.new_team.setFont(font)
        self.new_team.setObjectName("new_team")
        
        #--opening new_team window------------

        self.new_team.triggered.connect(self.New_Team)
        #----------------------------------------------

        
        self.open_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_team.setFont(font)
        self.open_team.setObjectName("open_team")
        
        #-----------------
        self.open_team.triggered.connect(self.Open_Team)
        #-----------------
        
        self.save_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.save_team.setFont(font)
        self.save_team.setObjectName("save_team")
        #-----------------------------------------------
        self.save_team.triggered.connect(self.saveteam)
        #-----------------------------------------------
        self.evaluate_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.evaluate_team.setFont(font)
        self.evaluate_team.setObjectName("evaluate_team")
        
        #----------------------
        self.evaluate_team.triggered.connect(self.Team_Evaluation)
        #-----------------------------
        
        self.manage_teams.addAction(self.new_team)
        self.manage_teams.addAction(self.open_team)
        self.manage_teams.addAction(self.save_team)
        self.manage_teams.addAction(self.evaluate_team)
        self.menuBar.addAction(self.manage_teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.label_bat.setText(_translate("MainWindow", "##"))
        self.label_bow.setText(_translate("MainWindow", "##"))
        self.label_ar.setText(_translate("MainWindow", "##"))
        self.label_wk.setText(_translate("MainWindow", "##"))
        self.label_points_availabel.setText(_translate("MainWindow", "####"))
        self.label_points_used.setText(_translate("MainWindow", "####"))
        self.label_team_name.setText(_translate("MainWindow", "Displayed Here"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label1.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.label2.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label3.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label4.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label5.setText(_translate("MainWindow", "Points Available"))
        self.label6.setText(_translate("MainWindow", "Points Used"))
        self.label7.setText(_translate("MainWindow", "Team Name"))
        self.label_17.setText(_translate("MainWindow", ">"))
        self.radio_bat.setText(_translate("MainWindow", "BAT"))
        self.radio_bow.setText(_translate("MainWindow", "BOW"))
        self.radio_ar.setText(_translate("MainWindow", "AR"))
        self.radio_wk.setText(_translate("MainWindow", "WK"))
        self.manage_teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.new_team.setText(_translate("MainWindow", "NEW Team"))
        self.open_team.setText(_translate("MainWindow", "OPEN Team"))
        self.save_team.setText(_translate("MainWindow", "SAVE Team"))
        self.evaluate_team.setText(_translate("MainWindow", "EVALUATE Team"))
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("UPDATE checktable SET flag1=0;")
        cur.execute("DELETE FROM Team WHERE Player1='';")
        con.commit()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

