import cryptography
import sys
import os
import hashlib
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QLineEdit, QTextEdit
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

        self.selected_files = []

    def select_file(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select File", "", "Text Files (*.txt *.enc)" # path should be os.path.expanduser("~")
        )
        if files:
            self.file_path_display.setText("\n".join(files))
            self.selected_files = files
            self.update_status("Files selected successfuly")
        else:
            self.update_status("No files selected")

    def update_status(self, message):
        self.status_label.setText(message)

    def encrypt_file(self):
        if not self.selected_files or not self.password_input.text():
            self.update_status("Please select at least 1 file and enter a password")
            return
        try:
            self.file_path_display.setText("")
            for file in self.selected_files:
                with open(file, "r", encoding="utf-8") as f:
                    plaintext = f.read()
                salt = os.urandom(8)
                key = cryptography.generate_key(self.password_input.text(), salt)
                cipher_text = cryptography.encrypt_text(plaintext, key)
                out_path = file + ".enc"
                with open(out_path, 'wb') as f:
                    f.write(salt + b'\n' + cipher_text)
                self.update_status(f"Encrypted successfuly")
                self.file_path_display.append(f"Encrypted successfuly:\n{file}\n -> {out_path}\n\n")

        except Exception as e:
            self.update_status(f"Encryption failed: {e.with_traceback()}")
            

    def decrypt_file(self):
        if not self.selected_files or not self.password_input.text():
            self.update_status("Please select at least 1 file and enter a password")
            return
        try:
            self.file_path_display.setText("")
            for file in self.selected_files:
                with open(file, "rb") as f:
                    salt, cipher_text = f.read().split(b'\n', 1)
                key = cryptography.generate_key(self.password_input.text(), salt)
                plain_text = cryptography.decrypt_text(cipher_text, key)
                out_path = file.replace(".txt.enc", "_decrypted.txt")
                with open(out_path, 'w', encoding="utf-8") as f:
                    f.write(plain_text)
                self.update_status(f"Decrypted successfuly")
                self.file_path_display.append(f"Decrypted successfuly:\n{file}\n-> {out_path}\n\n")

        except Exception as e:
            self.update_status(f"Decryption failed: {e.with_traceback()}")

    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptorApp()
    window.show()
    sys.exit(app.exec())
        