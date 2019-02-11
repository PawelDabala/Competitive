from PySide2 import QtCore, QtGui, QtWidgets



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.curFile = ''

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createStatusBar()

        self.readSettings()

        #self.textEdit.document().contentsChanged.connect(self.documentWasModified)

        #self.setCurrentFile('')


    def closeEvent(self, event):
        self.close()

        # if self.maybeSave():
        #     self.writeSettings()
        #     event.accept()
        # else:
        #     event.ignore()

    def newFile(self):
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFile('')

    def open(self):
        print("open")
        # !!! Nie kasować !!!
        # if self.maybeSave():
        #     fileName, filtr = QtWidgets.QFileDialog.getOpenFileName(self)
        #     if fileName:
        #         self.loadFile(fileName)

    def save(self):
        print("save file")
        ### !!!!! TUTAJ BĘDZIE ZAPIS DO BAZY !!!!!!!
        # if self.curFile:
        #     return self.saveFile(self.curFile)
        #
        # return self.saveAs()



    # def about(self):
    #     QtWidgets.QMessageBox.about(self, "About Application",
    #             "The <b>Application</b> example demonstrates how to write "
    #             "modern GUI applications using Qt, with a menu bar, "
    #             "toolbars, and a status bar.")
    #
    # def documentWasModified(self):
    #     self.setWindowModified(self.textEdit.document().isModified())

    def createActions(self):
        # self.newAct = QtWidgets.QAction(QtGui.QIcon(':/images/new.png'), "&New",
        #         self, shortcut=QtGui.QKeySequence.New,
        #         statusTip="Create a new file", triggered=self.newFile)

        self.openAct = QtWidgets.QAction(QtGui.QIcon(':/images/open.png'),
                "&Otwórz...", self, shortcut=QtGui.QKeySequence.Open,
                statusTip="Otwóż nowe pliki", triggered=self.open)

        self.saveAct = QtWidgets.QAction(QtGui.QIcon(':/images/save.png'),
                "&Zapisz...", self, shortcut=QtGui.QKeySequence.Save,
                statusTip="Zapisz plik", triggered=self.save)

        # self.saveAsAct = QtWidgets.QAction("Save &As...", self,
        #         shortcut=QtGui.QKeySequence.SaveAs,
        #         statusTip="Save the document under a new name",
        #         triggered=self.saveAs)

        self.exitAct = QtWidgets.QAction("&Zamknij", self, shortcut="Ctrl+Q",
                statusTip="Zamknij aplikacje", triggered=self.close)
        #
        # self.cutAct = QtWidgets.QAction(QtGui.QIcon(':/images/cut.png'), "Cu&t",
        #         self, shortcut=QtGui.QKeySequence.Cut,
        #         statusTip="Cut the current selection's contents to the clipboard",
        #         triggered=self.textEdit.cut)
        #
        # self.copyAct = QtWidgets.QAction(QtGui.QIcon(':/images/copy.png'),
        #         "&Copy", self, shortcut=QtGui.QKeySequence.Copy,
        #         statusTip="Copy the current selection's contents to the clipboard",
        #         triggered=self.textEdit.copy)
        #
        # self.pasteAct = QtWidgets.QAction(QtGui.QIcon(':/images/paste.png'),
        #         "&Paste", self, shortcut=QtGui.QKeySequence.Paste,
        #         statusTip="Paste the clipboard's contents into the current selection",
        #         triggered=self.textEdit.paste)
        #
        # self.aboutAct = QtWidgets.QAction("&About", self,
        #         statusTip="Show the application's About box",
        #         triggered=self.about)
        #
        # self.aboutQtAct = QtWidgets.QAction("About &Qt", self,
        #         statusTip="Show the Qt library's About box",
        #         triggered=QtWidgets.qApp.aboutQt)

        # self.cutAct.setEnabled(False)
        # self.copyAct.setEnabled(False)
        # self.textEdit.copyAvailable.connect(self.cutAct.setEnabled)
        # self.textEdit.copyAvailable.connect(self.copyAct.setEnabled)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&Plik")
        # self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        # self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        # self.editMenu = self.menuBar().addMenu("&Edit")
        # self.editMenu.addAction(self.cutAct)
        # self.editMenu.addAction(self.copyAct)
        # self.editMenu.addAction(self.pasteAct)

        # self.menuBar().addSeparator()
        #
        # self.helpMenu = self.menuBar().addMenu("&Help")
        # self.helpMenu.addAction(self.aboutAct)
        # self.helpMenu.addAction(self.aboutQtAct)


    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def readSettings(self):
        settings = QtCore.QSettings("Trolltech", "Application Example")
        pos = settings.value("pos", QtCore.QPoint(200, 200))
        size = settings.value("size", QtCore.QSize(400, 400))
        self.resize(size)
        self.move(pos)
    #
    # def writeSettings(self):
    #     settings = QtCore.QSettings("Trolltech", "Application Example")
    #     settings.setValue("pos", self.pos())
    #     settings.setValue("size", self.size())
    #
    # def maybeSave(self):
    #     if self.textEdit.document().isModified():
    #         ret = QtWidgets.QMessageBox.warning(self, "Application",
    #                 "The document has been modified.\nDo you want to save "
    #                 "your changes?",
    #                 QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard |
    #                 QtWidgets.QMessageBox.Cancel)
    #         if ret == QtWidgets.QMessageBox.Save:
    #             return self.save()
    #         elif ret == QtWidgets.QMessageBox.Cancel:
    #             return False
    #     return True
    #
    # def loadFile(self, fileName):
    #     file = QtCore.QFile(fileName)
    #     if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
    #         QtWidgets.QMessageBox.warning(self, "Application",
    #                 "Cannot read file %s:\n%s." % (fileName, file.errorString()))
    #         return
    #
    #     inf = QtCore.QTextStream(file)
    #     QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
    #     self.textEdit.setPlainText(inf.readAll())
    #     QtWidgets.QApplication.restoreOverrideCursor()
    #
    #     self.setCurrentFile(fileName)
    #     self.statusBar().showMessage("File loaded", 2000)

    # def saveFile(self, fileName):
    #     file = QtCore.QFile(fileName)
    #     if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
    #         QtWidgets.QMessageBox.warning(self, "Application",
    #                 "Cannot write file %s:\n%s." % (fileName, file.errorString()))
    #         return False
    #
    #     outf = QtCore.QTextStream(file)
    #     QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
    #
    #     # FIXME: Once file is out of scope, the file is empty, instead of having text.
    #     outf << self.textEdit.toPlainText()
    #     QtWidgets.QApplication.restoreOverrideCursor()
    #
    #     self.setCurrentFile(fileName)
    #     self.statusBar().showMessage("File saved", 2000)
    #     return True
    #
    # def setCurrentFile(self, fileName):
    #     self.curFile = fileName
    #     self.textEdit.document().setModified(False)
    #     self.setWindowModified(False)
    #
    #     if self.curFile:
    #         shownName = self.strippedName(self.curFile)
    #     else:
    #         shownName = 'untitled.txt'
    #
    #     self.setWindowTitle("%s[*] - Application" % shownName)
    #
    # def strippedName(self, fullFileName):
    #     return QtCore.QFileInfo(fullFileName).fileName()


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
