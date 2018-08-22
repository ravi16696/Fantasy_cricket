# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenTeam.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
playerlist=[]
flag=0
class Ui_OpenTeam(object):

    def addallteam(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT Team_name FROM Team;")
        record=cur.fetchall()
        self.comboBox_team.addItem('Select Team')
        for i in record:
            self.comboBox_team.addItem(i[0])

    def addallplayer(self):
        team_name=self.comboBox_team.currentText()
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT * FROM Team WHERE Team_name='"+team_name+"';")
        record=cur.fetchall()
        for i in range(1,12):
            if len(record[0][i].strip())==0:
                global flag
                flag=1
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have not choose player for this team")
                msg.setWindowTitle("Invalid choice")
                msg.exec_()
                return
            else:
                
                self.listWidget_player.addItem(record[0][i])
                playerlist.append(record[0][i])

    def addctgpoint(self):
        global flag
        if flag==1:
            return
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        for i in range(0,11):
            
            cur.execute("SELECT Ctg,Value FROM Stats WHERE Player='"+playerlist[i]+"';")
            record=cur.fetchall()
            self.listWidget_ctg.addItem(record[0][0])
            self.listWidget_point.addItem(str(record[0][1]))

    def initialize(self):
        global flag
        flag=0
        self.listWidget_player.clear()
        self.listWidget_ctg.clear()
        self.listWidget_point.clear()
        playerlist.clear()
        

    def addall(self):
        self.initialize()
        teamindex=self.comboBox_team.currentIndex()
        if teamindex==0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("First select team")
            msg.setWindowTitle("Invalid choice")
            msg.exec_()
            return
            
        self.addallplayer()
        self.addctgpoint()
    
    def setupUi(self, OpenTeam):
        OpenTeam.setObjectName("OpenTeam")
        OpenTeam.resize(500, 415)
        self.label = QtWidgets.QLabel(OpenTeam)
        self.label.setGeometry(QtCore.QRect(200, 20, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_open = QtWidgets.QPushButton(OpenTeam)
        self.pushButton_open.setGeometry(QtCore.QRect(210, 370, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")
        #--------------------------------------------
        self.pushButton_open.clicked.connect(self.addall)
        self.label_2 = QtWidgets.QLabel(OpenTeam)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_team = QtWidgets.QComboBox(OpenTeam)
        self.comboBox_team.setGeometry(QtCore.QRect(180, 60, 111, 22))
        self.comboBox_team.setObjectName("comboBox_team")

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(20)
        self.comboBox_team.setFont(font)
        
        self.listWidget_player = QtWidgets.QListWidget(OpenTeam)
        self.listWidget_player.setGeometry(QtCore.QRect(30, 130, 161, 211))
        self.listWidget_player.setObjectName("listWidget_player")

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_player.setFont(font)
        self.listWidget_player.setStyleSheet("color: rgb(3, 190, 159);")
        
        self.label_3 = QtWidgets.QLabel(OpenTeam)
        self.label_3.setGeometry(QtCore.QRect(240, 100, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listWidget_point = QtWidgets.QListWidget(OpenTeam)
        self.listWidget_point.setGeometry(QtCore.QRect(380, 130, 91, 211))
        self.listWidget_point.setObjectName("listWidget_point")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        
        self.listWidget_point.setFont(font)
        self.listWidget_point.setStyleSheet("color: rgb(3, 190, 159);")
        
        self.listWidget_ctg = QtWidgets.QListWidget(OpenTeam)
        self.listWidget_ctg.setGeometry(QtCore.QRect(230, 130, 121, 211))
        self.listWidget_ctg.setObjectName("listWidget_ctg")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)

        self.listWidget_ctg.setFont(font)
        self.listWidget_ctg.setStyleSheet("color: rgb(3, 190, 159);")
        
        self.label_4 = QtWidgets.QLabel(OpenTeam)
        self.label_4.setGeometry(QtCore.QRect(390, 100, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(OpenTeam)
        QtCore.QMetaObject.connectSlotsByName(OpenTeam)
        #-------------------------------------
        self.addallteam()

    def retranslateUi(self, OpenTeam):
        _translate = QtCore.QCoreApplication.translate
        OpenTeam.setWindowTitle(_translate("OpenTeam", "Open Team"))
        self.label.setText(_translate("OpenTeam", "Open Team"))
        self.pushButton_open.setText(_translate("OpenTeam", "Open"))
        self.label_2.setText(_translate("OpenTeam", "Players"))
        self.label_3.setText(_translate("OpenTeam", "Category"))
        self.label_4.setText(_translate("OpenTeam", "Point"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenTeam = QtWidgets.QDialog()
    ui = Ui_OpenTeam()
    ui.setupUi(OpenTeam)
    OpenTeam.show()
    sys.exit(app.exec_())

