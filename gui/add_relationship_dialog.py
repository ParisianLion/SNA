from PyQt6.QtWidgets import QDialog, QFormLayout, QComboBox, QPushButton, QVBoxLayout
from database import session
from models import Contact

class AddRelationshipDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Relationship')

        contacts = session.query(Contact).all()
        self.contact_dict = {contact.name: contact for contact in contacts}

        layout = QFormLayout()
        self.contact1_combo = QComboBox()
        self.contact2_combo = QComboBox()
        self.contact1_combo.addItems(self.contact_dict.keys())
        self.contact2_combo.addItems(self.contact_dict.keys())

        layout.addRow('Contact 1:', self.contact1_combo)
        layout.addRow('Contact 2:', self.contact2_combo)

        self.submit_button = QPushButton('Add Relationship')
        self.submit_button.clicked.connect(self.add_relationship)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.submit_button)
        self.setLayout(main_layout)

    def add_relationship(self):
        name1 = self.contact1_combo.currentText()
        name2 = self.contact2_combo.currentText()

        contact1 = self.contact_dict[name1]
        contact2 = self.contact_dict[name2]

        contact1.relationships.append(contact2)
        session.commit()
        self.accept()
