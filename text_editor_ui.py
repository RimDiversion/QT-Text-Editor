import os
from PyQt5 import QtCore, QtGui, QtWidgets

WIDTH = 1920
HEIGHT = 2000

class MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.resize(WIDTH, HEIGHT)
        MainWindow.setWindowTitle("MacroHardWord")
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)      


        self.palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)

        fonts = QtGui.QFontDatabase.families(QtGui.QFontDatabase())
        icon_folder = os.path.join(os.getcwd(), "icons") 
        icons = {"left" : icon_folder + r"\left.png",
            "right" : icon_folder + r"\right.png",
            "center" : icon_folder + r"\center.png",
            "bold" : icon_folder + r"\bold.png",
            "italic" : icon_folder + r"\italic.png",
            "underline" : icon_folder + r"\underline.png",}

        self.font = QtGui.QFont()
        self.font.setFamily("Courier New")
        self.font.setPointSize(12)

        dialog_font = QtGui.QFont()
        dialog_font.setFamily("Courier New")
        dialog_font.setPointSize(10)
        dialog_font.setBold(True)

        self.central_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.menubar_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.menubar_layout.setContentsMargins(0, 0, 0, 0)
        

        self.submenubar = QtWidgets.QFrame(self.centralwidget)
        self.submenubar.setPalette(self.palette)
        self.submenubar.setFrameStyle(0)
        self.submenubar.setLineWidth(0)
        self.submenubar.setStyleSheet("background-color: rgb(0, 30, 30);")
        self.central_layout.addWidget(self.submenubar)
        
        
        self.textEdit = QtWidgets.QTextBrowser(self.centralwidget)
        self.textEdit.setReadOnly(False)
        self.textEdit.setPalette(self.palette)
        self.textEdit.setFont(self.font)
        self.textEdit.setFocus()
        self.central_layout.addWidget(self.textEdit)

        self.centralwidget.setLayout(self.central_layout)
        

        self.font_size_label = QtWidgets.QLabel(self.centralwidget)
        self.font_size_label.setPalette(self.palette)
        self.font_size_label.setFont(self.font)
        self.font_size_label.setText("Font Size:")
        self.font_size_label.adjustSize()
        self.font_size_label.setMaximumSize(self.font_size_label.size())
        self.menubar_layout.addWidget(self.font_size_label)

        self.font_size_box = QtWidgets.QSpinBox(self.centralwidget)
        self.font_size_box.setPalette(self.palette)
        self.font_size_box.setFont(self.font)
        self.font_size_box.setProperty("value", self.font.pointSize())
        self.font_size_box.setMinimum(1)
        self.font_size_box.setSingleStep(2)
        self.font_size_box.setMaximumSize(self.font_size_box.size())
        self.menubar_layout.addWidget(self.font_size_box)

        self.font_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.font_combo_box.addItems(fonts)
        self.font_combo_box.setPalette(self.palette)
        self.font_combo_box.setFont(self.font)
        self.font_combo_box.adjustSize()
        self.font_combo_box.setStyleSheet("background-color: rgb(70, 150, 150)")
        self.font_combo_box.setCurrentText("Courier New")
        self.font_combo_box.setMaximumSize(self.font_combo_box.size())
        self.menubar_layout.addWidget(self.font_combo_box)

        self.alignment_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.alignment_combo_box.addItem(QtGui.QIcon(icons["left"]),"Left")
        self.alignment_combo_box.addItem(QtGui.QIcon(icons["center"]),"Center")
        self.alignment_combo_box.addItem(QtGui.QIcon(icons["right"]),"Right")
        self.alignment_combo_box.setStyleSheet("background-color: rgb(70, 150, 150)")
        self.alignment_combo_box.setFont(self.font)
        self.alignment_combo_box.adjustSize()
        self.alignment_combo_box.setPalette(self.palette)
        self.alignment_combo_box.setMaximumSize(self.alignment_combo_box.size())
        self.menubar_layout.addWidget(self.alignment_combo_box)

        self.bold_button = QtWidgets.QPushButton(self.centralwidget)
        self.bold_button.setIcon(QtGui.QIcon(icons["bold"]))
        self.bold_button.setStyleSheet("background-color: rgb(70, 150, 150)")
        self.bold_button.setCheckable(True)
        self.bold_button.setMaximumSize(self.bold_button.size())
        self.menubar_layout.addWidget(self.bold_button)

        self.italic_button = QtWidgets.QPushButton(self.centralwidget)
        self.italic_button.setIcon(QtGui.QIcon(icons["italic"]))
        self.italic_button.setStyleSheet("background-color: rgb(70, 150, 150)")
        self.italic_button.setCheckable(True)
        self.italic_button.setMaximumSize(self.italic_button.size())
        self.menubar_layout.addWidget(self.italic_button)

        self.underline_button = QtWidgets.QPushButton(self.centralwidget)
        self.underline_button.setIcon(QtGui.QIcon(icons["underline"]))
        self.underline_button.setStyleSheet("background-color: rgb(70, 150, 150)")
        self.underline_button.setCheckable(True)
        self.underline_button.setMaximumSize(self.underline_button.size())
        self.menubar_layout.addWidget(self.underline_button)

        #self.menubar_layout.addSpacerItem(QtWidgets.QSpacerItem(1700,40))

        self.submenubar.setLayout(self.menubar_layout)

        self.confirm_dialog = QtWidgets.QDialog()
        self.confirm_dialog.resize(500, 250)
        self.confirm_dialog.setFont(self.font)
        self.confirm_dialog.setWindowTitle("Confirm Quit")
        self.confirm_dialog.setPalette(self.palette)
        self.confirm_dialog.setStyleSheet("background-color: rgb(100, 155, 155)")

        self.buttonBox = QtWidgets.QDialogButtonBox(self.confirm_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 140, 300, 80))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.label = QtWidgets.QLabel(self.confirm_dialog)
        self.label.move(50, 50)
        self.label.setText("Would you like to save first?")
        self.label.adjustSize()
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.confirm_dialog_2 = QtWidgets.QDialog()
        self.confirm_dialog_2.resize(500, 250)
        self.confirm_dialog_2.setFont(self.font)
        self.confirm_dialog_2.setWindowTitle("Confirm Exit")
        self.confirm_dialog_2.setPalette(self.palette)
        self.confirm_dialog_2.setStyleSheet("background-color: rgb(100, 155, 155)")

        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.confirm_dialog_2)
        self.buttonBox_2.setGeometry(QtCore.QRect(160, 140, 300, 80))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox_2.setCenterButtons(True)
        self.label_2 = QtWidgets.QLabel(self.confirm_dialog_2)
        self.label_2.move(50, 50)
        self.label_2.setText("Would you like to save first?")
        self.label_2.adjustSize()
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))        
        self.menubar.setPalette(self.palette)

        self.menuFile = QtWidgets.QMenu(self.menubar)        
        self.menuFile.setPalette(self.palette)
        self.menuFile.setTitle("File")
        self.menubar.addAction(self.menuFile.menuAction())

        self.menuEdit = QtWidgets.QMenu(self.menubar)        
        self.menuEdit.setPalette(self.palette)
        self.menuEdit.setTitle("Edit")
        self.menubar.addAction(self.menuEdit.menuAction())

        self.menuFormat = QtWidgets.QMenu(self.menubar)        
        self.menuFormat.setPalette(self.palette)
        self.menuFormat.setTitle("Format")
        self.menubar.addAction(self.menuFormat.menuAction())

        self.menuFont = QtWidgets.QMenu(self.menuFormat)        
        self.menuFont.setPalette(self.palette)
        self.menuFont.setTitle("Font")
        self.menuFormat.addAction(self.menuFont.menuAction())

        self.menuAlignment = QtWidgets.QMenu(self.menuFormat)
        self.menuAlignment.setPalette(self.palette)
        self.menuAlignment.setTitle("Alignment")
        self.menuFormat.addAction(self.menuAlignment.menuAction())

        MainWindow.setMenuBar(self.menubar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setText("New")
        self.actionNew.setShortcut("Ctrl+N")
        self.menuFile.addAction(self.actionNew)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setText("Save")
        self.actionSave.setShortcut("Ctrl+S")
        self.menuFile.addAction(self.actionSave)

        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setText("Save As")
        self.menuFile.addAction(self.actionSaveAs)

        self.actionSaveAsPlainText = QtWidgets.QAction(MainWindow)
        self.actionSaveAsPlainText.setText("Save As Plain Text")
        self.menuFile.addAction(self.actionSaveAsPlainText)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setText("Open")
        self.actionOpen.setShortcut("Ctrl+O")
        self.menuFile.addAction(self.actionOpen)

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setText("Quit")
        self.menuFile.addAction(self.actionQuit)

        self.actionGmail = QtWidgets.QAction(MainWindow)
        self.actionGmail.setText("Email")
        self.menuFile.addAction(self.actionGmail)

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setText("Copy")
        self.actionCopy.setShortcut("Ctrl+C")
        self.menuEdit.addAction(self.actionCopy)

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setText("Paste")
        self.actionPaste.setShortcut("Ctrl+V")
        self.menuEdit.addAction(self.actionPaste)

        self.actionBold = QtWidgets.QAction(MainWindow)
        self.actionBold.setText("Bold")
        self.actionBold.setShortcut("Ctrl+B")
        self.actionBold.setCheckable(True)
        self.menuFormat.addAction(self.actionBold)

        self.actionItalics = QtWidgets.QAction(MainWindow)
        self.actionItalics.setText("Italics")
        self.actionItalics.setShortcut("Ctrl+I")
        self.actionItalics.setCheckable(True)
        self.menuFormat.addAction(self.actionItalics)

        self.actionUnderline = QtWidgets.QAction(MainWindow)
        self.actionUnderline.setText("Underline")
        self.actionUnderline.setShortcut("Ctrl+U")
        self.actionUnderline.setCheckable(True)
        self.menuFormat.addAction(self.actionUnderline)

        self.actionStrikeOut = QtWidgets.QAction(MainWindow)
        self.actionStrikeOut.setText("StrikeOut")
        self.actionStrikeOut.setCheckable(True)
        self.menuFormat.addAction(self.actionStrikeOut)

        self.actionLeft = QtWidgets.QAction(MainWindow)
        self.actionLeft.setText("Left")
        self.menuAlignment.addAction(self.actionLeft)

        self.actionCenter = QtWidgets.QAction(MainWindow)
        self.actionCenter.setText("Center")
        self.menuAlignment.addAction(self.actionCenter)

        self.actionRight = QtWidgets.QAction(MainWindow)
        self.actionRight.setText("right")
        self.menuAlignment.addAction(self.actionRight)