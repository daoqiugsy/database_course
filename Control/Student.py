import  sql
attributeListX = [
    ("SID", "学号"),
    ("Sname", "姓名"),
    ("Ssex", "性别"),
    ("isHethday", "绿码天数天数"),
    ("isHeth", "是否阳性"),
    ("Dor", "楼号"),
    ("DID", "宿舍号"),
    ("MID", "工作人员ID"),
]


class Student(object):  # 学号，姓名，性别，健康码正常天数，宿舍楼，是否健康，宿舍号，宿管ID
    def __init__(self, SID='', Sname='', Ssex=0, isHethday='', isHeth='',Dor='',  DID='', MID=''):
        self.SID = SID
        self.Sname = Sname
        self.Ssex = Ssex
        self.isHethday = isHethday
        self.Dor = Dor
        self.isHeth = isHeth
        self.DID = DID
        self.MID = MID

    def getSex(self):
        return ["", "男", "女"][self.Ssex]

    def copy(self):
        student = Student()
        self.copyTo(student)
        return student

    def copyTo(self, student):
        student.SID = self.SID
        student.Sname = self.Sname
        student.Ssex = self.Ssex
        student.isHethday = self.isHethday
        student.Dor = self.Dor
        student.isHeth = self.isHeth
        student.DID = self.DID
        student.MID = self.MID

    def checkInfo(self, new=False):  # """信息合法检查"""
        for attr, word in attributeListX:
            print(attr,word)
            if not getattr(self, attr):
                return (False, word + "不能为空")
        # 重复性检测
        check = sql.checkSTU(self.SID, self.Dor,self.DID,self.MID,new)
        if check[0]==0:
            return check
        return (True,"")


class StduentManager(object):
    def __init__(self):
        # 储存所有学生对象
        self.studentList = []
        # 学号为集合
        self.studentSID = {}
        # 读入学生信息
        self.load()
        # 空学生对象
        self.emptyStu = Student()

    # 增
    def add(self, student):
        print(student.SID)
        self.studentList.append(student)
        self.studentSID[student.SID] = student
        sql.student_add(student)
    def delete(self,student):
        self.studentList.remove(student)
        self.studentSID.pop(student.SID)
        sql.student_delete(student)
    def multiSearch(self,keyList):#高级搜索
        searchBy = []
        keyText = []
        for searchby, keytext in keyList:
            if keytext:
                searchBy.append(searchby)
                keyText.append(keytext)
        msg = sql.student_multiselect(searchBy, keyText)

        result = self.tostudent(msg)
        return result
    def search(self,searchBy,KeyList):#搜索
        result = []
        if not KeyList:
            result = self.load()
            return result
        else:
            msg = sql.student_select(searchBy,  KeyList)
            result = result + self.tostudent(msg)
            # print(result)
            return result
    def tostudent(self,msg):#展示学生数据
        result = []
        for i in range(len(msg)):
            # 创建每一个数据的student对象
            s = msg[i]
            # print(s)
            student = Student()
            student.SID = s[0]
            student.Sname = s[1]
            student.Ssex = s[2]
            student.isHethday = s[3]
            student.isHeth = s[4]
            student.Dor = s[5]
            student.DID = s[6]
            student.MID = s[7]
            result.append(student)
        #print('result',result)
        return result
    def load(self):
        studentList=[]
        studentSID={}
        try:
            msg=sql.Load("stutable")
            print("msg",msg)
            result=self.tostudent(msg)
            for student in result:
                studentList.append(student)
                studentSID[student.SID]=student
            result=True
        except:
            result = False
        finally:
            self.studentList = studentList
            self.studentSID = studentSID

        return studentList


