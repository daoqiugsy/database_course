import pymysql


def open():
    db = pymysql.connect(host='localhost', user='root', password='2001928', charset='utf8', db='newdb')
    return db


def student_add(student):
    db = open()
    cursor = db.cursor()
    sql1 = """insert into stutable(SID,Sname,Ssex,isHethday,isHeth,Dor,DID,MID)
                    values ("{}","{}",{},"{}","{}","{}","{}","{}")""".format(student.SID, student.Sname, student.Ssex,
                                                                             student.isHethday, student.isHeth,
                                                                             student.Dor, student.DID, student.MID,
                                                                             )
    sql2 = "update dor_table set C_n = C_n-1,L_n = L_n+1 where Dor = {} and DID = {}".format(student.Dor, student.DID)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('学生增加失败', e)
    else:
        db.commit()  # 事务提交
        print('增加学生成功', cursor.rowcount)
    # 关闭数据库连接
    db.close()


def checkSTU(SID, Dor, DID, MID, new):
    # 检查学生正确性
    flag = True
    msg = ''
    db = open()
    cursor = db.cursor()
    sql1 = "select MID from m_table where MID = {}".format(MID)
    sql2 = "select SID from stutable where SID = {}".format(SID)
    sql3 = "select C_n from dor_table where Dor = {} and DID = {}".format(Dor, DID)
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    cursor.execute(sql2)
    results2 = cursor.fetchall()
    cursor.execute(sql3)
    results3 = cursor.fetchall()
    if results1 == ():
        msg += '没有该工作人员、'
        flag = False
    if results3 == ():
        msg += "没有该工作人员、"
        flag = False
    if results3 != () and results3[0] == 0:
        msg += "该宿舍已满、"
        flag = False
    if results2 != () and new:
        msg += "学号重复、"
        flag = False
    db.close()
    return (flag, msg)


