import cryptography
import sys
import os
import hashlib
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QLineEdit, QMessageBox, QTextEdit, QGridLayout
)
from PySide6.QtCore import Qt

class EncryptorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Encryptor")
        self.resize(400, 500)
        layout = QVBoxLayout()

        self.select_button = QPushButton("Browse File")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.file_path_display = QTextEdit()
        self.file_path_display.setReadOnly(True)
        layout.addWidget(self.file_path_display)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")
        layout.addWidget(self.password_input)

        self.encrypt_button = QPushButton("Encrypt File")
        self.encrypt_button.clicked.connect(self.encrypt_file)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Decrypt File")
        self.decrypt_button.clicked.connect(self.decrypt_file)
        layout.addWidget(self.decrypt_button)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.selected_file = None

    def select_file(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select File", os.path.expanduser("~"), "Text Files (*.txt *.enc)"
        )
        if files:
            self.file_path_display.setText("\n".join(files))
        else:
            pass

    def update_status(self):
        pass

    def encrypt_file(self):
        pass

    def decrypt_file(self):
        pass

    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptorApp()
    window.show()
    sys.exit(app.exec())
        