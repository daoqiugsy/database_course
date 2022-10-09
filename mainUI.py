from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from UI._mainUI import Ui_MainWindow
from Control import StuboxUI, MboxUI, DorboxUI
import public


class mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 学生label
        self.SIDlable = self.ui.SID
        self.Snamelabel = self.ui.Sname
        self.Ssexlabel = self.ui.Ssex
        self.ishethlabel = self.ui.isheth
        self.hethdaylabel = self.ui.hethday
        self.Dorlabel = self.ui.Dor
        self.DIDlabel = self.ui.DID
        self.MIDlabel = self.ui.MID

        # 管理人员label
        self.MIDLabel_1 = self.ui.Mno
        self.MnameLabel_1 = self.ui.Mname_2
        self.Msexlabel = self.ui.MSex
        self.Magelabel = self.ui.Mage
        self.MphoneLabel = self.ui.MPhone

        # 宿舍label
        self.LnoLabel_1 = self.ui.Lno_2
        self.SnoLabel_2 = self.ui.Sno_2
        self.K_nLabel = self.ui.K_n
        self.C_nlabel = self.ui.C_n
        self.L_nlabel = self.ui.L_n
        # 高级搜索学生
        self.ui.SearchButton_1.clicked.connect(self.onSearchSTU)
        # 高级搜索宿管
        self.ui.SearchButton_3.clicked.connect(self.onSearchM)
        # 高级搜索宿舍
        self.ui.SearchButton_2.clicked.connect(self.onSearchS)
        # 新建学生档案
        self.ui.actionEdit_1.clicked.connect(self.onAddStudentX)
        # 新建宿管档案
        self.ui.actionEdit_3.clicked.connect(self.onAddStudentM)
        # 新建宿舍档案
        self.ui.actionEdit_2.clicked.connect(self.onAddStudentS)
        # 学生"快速检索信息, 使用"|"分隔多个条件"
        self.ui.SearchEdit_1.textChanged['QString'].connect(self.onQuickSearchX)
        # 宿管"快速检索信息, 使用"|"分隔多个条件"
        self.ui.SearchEdit_3.textChanged['QString'].connect(self.onQuickSearchM)
        # 宿舍"快速检索信息, 使用"|"分隔多个条件"
        self.ui.SearchEdit_2.textChanged['QString'].connect(self.onQuickSearchS)
        # 修改学生信息

        self.ui.editButton_1.clicked.connect(self.onEditX)
        # 修改宿管信息

        self.ui.editButton_3.clicked.connect(self.onEditM)
        # 修改宿舍信息
        self.ui.editButton_2.clicked.connect(self.onEditS)
        # 删除学生信息
        self.ui.DeleteButton_1.clicked.connect(self.onDeleteX)
        # 删除宿管信息

        self.ui.DeleteButton_3.clicked.connect(self.onDeleteM)
        # 删除宿舍信息
        self.ui.DeleteButton_2.clicked.connect(self.onDeleteS)
        # 学生表
        self.studentTable = self.ui.studentTable
        self.tableListX = []  # Student
        self.tableIndexX = {}  # Student -> Item
        self.studentTable.itemSelectionChanged.connect(self.onSelectStudent)
        self.studentTable.activated.connect(self.onEditX)

        width = [150, 102, 70, 70, 70, 70, 70, 150]
        [self.studentTable.setColumnWidth(i, width[i]) for i in range(8)]
        self.searchModeX = 0  # 0不搜索 1快速搜索 2高级搜索

        self.ui.SearchBox_1.currentTextChanged['QString'].connect(self.onSearchByX)

        # 宿管表
        self.managerTable = self.ui.Mtable
        self.tableListM = []  # Manager
        self.tableIndexM = {}  # Manager -> Item
        self.managerTable.itemSelectionChanged.connect(self.onSelectManager)
        self.managerTable.activated.connect(self.onEditM)

        width = [125, 125, 125, 125, 125]
        [self.managerTable.setColumnWidth(i, width[i]) for i in range(5)]
        self.searchModeM = 0  # 0不搜索 1快速搜索 2高级搜索

        self.ui.SearchBox_3.currentTextChanged['QString'].connect(self.onSearchByM)

        # 宿舍表
        self.susheTable = self.ui.ShusheTable
        self.tableListS = []  # Sushe
        self.tableIndexS = {}  # Sushe -> Item
        self.susheTable.itemSelectionChanged.connect(self.onSelectSushe)
        self.susheTable.activated.connect(self.onEditS)

        width = [92, 92, 92, 92, 92, 200]
        [self.susheTable.setColumnWidth(i, width[i]) for i in range(5)]
        self.searchModeS = 0  # 0不搜索 1快速搜索 2高级搜索

        self.ui.SearchBox_2.currentTextChanged['QString'].connect(self.onSearchByS)

        self.onSearchByM("工号")
        self.onSearchByS("楼号")
        self.onSearchByX("学号")

    def onSearchByX(self, searchByX):
        print('学生',searchByX)
        from Control.Student import attributeListX as attrs
        for attr, translate in attrs:
            if searchByX == translate:
                self.quickSearchByX = attr
        self.onQuickSearchX()

    def onSearchByM(self, searchByM):
        #print('suguan')
        from Control.Manager import attributeListM as attrs
        for attr, translate in attrs:
            if searchByM == translate:
                self.quickSearchByM = attr
        self.onQuickSearchM()

    def onSearchByS(self, searchByS):
       # print('sushe')
        from Control.Dormitory import attributeListS as attrs
        for attr, translate in attrs:
            if searchByS == translate:
                self.quickSearchByS = attr
        self.onQuickSearchS()

    def onQuickSearchS(self):
       # print('sushe')
        key = self.ui.SearchEdit_2.text()

        print('Skey',key)
        key = ' '.join(key.split())


        result = public.susheManager.search(self.quickSearchByS, key)
        self.tableShowS(result)

    def onQuickSearchX(self):
       # print('xuesheng')
        key = self.ui.SearchEdit_1.text()
        print("Xkey",key)
        key = ' '.join(key.split())
        print(self.quickSearchByX)
        result = public.studentManager.search(self.quickSearchByX, key)
        #print('学生',result)
        self.tableShowX(result)

    def onQuickSearchM(self):
        #print('suguan')
        key = self.ui.SearchEdit_3.text()
        print('Mkey',key)
        key = ' '.join(key.split())

        result = public.suguangManager.search(self.quickSearchByM, key)
        self.tableShowM(result)

    def onSearchSTU(self):#搜索学生
        def _onSaerch(keyList):
            result = public.studentManager.multiSearch(keyList)
            self.tableShowX(result)

        self._saerchBox = StuboxUI.SearchBox(_onSaerch)
        self._saerchBox.show()

    def onSearchM(self):
        def _onSaerch(keyList):
            result = public.suguangManager.multiSearch(keyList)
            self.tableShowM(result)

        self._saerchBox = MboxUI.SearchBox(_onSaerch)
        self._saerchBox.show()

    def onSearchS(self):
        def _onSaerch(keyList):
            result = public.susheManager.multiSearch(keyList)
            self.tableShowS(result)

        self._saerchBox = DorboxUI.SearchBox(_onSaerch)
        self._saerchBox.show()

    def onAddStudentX(self):
        def _onAddStudentX(_student):
            student = _student.copy()
            public.studentManager.add(student)
            self.tableSetX(student)

        self._newBox = StuboxUI.NewBox(_onAddStudentX)
        self._newBox.show()

    def onAddStudentM(self):
        def _onAddManager(_manager):
            manager = _manager.copy()
            public.suguangManager.add(manager)
            self.tableSetM(manager)

        self._newBox = MboxUI.NewBox(_onAddManager)
        self._newBox.show()

    def onAddStudentS(self):
        def _onAddSusheManager(_sushe):
            sushe = _sushe.copy()
            public.susheManager.add(sushe)
            self.tableSetS(sushe)

        self._newBox = DorboxUI.NewBox(_onAddSusheManager)
        self._newBox.show()

    def onDeleteX(self):
        student = self.selectionX
        if not student:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "删除档案", "确认删除此档案?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.tableIndexX[student]
            n = self.studentTable.topLevelItemCount()
            for i in range(0, n):
                if self.studentTable.topLevelItem(i) == item:
                    self.studentTable.takeTopLevelItem(i)
                    self.tableListX.remove(student)
                    self.tableIndexX.pop(student)
                    break
            public.studentManager.delete(student)

    def onDeleteM(self):
        manager = self.selectionM
        if not manager:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "删除档案", "确认删除此档案?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.tableIndexM[manager]
            n = self.managerTable.topLevelItemCount()
            for i in range(0, n):
                if self.managerTable.topLevelItem(i) == item:
                    self.managerTable.takeTopLevelItem(i)
                    self.tableListM.remove(manager)
                    self.tableIndexM.pop(manager)
                    break
            public.suguangManager.delete(manager)

    def onDeleteS(self):
        sushe = self.selectionS
        if not sushe:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "删除档案", "确认删除此档案?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.tableIndexS[sushe]
            n = self.susheTable.topLevelItemCount()
            for i in range(0, n):
                if self.susheTable.topLevelItem(i) == item:
                    self.susheTable.takeTopLevelItem(i)
                    self.tableListS.remove(sushe)
                    self.tableIndexS.pop(sushe)
                    break
            public.susheManager.delete(sushe)

    def onEditX(self):
        student = self.selectionX
        if not student:
            return

        def _onEditX(_student):
            public.studentManager.delete(student)
            _student.copyTo(student)
            public.studentManager.add(student)

            if student in self.tableIndexX:
                self.tableSetX(student, self.tableIndexX[student])

        self._editBox = StuboxUI.EditBox(student, _onEditX)
        self._editBox.show()

    def onEditM(self):
        manager = self.selectionM
        if not manager:
            return

        def _onEditM(_manager):
            if _manager.MID != manager.MID:
                public.suguangManager.delete(manager)
                _manager.copyTo(manager)
                public.suguangManager.add(manager)
            else:
                _manager.copyTo(manager)
                public.suguangManager.edit(manager)
            if manager in self.tableIndexM:
                self.tableSetM(manager, self.tableIndexM[manager])

        self._editBox = MboxUI.EditBox(manager, _onEditM)
        self._editBox.show()

    def onEditS(self):
        sushe = self.selectionS
        if not sushe:
            return

        def _onEditS(_sushe):
            if _sushe.Dor != sushe.Dor and _sushe.DID != sushe.DID:
                public.suguangManager.delete(sushe)
                _sushe.copyTo(sushe)
                public.susheManager.add(sushe)
            else:
                _sushe.copyTo(sushe)
                public.susheManager.edit(sushe)
            if sushe in self.tableIndexS:
                self.tableSetS(sushe, self.tableIndexS[sushe])

        self._editBox = DorboxUI.EditBox(sushe, _onEditS)
        self._editBox.show()

    def setStudentInfo(self, student=None):
        student = student or public.studentManager.emptyStu
        self.SIDlable.setText(student.SID)
        self.Snamelabel.setText(student.Sname)
        self.Ssexlabel.setText(student.getSex())
        self.hethdaylabel.setText(student.isHethday)
        self.ishethlabel.setText(student.isHeth)
        self.Dorlabel.setText(str(student.Dor))
        self.DIDlabel.setText(str(student.DID))
        self.MIDlabel.setText(student.MID)

    def setManagerInfo(self, manager=None):
        manager = manager or public.suguangManager.emptyManager
        self.MIDLabel_1.setText(manager.MID)
        self.MnameLabel_1.setText(manager.Mname)
        self.Msexlabel.setText(manager.getSex())
        self.Magelabel.setText(str(manager.Mage))
        self.MphoneLabel.setText(manager.Mphone)

    def setSusheInfo(self, sushe=None):
        sushe = sushe or public.susheManager.emptyDor
        self.LnoLabel_1.setText(sushe.Dor)
        self.SnoLabel_2.setText(sushe.DID)
        self.K_nLabel.setText(str(sushe.K_n))
        self.C_nlabel.setText(str(sushe.C_n))
        self.L_nlabel.setText(str(sushe.L_n))

    def show(self):
        self.dialog.show()

    def tableShowX(self, studentList):
        self.tableClearX()
        for student in studentList:
            self.tableAddX(student)
        self.onSelectStudent()

    def tableShowM(self, MList):
        self.tableClearM()
        for manager in MList:
            print(2)
            self.tableAddM(manager)
        self.onSelectManager()

    def tableShowS(self, SList):
        self.tableClearS()
        print(SList)
        for sushe in SList:
            self.tableAddS(sushe)
        self.onSelectSushe()

    def tableAddX(self, student):
        item = QtWidgets.QTreeWidgetItem(self.studentTable)
        self.tableSetX(student, item)
        self.tableListX.append(student)
        self.tableIndexX[student] = item

    def tableAddM(self, manager):
        item = QtWidgets.QTreeWidgetItem(self.managerTable)
        self.tableSetM(manager, item)
        self.tableListM.append(manager)
        self.tableIndexM[manager] = item

    def tableAddS(self, sushe):
        item = QtWidgets.QTreeWidgetItem(self.susheTable)
        self.tableSetS(sushe, item)
        self.tableListS.append(sushe)
        self.tableIndexS[sushe] = item

    def tableSetX(self, student, item=None):
        if item:
            item.setText(0, student.SID)
            item.setText(1, student.Sname)
            item.setText(2, student.getSex())
            item.setText(3, str(student.isHethday))
            item.setText(4, str(student.isHeth))
            item.setText(5,student.Dor)
            item.setText(6, student.DID)
            item.setText(7, student.MID)
        elif self.searchModeX == 0:
            self.tableAddX(student)

    def tableSetM(self, manager, item=None):
        if item:
            item.setText(0, manager.MID)
            item.setText(1, manager.Mname)
            item.setText(2, manager.getSex())
            item.setText(3, str(manager.Mage))
            item.setText(4, manager.Mphone)
        elif self.searchModeM == 0:
            self.tableAddM(manager)

    def tableSetS(self, sushe, item=None):
        if item:
            item.setText(0, sushe.Dor)
            item.setText(1, sushe.DID)
            item.setText(2, str(sushe.L_n))
            item.setText(3, str(sushe.C_n))
            item.setText(4, str(sushe.K_n))


        elif self.searchModeS == 0:
            self.tableAddS(sushe)

    def tableClearX(self):
        self.studentTable.clear()
        self.tableListX.clear()
        self.tableIndexX.clear()

    def tableClearM(self):
        self.managerTable.clear()
        self.tableListM.clear()
        self.tableIndexM.clear()

    def tableClearS(self):
        self.susheTable.clear()
        self.tableListS.clear()
        self.tableIndexS.clear()

    def onSelectStudent(self):
        item = self.studentTable.selectedItems()
        selected = True if item else False
        selection = None
        if selected:
            for k, v in self.tableIndexX.items():
                if v == item[0]:
                    selection = k
                    break
            else:
                selected = False
        self.selectionX = selection
        self.setStudentInfo(selection)
        self.ui.editButton_1.setEnabled(selected)
        self.ui.DeleteButton_1.setEnabled(selected)

    def onSelectManager(self):
        item = self.managerTable.selectedItems()
        selected = True if item else False
        selection = None
        if selected:
            for k, v in self.tableIndexM.items():
                if v == item[0]:
                    selection = k
                    break
            else:
                selected = False
        self.selectionM = selection
        self.setManagerInfo(selection)
        self.ui.editButton_3.setEnabled(selected)
        self.ui.DeleteButton_3.setEnabled(selected)

    def onSelectSushe(self):
        item = self.susheTable.selectedItems()
        selected = True if item else False
        selection = None
        if selected:
            for k, v in self.tableIndexS.items():
                if v == item[0]:
                    selection = k
                    break
            else:
                selected = False
        self.selectionS = selection
        self.setSusheInfo(selection)
        self.ui.editButton_2.setEnabled(selected)
        self.ui.DeleteButton_2.setEnabled(selected)