def student_delete(student):
    #删除学生
    db = open()
    cursor = db.cursor()
    sql1 = "delete from stutable where SID = {}".format(student.SID)
    sql2 = "update dor_table set C_n = C_n+1,L_n = L_n-1 where Dor = {} and DID = {}".format(student.Dor, student.DID)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
        cursor.execute(sql2)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('删除学生失败', e)
    else:
        db.commit()  # 事务提交
        print('删除学生成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()


def student_select(seachby, keyList):
    # 学生单属性查询
    db = open()
    cursor = db.cursor()
    sql1 = "select * from stutable where {} REGEXP '{}' ".format(seachby, keyList)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        results = ()
        db.rollback()  # 事务回滚
        print('查询学生失败', e)
    else:
        results = cursor.fetchall()
        print('查询学生成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()
    return results


def student_multiselect(seachby, keyList):
    # 学生多属性查询
    db = open()
    cursor = db.cursor()
    sql1 = "select * from stutable "
    for i in range(len(seachby)):
        if i == 0:
            sql1 = sql1 + "where {} REGEXP '{}' ".format(seachby[i], keyList[i])
        else:
            sql1 = sql1 + "and {} REGEXP '{}' ".format(seachby[i], keyList[i])
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        results = ()
        db.rollback()  # 事务回滚
        print('查询学生失败', e)
    else:
        results = cursor.fetchall()  # 一次获取所有数据
        print('查询学生成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()
    return results
#多属性查询

# def student_edit(student):
# db=open()
##cursor=db.cursor()
# sql1="""update stutable set """
def Load(table):
    db = open()
    cursor = db.cursor()  # 创建游标对象
    sql = "select * from {}".format(table)

    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()  # 一次读取所有数据
    # 关闭数据库连接
    db.close()  # 断开数据库释放资源
    return results


def checkM(MID, new):
    # 检查宿管正确性
    flag = True
    msg = ''
    db = open()
    cursor = db.cursor()
    sql = "select MID from m_table where MID = {}".format(MID)
    cursor.execute(sql)
    results1 = cursor.fetchall()
    if results1 != () and new:
        msg += '已有该宿管'
        flag = False
    db.close()
    return (flag, msg)


def manager_add(manager):
    # 增加宿管
    db = open()
    cursor = db.cursor()
    sql1 = """insert into m_table(MID,Mname,Msex,Mage,Mphone)
                values ("{}","{}",{},"{}","{}")""".format(manager.MID, manager.Mname, manager.Msex, manager.Mage,
                                                          manager.Mphone)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('增加宿管失败', e)
    else:
        db.commit()  # 事务提交
        print('增加宿管成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()


def manager_edit(manager):
    # 更改宿管
    db = open()
    cursor = db.cursor()
    sql1 = """update m_table set Mname = "{}",Msex= {},Mage = {},Mphone = "{}" where MID = "{}" """.format(
        manager.Mname, manager.Msex, manager.Mage, manager.Mphone, manager.MID)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('更改宿管失败', e)
    else:
        db.commit()  # 事务提交
        print('更改宿管成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()


def manager_delete(manager):
    db = open()
    cursor = db.cursor()
    sql1 = "delete from m_table where MID = {}".format(manager.MID)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('删除宿管失败', e)
    else:
        db.commit()  # 事务提交
        print('删除宿管成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()


def manager_select(seachby, keyList):
    # 宿管单属性查询
    # print('manager')
    db = open()
    cursor = db.cursor()
    sql1 = "select * from m_table where {} REGEXP '{}' ".format(seachby, keyList)
    print(sql1)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        results = ()
        db.rollback()  # 事务回滚
        print('查询宿管失败', e)
    else:
        results = cursor.fetchall()
        print('查询宿管成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()
    return results


def manager_multiselect(seachby, keyList):
    # 宿管多属性查询
    db = open()
    cursor = db.cursor()
    sql1 = "select * from m_table "
    for i in range(len(seachby)):
        if i == 0:
            sql1 = sql1 + "where {} REGEXP '{}' ".format(seachby[i], keyList[i])
        else:
            sql1 = sql1 + "and {} REGEXP '{}' ".format(seachby[i], keyList[i])
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        results = ()
        db.rollback()  # 事务回滚
        print('查询宿管失败', e)
    else:
        results = cursor.fetchall()
        print('查询宿管成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()
    return results


def checkDOR(Dor, new):
    print('检查宿舍正确性')
    flag = True
    msg = ''
    db = open()
    cursor = db.cursor()
    sql1 = "select C_n,L_n,K_n from dor_table where Dor = '{}' and DID = '{}'".format(Dor.Dor, Dor.DID)
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    if results1 != () and new:
        msg += "已有该宿舍、"
        flag = False

    if (int(Dor.L_n) + int(Dor.C_n) )!= int(Dor.K_n):
        msg += '人数不对、'
        flag = False
    db.close()
    return (flag, msg)


def Dor_add(sushe):
    # 增加宿舍
    db = open()
    cursor = db.cursor()
    sql1 = """insert into dor_table(Dor,DID,L_n,C_n,K_n)
                values ({},{},{},{},{})""".format(sushe.Dor, sushe.DID, sushe.L_n, sushe.C_n, sushe.K_n)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('增加宿舍失败', e)
    else:
        db.commit()  # 事务提交
        print('增加宿舍成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()


def Dor_edit(sushe):
    # 更改宿舍
    db = open()
    cursor = db.cursor()
    sql1 = """update dor_table set L_n = {},C_n = {},K_n = {} where Dor = {} and DID = {} """.format(
        sushe.L_n, sushe.C_n, sushe.K_n, sushe.Dor, sushe.DID)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('更改宿舍失败', e)
    else:
        db.commit()  # 事务提交
        print('更改宿舍成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()


def Dor_delete(sushe):
    db = open()
    cursor = db.cursor()
    sql1 = "delete from dor_table where Dor = {} and DID={}".format(sushe.Dor, sushe.DID)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        db.rollback()  # 事务回滚
        print('删除宿舍失败', e)
    else:
        db.commit()  # 事务提交
        print('删除宿舍成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()


def Dor_multiselect(seachby, keyList):
    # 宿舍多属性查询
    db = open()
    cursor = db.cursor()
    sql1 = "select * from dor_table "
    for i in range(len(seachby)):
        if i == 0:
            sql1 = sql1 + "where {} REGEXP '{}' ".format(seachby[i], keyList[i])
        else:
            sql1 = sql1 + "and {} REGEXP '{}' ".format(seachby[i], keyList[i])
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        results = ()
        db.rollback()  # 事务回滚
        print('查询宿舍失败', e)
    else:
        results = cursor.fetchall()
        print('查宿舍管成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()
    return results


def Dor_select(seachby, keyList):
    # 宿舍单属性查询
    db = open()
    cursor = db.cursor()
    sql1 = "select * from dor_table where {} REGEXP '{}' ".format(seachby, keyList)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
    except Exception as e:
        results = ()
        db.rollback()  # 事务回滚
        print('查询宿舍失败', e)
    else:
        results = cursor.fetchall()
        print('查询宿舍成功', cursor.rowcount)

    # 关闭数据库连接
    db.close()
    return results
