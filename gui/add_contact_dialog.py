from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QVBoxLayout
from database import session
from models import Contact

class AddContactDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Contact')

        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()

        layout.addRow('Name:', self.name_input)
        layout.addRow('Email:', self.email_input)
        layout.addRow('Phone:', self.phone_input)

        self.submit_button = QPushButton('Add')
        self.submit_button.clicked.connect(self.add_contact)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.submit_button)
        self.setLayout(main_layout)

    def add_contact(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()

        contact = Contact(name=name, email=email, phone=phone)
        session.add(contact)
        session.commit()
        self.accept()
