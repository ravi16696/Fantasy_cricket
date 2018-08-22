# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewTeam.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

class Ui_NewTeam(object):

    #-----adding team name to database-------------------

    def create_team(self):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("UPDATE checktable SET flag1=0;")
        cur.execute("DELETE FROM Team WHERE Player1='';")
        
        teamname=str(self.lineEdit_teamname.text())
        teamname=teamname.strip()
        if len(teamname)==0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()

        else:
            cur.execute("SELECT * FROM Team")
            flag=0
            record=cur.fetchall()
            for i in record:
                if i[0]==teamname:
                    flag=1
                    break

            if flag == 0:
                cur.execute("UPDATE checktable SET flag1=1;")
                cur.execute("""INSERT INTO Team VALUES (?,'','','','','','','','','','','')""", (teamname,))
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Team name created sucessfully!!!!")
                msg.setWindowTitle("Team created")
                msg.exec_()
                
                
                

            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Team name already exist.Choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
            con.commit()
            cur.close()
            con.close()
            
                    

    #--------------------------------------------------------------------

            
    def setupUi(self, NewTeam):
        NewTeam.setObjectName("NewTeam")
        NewTeam.resize(400, 300)
        self.label = QtWidgets.QLabel(NewTeam)
        self.label.setGeometry(QtCore.QRect(150, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QLabel(NewTeam)
        self.label1.setGeometry(QtCore.QRect(120, 110, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lineEdit_teamname = QtWidgets.QLineEdit(NewTeam)
        self.lineEdit_teamname.setGeometry(QtCore.QRect(100, 140, 181, 20))
        self.lineEdit_teamname.setObjectName("lineEdit_teamname")
        self.pushButton_create = QtWidgets.QPushButton(NewTeam)
        self.pushButton_create.setGeometry(QtCore.QRect(150, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")

        
        #-------------------------------------------------------
        self.pushButton_create.clicked.connect(self.create_team)
        #-------------------------------------------------------

        self.retranslateUi(NewTeam)
        QtCore.QMetaObject.connectSlotsByName(NewTeam)

    def retranslateUi(self, NewTeam):
        con=sqlite3.connect('fantasy_cricket.db')
        cur=con.cursor()
        cur.execute("UPDATE checktable SET flag1=0;")
        cur.execute("DELETE FROM Team WHERE Player1='';")
        con.commit()
        
        _translate = QtCore.QCoreApplication.translate
        NewTeam.setWindowTitle(_translate("NewTeam", "Create Team"))
        self.label.setText(_translate("NewTeam", "New Team"))
        self.label1.setText(_translate("NewTeam", "Enter the team name"))
        self.pushButton_create.setText(_translate("NewTeam", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTeam = QtWidgets.QDialog()
    ui = Ui_NewTeam()
    ui.setupUi(NewTeam)
    NewTeam.show()
    sys.exit(app.exec_())

