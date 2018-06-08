from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from AddDebtor import AddDebtor
from EditDebtorData import EditDebtorData
from ShowDebtorData import ShowDebtorData
import sys, qdarkstyle

class Debts(QMainWindow):
    def __init__(self, parent = None):
        super(Debts, self).__init__(parent)

        self.setWindowTitle("Debts")
        self.setFixedSize(480, 640)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setCentralWidget(QWidget())

        self.DebtorsMenu = QMenu("Debtors", self)
        self.menuBar().addMenu(self.DebtorsMenu)

        self.AddDebtorAction = QAction("Add Debtor", self, shortcut = "Ctrl+A", triggered=self.addDebtor)
        self.DebtorsMenu.addAction(self.AddDebtorAction)

        self.EditDebtorDataAction = QAction("Edit Debtor Data", self, shortcut = "Ctrl+E", triggered=self.editDebtorData)
        self.DebtorsMenu.addAction(self.EditDebtorDataAction)

        self.ShowDebtorDataAction = QAction("Show Debtor Data", self, shortcut="Ctrl+S", triggered=self.showDebtorData)
        self.DebtorsMenu.addAction(self.ShowDebtorDataAction)

        self.DeleteDebtorAction = QAction("Delete Debtor", self, shortcut = "Ctrl+D", triggered=self.DeleteDebtorData)
        self.DebtorsMenu.addAction(self.DeleteDebtorAction)

        self.ThemesMenu = QMenu("Themes", self)
        self.ThemesMenu.addActions([QAction("Default Theme", self, triggered=self.DefaultTheme), QAction("Dark Theme", self, triggered=self.DarkTheme)])
        self.menuBar().addMenu(self.ThemesMenu)

        self.MinimizeToTrayAction = QAction("Minimize To Tray", self, shortcut="Ctrl+M")
        self.menuBar().addAction(self.MinimizeToTrayAction)

        grid = QGridLayout(self.centralWidget())

        self.SearchBox = QLineEdit(self)
        self.SearchBox.setPlaceholderText("Search...")
        grid.addWidget(self.SearchBox, 0, 0)

        self.SearchByButton = QPushButton(self)
        self.SearchByButton.setText("Search By Name")
        self.SearchByMenu = QMenu(self)
        self.SearchByNameAction = QAction("Search By Name", self)
        self.SearchByIdAction = QAction("Search By Id", self)
        self.SearchByMenu.addActions([self.SearchByNameAction, self.SearchByIdAction])
        self.SearchByButton.setMenu(self.SearchByMenu)
        grid.addWidget(self.SearchByButton, 0, 1)

        self.NamesList = QListWidget(self)
        grid.addWidget(self.NamesList, 1, 0, 1, 2)

    def DefaultTheme(self):
        app.setStyleSheet("")

    def DarkTheme(self):
        f = open("style.qss", "r")
        app.setStyleSheet(f.read())
        f.close()

    def addDebtor(self):
        try:
            DebtorAddition.exec_()
        except Exception as ex:
            QMessageBox.critical(self, "Error", ex)

    def editDebtorData(self):
        try:
            Debtoredition.exec_()
        except Exception as ex:
            QMessageBox.critical(self, "Error", ex)

    def showDebtorData(self):
        try:
            Debtorshowing.exec_()
        except Exception as ex:
            QMessageBox.critical(self, "Error", ex)

    def DeleteDebtorData(self):
        QMessageBox.question(self, "Delete Debtor", "If you delete this debtor.\nYou will lose all of his data.\nIt can't be restored.", QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Cancel)

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("img/hand.png"))
f = open("style.qss", "r")
app.setStyleSheet(f.read())
f.close()
DebtorAddition = AddDebtor("Mohamed")
Debtoredition = EditDebtorData("Mohamed")
Debtorshowing = ShowDebtorData("Mohamed")
debts = Debts()
debts.show()
app.exec_()
