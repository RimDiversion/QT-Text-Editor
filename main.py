#!/usr/bin/env python3

import sys
import os
import datetime
from PyQt5 import QtWidgets, QtCore
import text_editor_ui
import gmail

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_ui = text_editor_ui.MainWindow()
        self.main_ui.setupUi(self)

        self.saved = True
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.recovery_period = 300000       # 5 Min in milleseconds
        self.recovery_depth = 20            # How many recovery files to keep
        self.file_name = "untitled"         # default file name
        self.directory = os.path.join(os.getcwd(), "files") # default directory
        self.quick_save_active = False

        # This allows you to be able to open files with the text editor
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            if filename:
                self.file_name = os.path.basename(filename).replace('.txt', '', 1)
                self.directory = os.path.dirname(filename)
                with open(filename) as file:
                    text = file.read()
                    self.main_ui.textEdit.setText(text)
                self.quick_save_active = True

        self.setWindowTitle(self.file_name)

        self.main_ui.actionBold.triggered.connect(self.toggle_bold)
        self.main_ui.actionItalics.triggered.connect(self.toggle_italic)
        self.main_ui.actionUnderline.triggered.connect(self.toggle_underline)
        self.main_ui.actionStrikeOut.triggered.connect(self.toggle_strikeOut)
        self.main_ui.actionSave.triggered.connect(self.save)
        self.main_ui.actionSaveAs.triggered.connect(self.save_as)
        self.main_ui.actionSaveAsPlainText.triggered.connect(self.save_as_plain_text)
        self.main_ui.actionOpen.triggered.connect(self.confirm_open)
        self.main_ui.actionQuit.triggered.connect(self.quit_win)
        self.main_ui.actionNew.triggered.connect(self.new)
        self.main_ui.actionGmail.triggered.connect(self.send_email)
        self.main_ui.buttonBox.accepted.connect(self.save_quit)
        self.main_ui.buttonBox.rejected.connect(sys.exit)
        self.main_ui.buttonBox_2.accepted.connect(self.save)
        self.main_ui.buttonBox_2.rejected.connect(self.open)
        self.main_ui.bold_button.clicked.connect(self.toggle_bold)
        self.main_ui.italic_button.clicked.connect(self.toggle_italic)
        self.main_ui.underline_button.clicked.connect(self.toggle_underline)
        self.main_ui.alignment_combo_box.activated.connect(self.icon_align)
        self.main_ui.actionLeft.triggered.connect(lambda: self.align(QtCore.Qt.AlignLeft))
        self.main_ui.actionCenter.triggered.connect(lambda: self.align(QtCore.Qt.AlignCenter))
        self.main_ui.actionRight.triggered.connect(lambda: self.align(QtCore.Qt.AlignRight))
        self.main_ui.font_size_box.valueChanged.connect(self.font_size)
        self.main_ui.font_combo_box.activated.connect(self.set_font)
        self.main_ui.textEdit.textChanged.connect(self.start_timer)
        self.main_ui.textEdit.cursorPositionChanged.connect(self.current_font)
        self.timer.timeout.connect(self.recovery)

        self.show()

    def align(self, alignment):
        self.main_ui.textEdit.setAlignment(alignment)
        self.main_ui.textEdit.setFocus()

    def cancel(self):
        self.main_ui.confirm_dialog.hide()
        self.main_ui.confirm_dialog_2.hide()

    def closeEvent(self, event):
        self.quit_win()
        event.ignore()

    def confirm_open(self):
        if not self.saved:
            self.main_ui.confirm_dialog_2.show()
        else:
            self.open()

    def current_font(self):
        font = self.main_ui.textEdit.currentFont()
        self.main_ui.font_combo_box.setCurrentText(font.family())
        self.main_ui.font_size_box.setProperty("value", font.pointSize())
        self.main_ui.actionBold.setChecked(font.bold())
        self.main_ui.actionItalics.setChecked(font.italic())
        self.main_ui.actionUnderline.setChecked(font.underline())
        self.main_ui.actionStrikeOut.setChecked(font.strikeOut())
        self.main_ui.bold_button.setChecked(font.bold())
        self.main_ui.italic_button.setChecked(font.italic())
        self.main_ui.underline_button.setChecked(font.underline())
        if self.main_ui.textEdit.alignment() == QtCore.Qt.AlignLeft:
            index = 0
        elif self.main_ui.textEdit.alignment() == QtCore.Qt.AlignCenter:
            index = 1
        elif self.main_ui.textEdit.alignment() == QtCore.Qt.AlignRight:
            index = 2
        self.main_ui.alignment_combo_box.setCurrentIndex(index)

    def font_size(self):
        font = self.main_ui.textEdit.font()
        font.setPointSize(self.main_ui.font_size_box.value())
        self.main_ui.textEdit.setCurrentFont(font)

    def send_email(self):
        gmail.send_email(self.windowTitle(), self.main_ui.textEdit.toPlainText())

    def icon_align(self):
        alignment = self.main_ui.alignment_combo_box.currentText()
        if alignment == "Left":
            self.align(QtCore.Qt.AlignLeft)
        elif alignment == "Center":
            self.align(QtCore.Qt.AlignCenter)
        elif alignment == "Right":
            self.align(QtCore.Qt.AlignRight)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter and self.main_ui.font_size_box.hasFocus():
            self.main_ui.textEdit.setFocus()

    def new(self):
        if not self.saved:
            self.main_ui.confirm_dialog_2.show()
        self.hide()
        Main()

    def open(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.main_ui.centralwidget,
            "Open:",
            f"{self.directory}",
             )
        if filename:
            self.file_name = os.path.basename(filename).replace('.txt', '', 1)
            self.directory = os.path.dirname(filename)
            self.setWindowTitle(self.file_name)
            with open(filename) as file:
                text = file.read()
                self.main_ui.textEdit.setText(text)
            self.quick_save_active = True
            self.saved = True
            self.stop_timer()
        self.cancel()

    def quit(self):
        sys.exit()

    def quit_win(self):
        if not self.saved:
            self.main_ui.confirm_dialog.show()
        else:
            sys.exit()

    def recovery(self):    
        name = datetime.datetime.now().strftime("%H.%M.%S.%m.%d.%Y.txt")
        filename =  os.path.join(os.getcwd(),"recovery", name)  
        with open(filename, "w") as file:
            file.write(self.main_ui.textEdit.toHtml())
            if len(os.listdir(os.path.join(os.getcwd(),"recovery"))) > self.recovery_depth:
                os.remove(os.path.join(os.getcwd(), 
                "recovery", 
                (os.listdir(os.path.dirname(filename))[0])))

    def save(self):
        if not self.quick_save_active:
            self.save_as()
        else:
            filename = f"{self.directory}/{self.file_name}.txt"
            with open(filename, "w") as file:
                file.write(self.main_ui.textEdit.toHtml())
        self.stop_timer()
        self.saved = True

    def save_as(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.main_ui.centralwidget,
            "Save as:", 
            f"{self.directory}/{self.file_name}",
            "Text files (*.txt)")
        if filename:
            self.file_name = os.path.basename(filename).replace('.txt', '', 1)
            self.directory = os.path.dirname(filename)
            self.setWindowTitle(self.file_name)
            with open(filename, "w") as file:
                file.write(self.main_ui.textEdit.toHtml())
            self.quick_save_active = True
            self.stop_timer()
        self.saved = True

    def save_as_plain_text(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.main_ui.centralwidget,
            "Save as:", 
            f"{self.directory}/{self.file_name}",
            "Text files (*.txt)")
        if filename:
            self.file_name = os.path.basename(filename).replace('.txt', '', 1)
            self.directory = os.path.dirname(filename)
            self.setWindowTitle(self.file_name)
            with open(filename, "w") as file:
                file.write(self.main_ui.textEdit.toPlainText())
            self.quick_save_active = True
            self.stop_timer()
        self.saved = True

    def save_quit(self):
        self.save()
        sys.exit()

    def set_font(self):
        """Sets current font keeping other atributes"""
        family = self.main_ui.font_combo_box.currentText()
        self.main_ui.font.setFamily(family) 
        self.main_ui.font.setPointSize(self.main_ui.font_size_box.value())     # fonts have default sizes attached and this overides that
        self.main_ui.textEdit.setCurrentFont(self.main_ui.font)
        self.main_ui.textEdit.setFocus()
    
    def start_timer(self):
        self.saved = False
        if not self.timer.isActive():
            self.timer.start(self.recovery_period)
    
    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()
  
    def toggle_bold(self):
        """Switches the bold state and updates ui"""

        font = self.main_ui.textEdit.currentFont()
        state = not font.bold()
        font.setBold(state)
        self.main_ui.textEdit.setCurrentFont(font)
        self.main_ui.textEdit.setFocus()

    def toggle_italic(self):
        """Switches the italic state and updates ui"""
        
        font = self.main_ui.textEdit.currentFont()
        state = not font.italic()
        font.setItalic(state)
        self.main_ui.textEdit.setCurrentFont(font)
        self.main_ui.textEdit.setFocus()

    def toggle_underline(self):
        """Switches the underline state and updates ui"""
        
        font = self.main_ui.textEdit.currentFont()
        state = not font.underline()
        font.setUnderline(state)
        self.main_ui.textEdit.setCurrentFont(font)
        self.main_ui.textEdit.setFocus()

    def toggle_strikeOut(self):
        """Switches the strikeout state and updates ui"""
        
        font = self.main_ui.textEdit.currentFont()
        state = not font.strikeOut()
        font.setStrikeOut(state)
        self.main_ui.textEdit.setCurrentFont(font)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)   
    win = Main()
    sys.exit(app.exec_())  
