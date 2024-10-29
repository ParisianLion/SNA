from PyQt6.QtGui import QAction  # Change this line
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QApplication
from gui.add_contact_dialog import AddContactDialog
from gui.add_relationship_dialog import AddRelationshipDialog
from gui.analytics_dashboard import AnalyticsDashboard
from visualization.network_visualization import NetworkVisualization

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Social Network Analysis App')
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.network_visualization = NetworkVisualization()
        self.analytics_dashboard = AnalyticsDashboard()

        self.tabs.addTab(self.network_visualization, 'Network Visualization')
        self.tabs.addTab(self.analytics_dashboard, 'Analytics Dashboard')

        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu('File')

        add_contact_action = QAction('Add Contact', self)
        add_contact_action.triggered.connect(self.open_add_contact_dialog)
        file_menu.addAction(add_contact_action)

        add_relationship_action = QAction('Add Relationship', self)
        add_relationship_action.triggered.connect(self.open_add_relationship_dialog)
        file_menu.addAction(add_relationship_action)

    def open_add_contact_dialog(self):
        dialog = AddContactDialog(self)
        dialog.exec()

    def open_add_relationship_dialog(self):
        dialog = AddRelationshipDialog(self)
        dialog.exec()
