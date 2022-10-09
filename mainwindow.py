import sys
from PyQt5.QtWidgets import QApplication,QWidget
from mainUI import mainwindow
import public
from  QcureUi import cure
from Control.Dormitory import DorManager
from Control.Manager import MManager
from Control.Student import StduentManager
if __name__ == '__main__':
    app=QApplication(sys.argv)
    public.studentManager = StduentManager()
    public.suguangManager = MManager()
    public.susheManager = DorManager()
    w=cure.Windows(mainwindow(),'NAME',r"C:\Users\12424\Pictures\Saved Pictures\2022-02-14-16-37-51.jpg",'blue','隔离宿舍管理系统','images/favicon.ico')

    sys.exit(app.exec_())
