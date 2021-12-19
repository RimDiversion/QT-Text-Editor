#!/usr/bin/env python3

import text_editor_ui
import gmail
import sys
from PyQt5 import QtWidgets, QtCore
import os
import datetime

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = text_editor_ui.MainWindow()
        self.ui.setupUi(self)

        self.saved = True
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)       
        self.recovery_period = 300000       # 5 Min in milleseconds
        self.recovery_depth = 20            # How many recovery files to keep
        self.file_name = "untitled"         # default file name
        self.directory = os.path.join(os.getcwd(), "files") # default directory
        self.quick_save_active = False        

        if len(sys.argv) == 2:
            filename = sys.argv[1]
            if filename:
                self.file_name = os.path.basename(filename).replace('.txt', '', 1)
                self.directory = os.path.dirname(filename)
                with open(filename) as file:
                    text = file.read()
                    self.ui.textEdit.setText(text)
                self.quick_save_active = True

        self.setWindowTitle(self.file_name)

        self.ui.actionBold.triggered.connect(self.toggle_bold)
        self.ui.actionItalics.triggered.connect(self.toggle_italic)
        self.ui.actionUnderline.triggered.connect(self.toggle_underline)
        self.ui.actionStrikeOut.triggered.connect(self.toggle_strikeOut)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSaveAs.triggered.connect(self.save_as)
        self.ui.actionSaveAsPlainText.triggered.connect(self.save_as_plain_text)
        self.ui.actionOpen.triggered.connect(self.confirm_open)
        self.ui.actionQuit.triggered.connect(self.quit_win)
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionGmail.triggered.connect(self.send_email)
        self.ui.buttonBox.accepted.connect(self.save_quit)
        self.ui.buttonBox.rejected.connect(self.quit)
        self.ui.buttonBox_2.accepted.connect(self.save)
        self.ui.buttonBox_2.rejected.connect(self.open)
        self.ui.bold_button.clicked.connect(self.toggle_bold)
        self.ui.italic_button.clicked.connect(self.toggle_italic)
        self.ui.underline_button.clicked.connect(self.toggle_underline)
        self.ui.alignment_combo_box.activated.connect(self.icon_align)
        self.ui.actionLeft.triggered.connect(lambda: self.align(QtCore.Qt.AlignLeft))
        self.ui.actionCenter.triggered.connect(lambda: self.align(QtCore.Qt.AlignCenter))
        self.ui.actionRight.triggered.connect(lambda: self.align(QtCore.Qt.AlignRight))
        self.ui.font_size_box.valueChanged.connect(self.font_size)
        self.ui.font_combo_box.activated.connect(self.set_font)
        self.ui.textEdit.textChanged.connect(self.start_timer)
        self.ui.textEdit.cursorPositionChanged.connect(self.current_font)
        self.timer.timeout.connect(self.recovery)
      
        self.show()

    def align(self, alignment):
        self.ui.textEdit.setAlignment(alignment)
        self.ui.textEdit.setFocus()
    
    def cancel(self):
        self.ui.confirm_dialog.hide()
        self.ui.confirm_dialog_2.hide() 

    def closeEvent(self, event):
        self.quit_win()
        event.ignore()

    def confirm_open(self):
        if not self.saved:
            self.ui.confirm_dialog_2.show()
        else:
            self.open()

    def current_font(self):
        font = self.ui.textEdit.currentFont()
        self.ui.font_combo_box.setCurrentText(font.family())
        self.ui.font_size_box.setProperty("value", font.pointSize())
        self.ui.actionBold.setChecked(font.bold())
        self.ui.actionItalics.setChecked(font.italic())
        self.ui.actionUnderline.setChecked(font.underline())
        self.ui.actionStrikeOut.setChecked(font.strikeOut())
        self.ui.bold_button.setChecked(font.bold())
        self.ui.italic_button.setChecked(font.italic())
        self.ui.underline_button.setChecked(font.underline())
        if self.ui.textEdit.alignment() == QtCore.Qt.AlignLeft:
            index = 0
        elif self.ui.textEdit.alignment() == QtCore.Qt.AlignCenter:
            index = 1
        elif self.ui.textEdit.alignment() == QtCore.Qt.AlignRight:
            index = 2     
        self.ui.alignment_combo_box.setCurrentIndex(index)

    def font_size(self):
        font = self.ui.textEdit.font()
        font.setPointSize(self.ui.font_size_box.value())
        self.ui.textEdit.setCurrentFont(font)   

    
    def send_email(self):
        gmail.send_email('machine.rim@gmail.com', self.windowTitle(), self.ui.textEdit.toPlainText())
       
        
    def icon_align(self):
        alignment = self.ui.alignment_combo_box.currentText()
        if alignment == "Left":
            self.align(QtCore.Qt.AlignLeft)
        elif alignment == "Center":
            self.align(QtCore.Qt.AlignCenter)
        elif alignment == "Right": 
            self.align(QtCore.Qt.AlignRight)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter and self.ui.font_size_box.hasFocus():
            self.ui.textEdit.setFocus()

    def new(self):
        if not self.saved:
            self.ui.confirm_dialog_2.show()
        self.hide()
        Main()

    def open(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.ui.centralwidget,
            "Open:",
            f"{self.directory}",
            #"Text files (*.txt)",
             )
        if filename:
            self.file_name = os.path.basename(filename).replace('.txt', '', 1)
            self.directory = os.path.dirname(filename)
            self.setWindowTitle(self.file_name)
            with open(filename) as file:
                text = file.read()
                self.ui.textEdit.setText(text)
            self.quick_save_active = True
            self.saved = True
            self.stop_timer()
        self.cancel()

    def quit(self):
        sys.exit()

    def quit_win(self):
        if not self.saved:
            self.ui.confirm_dialog.show()
        else:
            self.quit()       

    def recovery(self):    
        name = datetime.datetime.now().strftime("%H.%M.%S.%m.%d.%Y.txt")
        filename =  os.path.join(os.getcwd(),"recovery", name)  
        with open(filename, "w") as file:
            file.write(self.ui.textEdit.toHtml())
            if len(os.listdir(os.path.join(os.getcwd(),"recovery"))) > self.recovery_depth:
                os.remove(os.path.join(os.getcwd(), 
                "recovery", 
                (os.listdir(os.path.dirname(filename))[0])))

    def refocus(self):
        self.ui.textEdit.setFocus()

    def save(self):
        if not self.quick_save_active:
            self.save_as()
        else:
            filename = f"{self.directory}/{self.file_name}.txt"
            with open(filename, "w") as file:
                file.write(self.ui.textEdit.toHtml())
        self.stop_timer()
        self.saved = True
    
    def save_as(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,
            "Save as:", 
            f"{self.directory}/{self.file_name}",
            "Text files (*.txt)")
        if filename:
            self.file_name = os.path.basename(filename).replace('.txt', '', 1)
            self.directory = os.path.dirname(filename)
            self.setWindowTitle(self.file_name)
            with open(filename, "w") as file:
                file.write(self.ui.textEdit.toHtml())
            self.quick_save_active = True
            self.stop_timer()
        self.saved = True

    def save_as_plain_text(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,
            "Save as:", 
            f"{self.directory}/{self.file_name}",
            "Text files (*.txt)")
        if filename:
            self.file_name = os.path.basename(filename).replace('.txt', '', 1)
            self.directory = os.path.dirname(filename)
            self.setWindowTitle(self.file_name)
            with open(filename, "w") as file:
                file.write(self.ui.textEdit.toPlainText())
            self.quick_save_active = True
            self.stop_timer()
        self.saved = True

    def save_quit(self):          
        self.save()
        self.quit()

    def set_font(self):
        family = self.ui.font_combo_box.currentText()
        self.ui.font.setFamily(family) 
        self.ui.font.setPointSize(self.ui.font_size_box.value())     # fonts have default sizes attached and this overides that
        self.ui.textEdit.setCurrentFont(self.ui.font)
        self.ui.textEdit.setFocus()
    
    def start_timer(self):
        self.saved = False     
        if not self.timer.isActive():
            self.timer.start(self.recovery_period)
    
    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()
  
    def toggle_bold(self):
        font = self.ui.textEdit.currentFont()
        state = False if font.bold() else True
        font.setBold(state)
        self.ui.textEdit.setCurrentFont(font)
        self.ui.textEdit.setFocus()        

    def toggle_italic(self):
        font = self.ui.textEdit.currentFont()
        state = False if font.italic() else True
        font.setItalic(state)
        self.ui.textEdit.setCurrentFont(font)
        self.ui.textEdit.setFocus()

    def toggle_underline(self):
        font = self.ui.textEdit.currentFont()
        state = False if font.underline() else True
        font.setUnderline(state)
        self.ui.textEdit.setCurrentFont(font)
        self.ui.textEdit.setFocus()

    def toggle_strikeOut(self):
        font = self.ui.textEdit.currentFont()
        state = False if font.strikeOut() else True
        font.setStrikeOut(state)
        self.ui.textEdit.setCurrentFont(font)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)   
    win = Main()
    sys.exit(app.exec_())  
