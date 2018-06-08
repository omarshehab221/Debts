from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ShowDebtorData(QDialog):
    def __init__(self, Debtor, parent = None):
        super(ShowDebtorData, self).__init__(parent)

        self.setWindowTitle("Show Debtor Data")
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(423, 104)

        grid = QGridLayout(self)

        self.Name = QLabel("Name: ", self)
        grid.addWidget(self.Name, 0, 0, 1, 4)

        self.Nickname = QLabel("Nickname: ", self)
        grid.addWidget(self.Nickname, 1, 0, 1, 4)

        self.Telephone = QLabel("Telephone: ", self)
        grid.addWidget(self.Telephone, 2, 0, 1, 2)

        self.PhoneNumber = QLabel("Phone number: ", self)
        grid.addWidget(self.PhoneNumber, 2, 2, 1, 2)

        self.Debt = QLabel("Debt: ", self)
        grid.addWidget(self.Debt, 3, 0, 1, 2)

        showPayments = QPushButton("Show Payments", self)
        grid.addWidget(showPayments, 3, 2, 1, 2)