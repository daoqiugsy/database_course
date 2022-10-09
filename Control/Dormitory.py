import sql

# 宿管属性集
attributeListS = [
    ("Dor", "楼号"),
    ("DID", "宿舍号"),
    ("L_n", "入住人数"),
    ("C_n", "剩余空位"),
    ("K_n", "可容纳人数"),
]


class DorManager(object):
    """宿舍管理类, 单例"""

    def __init__(self):
        # 用于存储所有宿舍对象
        self.SList = []
        # 楼号+宿舍号 -> 宿舍对象
        self.SLSID = {}

        self.load()

        self.emptyDor = DOR()

    def add(self, Dor):
        self.SList.append(Dor)
        self.SLSID[Dor.Dor + Dor.DID] = Dor
        sql.Dor_add(Dor)

    def edit(self, Dor):
        sql.Dor_edit(Dor)
        return True

    def delete(self, Dor):
        self.SLSID.pop(Dor.Dor + Dor.DID)
        self.SList.remove(Dor)
        sql.Dor_delete(Dor)
        return True

    def multiSearch(self, keyList):
        # print(keyList)
        searchBy = []
        keyText = []
        # print(keyList)
        for searchby, keytext in keyList:
            if keytext:
                searchBy.append(searchby)
                keyText.append(keytext)
        msg = sql.Dor_multiselect(searchBy, keyText)
        # print(searchBy)
        # print(keyText)
        result = self.toDor(msg)
        return result

    def search(self, searchBy, keyList):
        # print(searchBy)
        result = []
        if not keyList:
            result = self.load()
            return result
        else:
            msg = sql.Dor_select(searchBy, keyList)
            result = result + self.toDor(msg)
            # print(result)
            return result

    def toDor(self, msg):
        result = []
        for i in range(len(msg)):
            # 创建每一个数据的Dor对象
            m = msg[i]
            # print(s)
            Dor = DOR()
            Dor.Dor = m[0]
            Dor.DID = m[1]
            Dor.L_n = m[2]
            Dor.C_n = m[3]
            Dor.K_n = m[4]
            result.append(Dor)
        return result

    def load(self):
        SList = []
        SLSID = {}
        try:
            msg = sql.Load("dor_table")
            result = self.toDor(msg)
            for Dor in result:
                SList.append(Dor)
                SLSID[Dor.DID + Dor.Dor] = Dor
            result = True
        except:
            result = False
        finally:
            self.SList = SList
            self.SLSID = SLSID

        # print(self.MMID)
        # print(self.MList)
        return SList


class DOR(object):


    def __init__(self, Dor="", DID="", L_n="", C_n="", K_n=""):
        self.Dor = Dor
        self.DID = DID
        self.L_n = L_n
        self.C_n = C_n
        self.K_n = K_n


    def copy(self):
        dor = DOR()
        self.copyTo(dor)
        return dor

    def copyTo(self, dor):
        dor.Dor = self.Dor
        dor.DID = self.DID
        dor.L_n = self.L_n
        dor.C_n = self.C_n
        dor.K_n = self.K_n


    def checkInfo(self, new=False):
        '''检查自身信息是否完整合法'''
        # 空值检测
        for attr, text in attributeListS:
            if not getattr(self, attr):
                return (False, "%s不能为空" % text)
        # 重复性检测
        check = sql.checkDOR(self, new)
        if check[0] == 0:
            return check

        return (True, "")
