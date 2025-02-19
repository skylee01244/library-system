from PyQt6.QtCore import * 
from PyQt6.QtGui import *
from PyQt6.QtWidgets import * 
import sys
import mysql.connector

from PyQt6.uic import loadUiType

ui,_ = loadUiType('untitled.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

        self.Show_Category()
        self.Show_Author()
        self.Show_Publisher()

        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()

    
    def Handle_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)       # hide the top tab bar 

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)


        self.pushButton_14.clicked.connect(self.Add_Category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()

    #################################
    ########## OPENING TABS #########

    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)


    #################################
    ########## BOOKS ################
    def Add_New_Book(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_5.CurrentText()
        book_author = self.comboBox_6.CurrentText()
        book_publisher = self.comboBox_6.CurrentText()
        book_price = self.lineEdit_6.text()


    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass

    #################################
    ########## USERS ################

    def Add_New_User(self):
        pass

    def Login(self):
        pass

    def Edit_User(self):
        pass

    #################################
    ########## SETTINGS #############

    def Add_Category(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_21.text().strip()
        if not category_name: 
            self.lineEdit_21.setText('')
            return
        
        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''', (category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added ')
        self.lineEdit_21.setText('')
        self.Show_Category()

    def Show_Category(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)


    def Add_Author(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_22.text().strip()
        if not author_name: 
            self.lineEdit_22.setText('')
            return
        self.cur.execute('''
            INSERT INTO author (author_name) VALUES (%s)
        ''', (author_name,))

        self.db.commit()
        self.lineEdit_22.setText('')
        self.statusBar().showMessage('New Author Added ')
        self.Show_Author()

    def Show_Author(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author ''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def Add_Publisher(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_23.text().strip()
        if not publisher_name: 
            self.lineEdit_23.setText('')
            return
        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES (%s)
        ''', (publisher_name,))

        self.db.commit()
        self.lineEdit_23.setText('')
        self.statusBar().showMessage('New Publisher Added ')
        self.Show_Publisher()

    def Show_Publisher(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


    #################################
    #### SHOW SETTINGS DATA IN UI ###

    def Show_Category_Combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()

        for category in data:
            self.comboBox_5.addItem(category[0]) 

    def Show_Author_Combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author ''')
        data = self.cur.fetchall()

        for author in data:
            self.comboBox_6.addItem(author[0])

    def Show_Publisher_Combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()

        for publisher in data:
            self.comboBox_7.addItem(publisher[0])

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

