from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from functions import update_app
from PyQt5.QtCore import QSize, Qt
import csv
import requests

class DialogWindow(QDialog):
    def __init__(self, parent=None,):
        QtWidgets.QWidget.__init__(self,parent)
        uic.loadUi("data_form.ui",self)        
        self.send_data.clicked.connect(self.send_info)
        self.close_window.clicked.connect(self.close)

    def send_info(self):
        info=update_app()
        for element in info:
            r = requests.post('http://127.0.0.1:8000/user/', data=element)
            

class Dialog2Window(QDialog):
    def __init__(self, parent=None,):
        QtWidgets.QWidget.__init__(self,parent)
        uic.loadUi("data_server.ui",self)
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
            "date":date,
            "direction":direction,
            "status":status,
            "type_passage":type_passage,
            "sync":sync,
            "photo":None,
        }
        r = requests.post('http://127.0.0.1:8000/user/', data=data)
        self.close()

class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        
        
        QtWidgets.QWidget.__init__(self,parent)
        uic.loadUi("form1.ui",self)
        self.download_csv.clicked.connect(self.download_file)
        self.send_data.clicked.connect(self.open_form)
        self.update_hab_data.clicked.connect(self.update_data)
        self.data_to_server.clicked.connect(self.open_dialog2)
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
        # заполняем первую строку
        
        for i in range(0,4):
            for j in range(0,12):
                    table.setItem(j, i, QTableWidgetItem(str(info[i][keys[j]])))

    def download_file(self):
        info= update_app() #если время переделать        
        with open('export.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, info[0].keys(), delimiter=';')
            writer.writeheader()
            for user in info:
                writer.writerow(user)

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
