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
        self.pushButton_9.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)

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
        book_description = self.textEdit.toPlainText() 
        book_code = self.lineEdit_5.text()
        book_category = self.comboBox_5.currentIndex()
        book_author = self.comboBox_6.currentIndex()
        book_publisher = self.comboBox_7.currentIndex()
        book_price = self.lineEdit_6.text()

        self.cur.execute(''' 
            INSERT INTO book(book_name, book_description, book_code, book_category, book_author, book_publisher, book_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''' ,(book_title, book_description, book_code, book_category, book_author, book_publisher, book_price))
        self.db.commit()
        self.statusBar().showMessage('New Book Added')
        
        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_5.setText('')
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.lineEdit_6.setText('')
        
        
    def Search_Books(self):
        book_title = self.lineEdit_3.text()
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()
        
        sql =  ''' SELECT * FROM book WHERE book_name = %s'''
        self.cur.execute(sql, [(book_title)])
        
        data = self.cur.fetchone()
        # print(data)
        self.lineEdit_10.setText(data[1])           # title
        self.textEdit_2.setPlainText(data[2])       # description
        self.lineEdit_9.setText(data[3])            # code
        self.comboBox_8.setCurrentIndex(data[4])    # category
        self.comboBox_9.setCurrentIndex(data[5])    # author
        self.comboBox_10.setCurrentIndex(data[6])   # publisher
        self.lineEdit_7.setText(str(data[7]))       # price
        
        
        

    def Edit_Books(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()
        
        book_title = self.lineEdit_10.text()                # title
        book_description = self.textEdit_2.toPlainText()    # description
        book_code = self.lineEdit_9.text()                  # code
        book_category = self.comboBox_8.currentIndex()      # category
        book_author = self.comboBox_9.currentIndex()        # author
        book_publisher = self.comboBox_10.currentIndex()    # publisher
        book_price = self.lineEdit_7.text()                 # price
        
        search_book_title = self.lineEdit_3.text()
        
        self.cur.execute('''
            UPDATE book SET book_name=%s ,book_description=%s ,book_code=%s ,book_category=%s ,book_author=%s ,book_publisher=%s ,book_price=%s WHERE book_name=%s              
        ''', (book_title, book_description, book_code, book_category, book_author, book_publisher, book_price, search_book_title))
        self.db.commit()
        self.statusBar().showMessage('Book Updated')
        
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
        self.Show_Category_Combobox()

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
        self.Show_Author_Combobox()

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
        self.Show_Publisher_Combobox()

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

        self.comboBox_5.clear()
        self.comboBox_8.clear()
        for category in data:
            self.comboBox_5.addItem(category[0]) 
            self.comboBox_8.addItem(category[0])

    def Show_Author_Combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author ''')
        data = self.cur.fetchall()

        self.comboBox_6.clear()
        self.comboBox_9.clear()
        for author in data:
            self.comboBox_6.addItem(author[0])
            self.comboBox_9.addItem(author[0])

    def Show_Publisher_Combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()

        self.comboBox_7.clear()
        self.comboBox_10.clear()
        for publisher in data:
            self.comboBox_7.addItem(publisher[0])
            self.comboBox_10.addItem(publisher[0])

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

