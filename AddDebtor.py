from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AddDebtor(QDialog):
    def __init__(self, Debtor, parent = None):
        super(AddDebtor, self).__init__(parent)

        self.setWindowTitle("Add Debtor")
        self.setWindowFlags(Qt.Window|Qt.WindowCloseButtonHint|Qt.CustomizeWindowHint|Qt.WindowStaysOnTopHint)
        self.setFixedSize(336, 293)

        grid = QGridLayout(self)

        name = QLabel("Name", self)
        grid.addWidget(name, 0, 0)

        self.Name = QLineEdit(self)
        name.setBuddy(self.Name)
        grid.addWidget(self.Name, 1, 0, 1, 4)

        nickname = QLabel("Nickname(optional)", self)
        grid.addWidget(nickname, 2, 0)

        self.Nickname = QLineEdit(self)
        nickname.setBuddy(self.Nickname)
        grid.addWidget(self.Nickname, 3, 0, 1, 4)

        telephone = QLabel("Telephone number(optional)", self)
        grid.addWidget(telephone, 4, 0)

        self.Telephone = QLineEdit(self)
        telephone.setBuddy(self.Telephone)
        grid.addWidget(self.Telephone, 5, 0, 1, 2)

        phonenumber = QLabel("Phone number(optional)", self)
        grid.addWidget(phonenumber, 4, 2)

        self.PhoneNumber = QLineEdit(self)
        phonenumber.setBuddy(self.PhoneNumber)
        grid.addWidget(self.PhoneNumber, 5, 2, 1, 2)

        debt = QLabel("Debt", self)
        grid.addWidget(debt, 6, 0)

        self.Debt = QLineEdit(self)
        self.Debt.setReadOnly(True)
        debt.setBuddy(self.Debt)
        grid.addWidget(self.Debt, 7, 0, 1, 4)

        paid = QLabel("Paid", self)
        grid.addWidget(paid, 8, 0)

        self.Paid = QLineEdit(self)
        paid.setBuddy(self.Paid)
        grid.addWidget(self.Paid, 9, 0, 1, 2)

        totalafterpayment = QLabel("The Total after Payment", self)
        grid.addWidget(totalafterpayment, 8, 2)

        self.TotalAfterPayment = QLineEdit(self)
        self.TotalAfterPayment.setReadOnly(True)
        totalafterpayment.setBuddy(self.TotalAfterPayment)
        grid.addWidget(self.TotalAfterPayment, 9, 2, 1, 2)

        self.Save = QPushButton("Save", self)
        grid.addWidget(self.Save, 10, 2)

        self.Cancel = QPushButton("Cancel", self)
        grid.addWidget(self.Cancel, 10, 3)
