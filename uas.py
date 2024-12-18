import sys
import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1044, 823)

        # Input fields
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 301, 41))
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 180, 301, 41))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 81, 31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 131, 31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 280, 301, 41))
        self.textEdit_3.setObjectName("textEdit_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 340, 131, 31))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 380, 301, 41))
        self.textEdit_4.setObjectName("textEdit_4")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 450, 131, 31))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 490, 301, 41))
        self.textEdit_5.setObjectName("textEdit_5")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 570, 301, 51))
        self.pushButton.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.pushButton.setObjectName("pushButton")

        self.textEdit_6 = QtWidgets.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(430, 60, 421, 41))
        self.textEdit_6.setObjectName("textEdit_6")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(370, 70, 55, 31))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 640, 301, 51))
        self.pushButton_2.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 710, 301, 51))
        self.pushButton_3.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.pushButton_3.setObjectName("pushButton_3")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(370, 120, 621, 641))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)

        for col in range(5):
            self.tableWidget.setHorizontalHeaderItem(col, QtWidgets.QTableWidgetItem())

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 60, 121, 41))
        self.pushButton_4.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect buttons to functions
        self.pushButton.clicked.connect(self.insertmahasiswa)
        self.pushButton_2.clicked.connect(self.updatemahasiswa)
        self.pushButton_3.clicked.connect(self.hapusmahasiswa)
        self.pushButton_4.clicked.connect(self.searchmahasiswa)

        # Load mahasiswa data on startup
        self.loadmahasiswa()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Npm :"))
        self.label_2.setText(_translate("Form", "Nama :"))
        self.label_3.setText(_translate("Form", "Tanggal Lahir :"))
        self.label_4.setText(_translate("Form", "Kelas :"))
        self.label_5.setText(_translate("Form", "Jurusan :"))
        self.pushButton.setText(_translate("Form", "SIMPAN"))
        self.label_6.setText(_translate("Form", "Cari :"))
        self.pushButton_2.setText(_translate("Form", "PERBARUI"))
        self.pushButton_3.setText(_translate("Form", "HAPUS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "NPM"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Kelas"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Jurusan"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tanggal Lahir"))
        self.pushButton_4.setText(_translate("Form", "Cari"))

    # Database Connection
    def koneksi_db(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="dbkampus"
            )
            return mydb
        except mc.Error as e:
            QMessageBox.critical(None, "Database Error", f"Koneksi ke database gagal: {e}")
            return None

    # Insert Mahasiswa
    def insertmahasiswa(self):
        try:
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            sql = "INSERT INTO mahasiswa (npm, nama, kelas, jurusan, tanggal_lahir) VALUES (%s, %s, %s, %s, %s)"
            val = (
                self.textEdit.toPlainText(),
                self.textEdit_2.toPlainText(),
                self.textEdit_4.toPlainText(),
                self.textEdit_5.toPlainText(),
                self.textEdit_3.toPlainText()
            )
            cursor.execute(sql, val)
            mydb.commit()
            QMessageBox.information(None, "Success", "Data mahasiswa berhasil ditambahkan")
            self.loadmahasiswa()
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal menambahkan data: {e}")

    # Load all Mahasiswa
    def loadmahasiswa(self):
        try:
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM mahasiswa")
            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal memuat data: {e}")

    # Update Mahasiswa
    def updatemahasiswa(self):
        try:
            selected_row = self.tableWidget.currentRow()
            if selected_row == -1:
                QMessageBox.warning(None, "Warning", "Pilih baris yang ingin diubah")
                return
            npm = self.tableWidget.item(selected_row, 0).text()
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            sql = "UPDATE mahasiswa SET nama = %s, kelas = %s, jurusan = %s, tanggal_lahir = %s WHERE npm = %s"
            val = (
                self.textEdit_2.toPlainText(),
                self.textEdit_4.toPlainText(),
                self.textEdit_5.toPlainText(),
                self.textEdit_3.toPlainText(),
                npm
            )
            cursor.execute(sql, val)
            mydb.commit()
            QMessageBox.information(None, "Success", "Data mahasiswa berhasil diubah")
            self.loadmahasiswa()
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal mengubah data: {e}")

    # Delete Mahasiswa
    def hapusmahasiswa(self):
        try:
            selected_row = self.tableWidget.currentRow()
            if selected_row == -1:
                QMessageBox.warning(None, "Warning", "Pilih baris yang ingin dihapus")
                return
            npm = self.tableWidget.item(selected_row, 0).text()
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            sql = "DELETE FROM mahasiswa WHERE npm = %s"
            cursor.execute(sql, (npm,))
            mydb.commit()
            QMessageBox.information(None, "Success", "Data mahasiswa berhasil dihapus")
            self.loadmahasiswa()
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal menghapus data: {e}")

    # Search Mahasiswa by Name
    def searchmahasiswa(self):
        try:
            keyword = self.textEdit_6.toPlainText().strip()

            if not keyword:
                QMessageBox.warning(None, "Input Error", "Masukkan nama yang ingin dicari.")
                return

            mydb = self.koneksi_db()
            if not mydb:
                return

            cursor = mydb.cursor()
            sql = "SELECT * FROM mahasiswa WHERE nama LIKE %s"
            cursor.execute(sql, (f"%{keyword}%",))

            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)

            if not result:
                QMessageBox.information(None, "Search Result", "Tidak ada data yang ditemukan.")
                return

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal mencari data: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
