from PyQt5 import QtWidgets, QtCore, QtGui
from UI.Student import Ui_Xbox
from Control.Student import Student


class StudentBox(object):
    """学生信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_Xbox()
        window.setupUi(self.dialog)

        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/favicon.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.SIDEdit = window.SIDEdit  # 学号编辑
        self.SnameEdit = window.SnameEdit  # 姓名编辑
        self.DorEdit = window.DorEdit  # 楼号编辑
        self.DIDEdit = window.DIDEdit  # 宿舍号编辑
        self.isHethdayEdit = window.isHethdayEdit  # 是否健康
        self.MIDEdit = window.MIDEdit  # 楼管ID编辑
        self.ishethEdit = window.ishethEdit  # 核酸情况
        self.msgLabel = window.msg  # 提示信息

        self.okButton = window.okButton
        self.cancelButton = window.cancelButton
        self.okButton.clicked.connect(self.onOkButtonClicked)
        self.cancelButton.clicked.connect(self.dialog.close)

        self.maleButton = window.nanButton
        self.famaleButton = window.nvButton

    def getSex(self):  # 得到性别
        if self.maleButton.isChecked():
            return 1
        elif self.famaleButton.isChecked():
            return 2
        else:
            return 0

    def setSex(self, value):
        if value == 1:
            self.maleButton.setChecked(True)
        elif value == 2:
            self.famaleButton.setChecked(True)

    def onOkButtonClicked(self):
        if self.onFinished():
            self.dialog.close()

    def show(self):
        self.dialog.show()

    def setTitle(self, title):
        self.dialog.setWindowTitle(title)

    def setMsg(self, text):
        self.msgLabel.setText(text)

    def setButton(self, ok, cancel=None):
        self.okButton.setText(ok)
        self.cancelButton.setText(cancel) if cancel is not None else None

    def applyToStudent(self, student):
        student.SID = self.SIDEdit.text()
        student.Sname = self.SnameEdit.text()
        student.Ssex = self.getSex()
        student.isHethday = self.isHethdayEdit.text()
        student.isHeth = self.ishethEdit.text()
        student.DID = self.DIDEdit.text()
        student.MID = self.MIDEdit.text()
        student.Dor = self.DorEdit.text()

    def onFinished(self):
        return False


class EditBox(StudentBox):
    """编辑学生信息 - 继承StudentBox"""

    def __init__(self, student, callback):
        super(EditBox, self).__init__()
        self.callback = callback

        self.setTitle("修改信息...")
        self.setMsg("")
        self.setButton("修改")

        self.SIDEdit.setText(student.SID)
        self.SnameEdit.setText(student.Sname)
        self.setSex(student.Ssex)
        self.DorEdit.setText(student.Dor)
        self.DIDEdit.setText(student.DID)
        self.isHethdayEdit.setText(student.isHethday)
        self.ishethEdit.setText(student.isHeth)
        self.MIDEdit.setText(student.MID)

        self._student = Student()

    def onFinished(self):
        self.applyToStudent(self._student)
        check, info = self._student.checkInfo()
        if check:
            self.callback(self._student)
        else:
            self.setMsg(info)
        return check

    def show(self):
        self.SIDEdit.setEnabled(False)
        self.SnameEdit.setEnabled(False)
        self.SnameEdit.setClearButtonEnabled(False)
        self.SIDEdit.setClearButtonEnabled(False)
        self.dialog.show()


class NewBox(StudentBox):
    """新建学生档案 - 继承StudentBox"""

    def __init__(self, callback):
        super(NewBox, self).__init__()
        self.callback = callback

        self.setTitle("新建档案...")
        self.setMsg("")
        self.setButton("新建")

        self.student = Student()

    def onFinished(self):
        student = self.student
        self.applyToStudent(student)
        check, info = student.checkInfo(True)
        self.callback(self.student) if check else self.setMsg(info)
        return check


class SearchBox(StudentBox):
    """高级搜索框 - 继承StudentBox"""

    def __init__(self, callback):
        super(SearchBox, self).__init__()
        self.callback = callback

        self.setTitle("高级搜索...")
        self.setMsg("请输入检索关键词")
        self.setButton("搜索")

        self.maleButton.setEnabled(False)
        self.famaleButton.setEnabled(False)

    def onFinished(self):
        keyList = [
            ("SID", ' '.join(self.SIDEdit.text().split())),
            ("Sname", ' '.join(self.SnameEdit.text().split())),
            ("Dor", ' '.join(self.DorEdit.text().split())),
            ("DID", ' '.join(self.DIDEdit.text().split())),
            ("MID", ' '.join(self.MIDEdit.text().split())),
            ("isHethday",' '.join(self.isHethdayEdit.text().split())),
            ("isHeth", ' '.join(self.ishethEdit.text().split())),
        ]
        self.callback(keyList)
        return True
