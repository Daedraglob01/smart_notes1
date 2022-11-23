from PyQt5.QtWidgets import QApplication, QInputDialog, QPushButton,QMessageBox
from notes_layout1 import *
import json

#   "Ласкаво просимо!": {
 #        "текст": "Це програма для створення заміток ...",
  #       "тегі": ["інструкція", "про програму"]
   # }
#}


#notes = {
 #       "Ласкаво просимо!": {
  #    "текст": "Це програма для створення заміток ...",
   #     "тегі": ["інструкція", "про програму"]
    #}
#}

#with open("notes.json", "w", encoding="utf-8") as file:
 #   json.dump(notes, file)

with open("notes.json", "r", encoding="utf-8") as file:
   notes = json.load(file)
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

    del notes[note_name]
    wind.listWidget.takeItem(wind.listWidget.currentRow())
    wind.listWidget_2.clear()
    wind.textEdit.clear()
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file,sort_keys=True)
def add_tag():
    try:
        note_name = wind.listWidget.currentItem().text()
    except:
        print('Обери замітку!')
        return()
    tag = wind.lineEdit.text()
    if tag:
        notes[note_name]["тегі"].append(tag)
        wind.listWidget_2.clear()
        wind.listWidget_2.addItems(notes[note_name]["тегі"])
    wind.lineEdit.clear()
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file,sort_keys=True)
def del_tag():
    try:
        tag_name = wind.listWidget_2.currentItem().text()
    except:
        print('Обери тег!')
        return()
    note_name = wind.listWidget.currentItem().text()
    notes[note_name]['тегі'].remove(tag_name)
    wind.listWidget_2.clear()
    wind.listWidget_2.addItems(notes[note_name]["тегі"])
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file,sort_keys=True)

def search_tag():
    tag = wind.lineEdit.text()
    if wind.pushButton_6.text() == "Шукати замітки по тегу" and tag:
        notes_filtered = {} # тут будуть замітки з виділеним тегом
        for note in notes:
            if tag in notes[note]["тегі"]: 
                notes_filtered[note]=notes[note]
        wind.pushButton_6.setText("Скинути пошук")
        wind.listWidget.clear()
        wind.listWidget_2.clear()
        wind.listWidget.addItems(notes_filtered)
    elif wind.pushButton_6.text() == "Скинути пошук":
        wind.lineEdit.clear()
        wind.listWidget.clear()
        wind.listWidget_2.clear()
        wind.listWidget.addItems(notes)
        wind.pushButton_6.setText("Шукати замітки по тегу")
    else:
        pass
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
wind.pushButton_4.clicked.connect(add_tag)
wind.pushButton_5.clicked.connect(del_tag)
wind.pushButton_6.clicked.connect(search_tag)
app.exec_()