from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from database import init_db

def main():
    init_db()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
