from PyQt5.QtWidgets import QApplication, QInputDialog, QPushButton,QMessageBox
from notes_layout1 import *
import json



with open("notes.json", "r", encoding="utf-8") as file:
   notes = json.load(file)
notes['текст']=None
def show_note():
    t = wind.listWidget.currentItem().text()
    wind.textEdit.setText(notes[t]['текст'])
    wind.listWidget_2.clear()
    wind.listWidget_2.addItems(notes[t]['тегі'])
def add_note():
    note_name, ok = QInputDialog.getText(wind,'Додати замітку','Назва замітки')
    if note_name !="" and ok:
        notes[note_name] = {'текст': '','тегі': []}
        wind.listWidget.addItem(note_name)
def save_note():
    try:
        note_name = wind.listWidget.currentItem().text()

    except:
        print('Обери замітку!')
        return()
    
    text = wind.textEdit.toPlainText()
    notes[note_name]['текст'] = text
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file)

def del_note():
    try:
        note_name = wind.listWidget.currentItem().text()
 
    except:
        print('Обери замітку!')
        return()
    text = wind.textEdit.toPlainText()
    del notes['текст']
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file)

app = QApplication([])

#print(notes.keys())

wind = Ui_Form()
wind.setupUi(wind)
wind.show()
wind.listWidget.addItems(notes.keys())
wind.listWidget.itemClicked.connect(show_note)
wind.pushButton.clicked.connect(add_note)
wind.pushButton_3.clicked.connect(save_note)
wind.pushButton_2.clicked.connect(del_note)

app.exec_()