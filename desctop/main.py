from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from functions import update_app, get_info_server
from PyQt5.QtCore import  Qt
import csv
import requests
from config import URL_SERVER

class DialogWindow(QDialog):
    def __init__(self, parent=None,):
        QtWidgets.QWidget.__init__(self,parent)
        uic.loadUi("ui_files/data_form.ui",self)        
        self.send_data.clicked.connect(self.send_info)
        self.close_window.clicked.connect(self.close)

    def send_info(self):
        info=update_app()
        for element in info:
            r = requests.post(URL_SERVER, data=element)
        self.close()   

class Dialog2Window(QDialog):
    def __init__(self, parent=None,):
        QtWidgets.QWidget.__init__(self,parent)
        uic.loadUi("ui_files/data_server.ui",self)
        self.close_window.clicked.connect(self.close)        
        self.send_data_2.clicked.connect(self.send_info)
    
    def send_info(self):
        name=self.name.toPlainText()
        surname=self.surname.toPlainText()
        uuid=self.surname.toPlainText()
        plate_number=self.plate_number.toPlainText()
        group=self.group.currentText()
        date=self.date.dateTime()
        direction=self.direction.toPlainText()
        status=self.status.currentText()
        type_passage=self.type_passage.currentText()
        sync=self.sync.currentText()
       
        data={
            "name": name,
            "surname":surname,
            "uuid":uuid,
            "plate_number":plate_number,
            "group":group,
            "date":date.toPyDateTime(),
            "direction":direction,
            "status":status,
            "type_passage":type_passage,
            "sync":sync,
            "photo":None,
        }
        
        r = requests.post(URL_SERVER, data=data)
        self.close()

class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
    
        QtWidgets.QWidget.__init__(self,parent)
        uic.loadUi("ui_files/form.ui",self)
        self.download_csv.clicked.connect(self.download_file)
        self.send_data.clicked.connect(self.open_form)
        self.update_hab_data.clicked.connect(self.update_data)
        self.data_to_server.clicked.connect(self.open_dialog2)
        self.get_data_from_server.clicked.connect(self.get_data)
        self.update_data()
                    
    def update_data(self):
        info=update_app()
        table=self.tableWidget
        table.setColumnCount(len(info))     # Устанавливаем  колонки
        table.setRowCount(len(info[0]))  #Устанавливаем строки
        user_list=list()
        for i in range (1,len(info)+1):
            user_list.append("User "+str(i))
        table.setHorizontalHeaderLabels(user_list)
        table.setVerticalHeaderLabels(info[0].keys())
        # Устанавливаем выравнивание на заголовки
        for i in range (0,len(info)):
            table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
        keys = list(info[0].keys())
        # заполняем строки
        
        for i in range(0,len(info)):
            for j in range(0,len(info[0])):
                    table.setItem(j, i, QTableWidgetItem(str(info[i][keys[j]])))

    def download_file(self):
        info= update_app()       
        with open('export.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, info[0].keys(), delimiter=';')
            writer.writeheader()
            for user in info:
                writer.writerow(user)
    def get_data(self):
        info=get_info_server()
        table=self.tableWidget
        table.setColumnCount(len(info))     # Устанавливаем  колонки
        table.setRowCount(len(info[0]))  #Устанавливаем строки
        user_list=list()
        for i in range (1,len(info)+1):
            user_list.append("User "+str(i))
        table.setHorizontalHeaderLabels(user_list)
        table.setVerticalHeaderLabels(info[0].keys())
        # Устанавливаем выравнивание на заголовки
        for i in range (0,len(info)):
            table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
        keys = list(info[0].keys())
        # заполняем строки
        
        for i in range(0,len(info)):
            for j in range(0,len(info[0])):
                    table.setItem(j, i, QTableWidgetItem(str(info[i][keys[j]])))




    def open_form(self):
        window= DialogWindow()    
        window.show()
        window.exec_()

    def open_dialog2(self):
        window= Dialog2Window()    
        window.show()
        window.exec_()    

    
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())
