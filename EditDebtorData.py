from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class EditDebtorData(QDialog):
    def __init__(self, Debtor, parent = None):
        super(EditDebtorData, self).__init__(parent)

        self.setWindowTitle("Edit Debtor Data")
        self.setWindowFlags(Qt.Window|Qt.WindowCloseButtonHint|Qt.CustomizeWindowHint|Qt.WindowStaysOnTopHint)
        self.setFixedSize(374, 343)

        grid = QGridLayout(self)

        self.Name = QLabel("Name: ", self)
        grid.addWidget(self.Name, 0, 0, 1, 4)

        self.Nickname = QLabel("Nickname: ", self)
        grid.addWidget(self.Nickname, 1, 0, 1, 4)

        previousdebt = QLabel("Previous debt", self)
        grid.addWidget(previousdebt, 2, 0)

        self.PreviousDebt = QLineEdit(self)
        self.PreviousDebt.setReadOnly(True)
        previousdebt.setBuddy(self.PreviousDebt)
        grid.addWidget(self.PreviousDebt, 3, 0, 1, 2)

        currentdebt = QLabel("Current debt", self)
        grid.addWidget(currentdebt, 2, 2)

        self.CurrentDebt = QLineEdit(self)
        currentdebt.setBuddy(self.CurrentDebt)
        grid.addWidget(self.CurrentDebt, 3, 2, 1, 2)

        totaldebt = QLabel("Total debt", self)
        grid.addWidget(totaldebt, 4, 0)

        self.TotalDebt = QLineEdit(self)
        self.TotalDebt.setReadOnly(True)
        totaldebt.setBuddy(self.TotalDebt)
        grid.addWidget(self.TotalDebt, 5, 0, 1, 4)

        paid = QLabel("Paid", self)
        grid.addWidget(paid, 6, 0)

        self.Paid = QLineEdit(self)
        paid.setBuddy(self.Paid)
        grid.addWidget(self.Paid, 7, 0, 1, 2)

        showPayments = QPushButton("Show Payments", self)
        grid.addWidget(showPayments, 7, 2, 1, 2)

        totalafterpayment = QLabel("The Total after Payment", self)
        grid.addWidget(totalafterpayment, 8, 0)

        self.TotalAfterPayment = QLineEdit(self)
        self.TotalAfterPayment.setReadOnly(True)
        totalafterpayment.setBuddy(self.TotalAfterPayment)
        grid.addWidget(self.TotalAfterPayment, 9, 0, 1, 4)

        self.Save = QPushButton("Save", self)
        self.Save.clicked.connect(self.clicked)
        grid.addWidget(self.Save, 10, 2)

        self.Cancel = QPushButton("Cancel", self)
        grid.addWidget(self.Cancel, 10, 3)

    def clicked(self):
        print("Width: %i," % self.width(), "Height: %i" % self.height())
