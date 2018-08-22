# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeamEvaluation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
playerlist=[]
totalpoint=0
flag=0
class Ui_TeamEvaluation(object):

    def addallteam(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("SELECT Team_name FROM Team;")
        record=cur.fetchall()
        self.combo_team.addItem('Select Team')
        for i in record:
            self.combo_team.addItem(i[0])

    def addallmatch(self):
        self.combo_match.addItem('Select Match')
        self.combo_match.addItem('Match1')

    def addallplayer(self):
        team_name=self.combo_team.currentText()
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
            
            self.listWidget_players.addItem(record[0][i])
            playerlist.append(record[0][i])
                

    def batscore(self,t1):
        name=t1[0]
        runs=t1[1]
        balls=t1[2]
        four=t1[3]
        six=t1[4]
        bowl=t1[5]
        maiden=t1[6]
        given=t1[7]
        wickets=t1[8]
        catch=t1[9]
        stump=t1[10]
        runout=t1[11]
        
        point=0
        point=point+int(runs/2)
        if runs>=100:
            point=point+10
        elif runs>=50:
            point=point+5
        if balls>0:
            st_rate=int(runs/balls)*100
            if st_rate>100:
                point=point+4
            elif st_rate>=80:
                point=point+2
        point=point+four
        point=point+(2*six)

        

        point=point+(10*wickets)
        if wickets>=5:
            point=point+10
        elif wickets>=3:
            point=point+5
        over=int(bowl/6)
        if over>0:
            ec_rate=float(given/over)
            if ec_rate<2:
                point=point+10
            elif ec_rate<3.5:
                point=point+7
            elif ec_rate<=4.5:
                point=point+4
        point=point+(10*catch)
        point=point+(10*stump)
        point=point+(10*runout)
        return point

    def addplayerpoint(self):
        global totalpoint
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        for playername in playerlist:
            cur.execute("SELECT * FROM Match1 WHERE Player='"+playername+"';")
            record=cur.fetchall()
            point=self.batscore(record[0])
            totalpoint=totalpoint+point
            self.listWidget_points.addItem(str(point))

        self.label_4.setText(str(totalpoint))
    def chkbutton(self):
        teamindex=self.combo_team.currentIndex()
        matchindex=self.combo_match.currentIndex()
        if teamindex==0 or matchindex==0:
            return False
        else:
            return True
        

    def showevaluation(self):
        if self.chkbutton()==False:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("First choose Team and match")
            msg.setWindowTitle("Invalid choice")
            msg.exec_()
        else:
                
            
            
            self.initialize()
            global flag
            self.addallplayer()
            if flag==0:
                self.addplayerpoint()

    def initialize(self):
        global totalpoint
        global flag
        flag=0
        totalpoint=0
        playerlist.clear()
        self.listWidget_points.clear()
        self.listWidget_players.clear()
        
        
        
        
        
            
            
        
        
        
    def setupUi(self, TeamEvaluation):
        TeamEvaluation.setObjectName("TeamEvaluation")
        TeamEvaluation.resize(622, 449)
        self.label = QtWidgets.QLabel(TeamEvaluation)
        self.label.setGeometry(QtCore.QRect(160, 30, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.combo_team = QtWidgets.QComboBox(TeamEvaluation)
        self.combo_team.setGeometry(QtCore.QRect(110, 80, 131, 22))
        self.combo_team.setAutoFillBackground(False)
        self.combo_team.setEditable(False)
        self.combo_team.setObjectName("combo_team")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(20)
        self.combo_team.setFont(font)
        self.combo_match = QtWidgets.QComboBox(TeamEvaluation)
        self.combo_match.setGeometry(QtCore.QRect(380, 80, 121, 22))
        self.combo_match.setObjectName("combo_match")
        self.combo_match.setFont(font)
        self.line = QtWidgets.QFrame(TeamEvaluation)
        self.line.setGeometry(QtCore.QRect(60, 120, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget_players = QtWidgets.QListWidget(TeamEvaluation)
        self.listWidget_players.setGeometry(QtCore.QRect(60, 170, 211, 231))
        self.listWidget_players.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_players.setObjectName("listWidget_players")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_players.setFont(font)
        self.listWidget_players.setStyleSheet("color: rgb(3, 190, 159);")
        self.listWidget_points = QtWidgets.QListWidget(TeamEvaluation)
        self.listWidget_points.setGeometry(QtCore.QRect(370, 170, 201, 231))
        self.listWidget_points.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_points.setObjectName("listWidget_points")
        self.listWidget_points.setFont(font)
        self.listWidget_points.setStyleSheet("color: rgb(3, 190, 159);")
        self.label1 = QtWidgets.QLabel(TeamEvaluation)
        self.label1.setGeometry(QtCore.QRect(70, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(TeamEvaluation)
        self.label2.setGeometry(QtCore.QRect(380, 140, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label_4 = QtWidgets.QLabel(TeamEvaluation)
        self.label_4.setGeometry(QtCore.QRect(440, 140, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(7, 200, 168);")
        self.label_4.setObjectName("label_4")
        self.pushButton_evaluate = QtWidgets.QPushButton(TeamEvaluation)
        self.pushButton_evaluate.setGeometry(QtCore.QRect(280, 410, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_evaluate.setFont(font)
        self.pushButton_evaluate.setObjectName("pushButton_evaluate")
        #-------------------------------------------
        self.pushButton_evaluate.clicked.connect(self.showevaluation)

        self.retranslateUi(TeamEvaluation)
        QtCore.QMetaObject.connectSlotsByName(TeamEvaluation)
        #-----------------------------------------------
        self.addallteam()
        self.addallmatch()

    def retranslateUi(self, TeamEvaluation):
        _translate = QtCore.QCoreApplication.translate
        TeamEvaluation.setWindowTitle(_translate("TeamEvaluation", "Team Evaluation"))
        self.label.setText(_translate("TeamEvaluation", "Enter the performance of your fantasy team"))
        self.label1.setText(_translate("TeamEvaluation", "Players"))
        self.label2.setText(_translate("TeamEvaluation", "Points:"))
        self.label_4.setText(_translate("TeamEvaluation", "####"))
        self.pushButton_evaluate.setText(_translate("TeamEvaluation", "Evaluate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeamEvaluation = QtWidgets.QDialog()
    ui = Ui_TeamEvaluation()
    ui.setupUi(TeamEvaluation)
    TeamEvaluation.show()
    sys.exit(app.exec_())

