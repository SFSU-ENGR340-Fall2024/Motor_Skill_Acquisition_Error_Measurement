import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, 
                             QVBoxLayout, QStackedWidget, QLabel, QHBoxLayout)

class MultiPageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        # Create a stacked widget to hold multiple pages
        self.stacked_widget = QStackedWidget(self)

        # Create different pages as separate widgets
        self.page1 = self.create_page1()
        self.page2 = self.create_page2()
        self.page3 = self.create_page3()

        # Add pages to the stacked widget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # Create navigation buttons
        nav_layout = QHBoxLayout()
        self.btn_page1 = QPushButton('Go to Page 1')
        self.btn_page2 = QPushButton('Go to Page 2')
        self.btn_page3 = QPushButton('Go to Page 3')

        # Connect buttons to their respective page-changing functions
        self.btn_page1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.btn_page2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.btn_page3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Add buttons to the navigation layout
        nav_layout.addWidget(self.btn_page1)
        nav_layout.addWidget(self.btn_page2)
        nav_layout.addWidget(self.btn_page3)

        # Main layout that combines navigation and the stacked widget
        main_layout = QVBoxLayout()
        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.stacked_widget)

        # Set the layout for the main window
        self.setLayout(main_layout)
        self.setGeometry(300, 200, 400, 300)
        self.setWindowTitle('Multi-Page GUI')
        self.show()

    # Create a simple page with a label
    def create_page1(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel('This is Page 1')
        layout.addWidget(label)
        page.setLayout(layout)
        return page

    def create_page2(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel('This is Page 2')
        layout.addWidget(label)
        page.setLayout(layout)
        return page

    def create_page3(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel('This is Page 3')
        layout.addWidget(label)
        page.setLayout(layout)
        return page

def run():
    app = QApplication(sys.argv)
    window = MultiPageApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
