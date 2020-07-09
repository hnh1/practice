'''
print("hello world!")  #字符串
print(2333)  #整数
print(2.3)  #小数
print(True)  #布尔值:True,False
print(False)
print(())  #元组
print([])  #数组
print({})  #字典  
"""
锄禾日当午
汗滴禾下土
"""
print("hahaha",2333,2.333)
print("haha"+"xixi")  #字符串的拼接（只能同样的类型进行拼接操作）
print("hahaha"*100)  #打印100个
print(((1+2)*100-9.9)/2)
print((1+1)==2)
print(2>3)
#变量，赋值
a="zhangsan" #把zhangsan这个值赋值给了a这个变量
print(a)
'''

# a=input("请输入a：")
# b=input("请输入b：")
# print("input获取的内容：",a+b)

#数据格式的转换
# print(type(2333))
# print(type("haha"))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a=str(2333)
# print(type(a))
# print(type(None))
# a = int("hahaha")
# print(type(a))
# print(int(2.33))

# a=float(input("请输入a:"))
# b=float(input("请输入b:"))
# print("获取input的内容：",a+b)
#print(str(None))
# print(len('aaaa'))
# a=input("输入a：")
# b=input("输入b：")
# print("a和b的长度和：",len(a)+len(b))

#元组，下标，从0开始编号（正着数），从-1开始（倒着数）
#a=() #空的元组
#a = (1,2,3,4,"haha","xixi",True,False,"haha","haha")
#print(a[-3])
#切片
#print(a[0:4])  #左闭右开
#print(a[4:9])
# print(a[9:])
# print(a[:4])
# print(a[:])
# print(a)

#print(a.index("haha"))
# print(a.count("haha"))
#二维元组
# b = (a,"haha",True,(123,4.5))
# print(b[3][0])

#数组
# a = [4,2.3,"haha","xixi","haha",True,False]
#print(a[2])
# a.append((1,2))
# a.append("append")
# a.insert(2,"append")
# b = a.pop(0) #剪切
# c = a.pop(0)
# print(b+c)
# print(a.index((1,2)))
# print(a.count("haha"))
#a.clear()  #清空
# xx = ["nihao","buhao"]
# a.extend(xx)
# print(a+xx)
# a.remove("haha") #删除
# print(a)
# xx = [1,True,0,False]
# b = xx.count(0)
# print(b)
# b = (2,3)
# xx = [b,1,2.3,4]
# print(xx[0][1])

#字典
# a = {
#     "name":"zhangsan",
#     0:"haha",
#     "age":25
#     }
#取值
#print(a["age"])
#新增
#a["height"] = "183cm"
#修改
#a["name"] = "lisi"
#print(a)
# print(a.get("name"))
# b = a.pop("name")
# print(b)
# print(a)
# a.update(height="132cm")
# a.update(name="lisi")
#print(a)
# print(a.get("name"))
# print(a["name"])
# print(a.get("name11"))
# print(a["name11"])

#数组和字典的删除 
# del a["name"]
# print(a)
# xx = [1,2.3]
# del xx[1]
# print(xx)

#获取用户输入的个人信息，并且存储到字典中（name,age,sex）
# name = input("请输入姓名：")
# age = int(input("请输入年龄："))
# sex = input("请输入性别：")
# a = {}
# a.update(name=name,age=age,sex=sex)
# a["name"] = name
# a["age"] = age
# a["sex"] = sex
# a = {"name":name,"age":age,"sex":sex}
# print(a)

#判断
# a = 1
# b = 2
# if a == 1:
#     print("hahaha")

# if a > b:
#     print("a比b大")  #前面是4个空格(缩进)，属于一个代码块
# else:
#     print("b比a大")

# age = int(input("请输入你的年龄:"))
# if age > 60:
#     print("你应该退休了")
# elif age > 30:
#     print("家庭的责任很重大")
# elif age > 20:
#     print("一定要好好规划你的未来") 
# else:
#     print("读书的时候要认真")
# if age > 20 and age <=30:
#     print("2222")
# elif age > 30:
#     print("3333")
# elif age > 60:
#     print("6666")
# else:
#     print("0000")

# a = "nihao"
# if a in "nihaojintian":  #字符串，字典，数组，元组
# if a in ["nihao","nibuhao"]:
#if a in ("nihao","nibuhao"):
#if a in {"niha":"nihao"}:  #字典的话是针对key相等
#     print("ok")
# else:
#     print("no ok")

# a = input("请输入:")
# if a == "":  #什么都不输入，直接回车
#     print("不能为空") 
#     exit()
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄")
#     exit()

# if a > 5:
#     print("da")
# else:
#     print("xiao")

# a = 10
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

#循环
# a = 1
# while a < 10:
#     print("hahaha",a)
#     a = a+2

#现在有10个学生的成绩需要录入到系统中，这10个人分别是：
#张三、李四、王麻子、李易峰、权志龙、李胜利、王晓红、李柱、二狗、浪晋，
#并且名字和成绩需要对应上(字典)，而且大于60的和小于60的需要分开存放（字典/数组/元组）
# studentlist = ["张三","李四","王麻子","李易峰","权志龙","李胜利","王晓红","李柱","二狗","浪晋"]
# highgrade = {}
# lowgrade = {}
# a = 0
# while a < len(studentlist):
#     grade = float(input("请输入"+studentlist[a]+"的成绩："))
#     if grade >=60:
#         highgrade[studentlist[a]] = grade
#     else:
#         lowgrade[studentlist[a]] = grade
#     a = a+1
# print("大于60的：",highgrade)
# print("小于60的：",lowgrade)

#for循环的原理：遍历
# a = "你好，今天你吃了吗？"
#a = ["张三","李四","王麻子","李易峰","权志龙","李胜利","王晓红","李柱","二狗","浪晋"]
# a = {"name":"zhansan","age":23}  #指的是key
# for i in a:
#     print(i)
#b = range(100)
#b = range(0,100) #自动生成了一个数列
# b = list(range(0,100))
# print(b)
# for i in range(0,100):
#     print(i)
# b = range(0,100,3)  #步进/步长
# for i in b:
#     print(i)

# studentlist = ["张三","李四","王麻子","李易峰","权志龙","李胜利","王晓红","李柱","二狗","浪晋"]
# highgrade = {}
# lowgrade = {}
# for i in studentlist:
#     grade = float(input("请输入"+i+"的成绩："))
#     if grade >=60:
#         highgrade[i] = grade
#     else:
#         lowgrade[i] = grade
# print("大于60的：",highgrade)
# print("小于60的：",lowgrade)


#打印九九乘法表：
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"×",j,"=",i*j,end="  ")  #end表示不换行，以end的值隔开
#     print() #换行

#练习1：通过print打印，模拟一个红绿灯的功能，红灯30次，绿灯35次，黄灯3次
#练习2：使用代码实现一个注册的功能，用户输入账号和密码，要求账号长度是5-8位，密码8-12位，并且账号必须小写字母开头，储存到字典中
# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有：",light[i]-j,"秒")

# name = input("请输入账号：")
# pwd = input("请输入密码：")
# if len(name) >= 5 and len(name) <= 8:
#     # if name[0] in "qwertyuiopasdfghjklzxcvbnm":
#     if name[0] >= "a" and name[0] <= "z":
#         if len(pwd) >=8 and len(pwd) <=12:
#             print("注册成功",{name:pwd})
#         else:
#             print("密码的长度不符合规范，密码8-12位")
#     else:
#         print("账号必须以小写字母开头")
# else:
#     print("账号的长度不符合规范，请输入5-8位的账号")

# for i in range(10):
#     if i == 4:
#         continue
#         #break
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         if i ==3:
#             break  #只跳出了一层循环
#         print(i,"×",j,"=",i*j,end="  ")  #end表示不换行，以end的值隔开
#     print() #换行

#方法（函数）
# def checkname(username):   #方法的声明 方法的名字（方法的参数）
#     """自动的判断账号长度是5-8位，并且账号必须小写字母开头"""    #方法的说明
#     if len(username) >=5 and len(username) <= 8:   #方法的逻辑代码
#         if username[0] >= "a" and username[0] <= "z":
#             print("ok")
#         else:
#             print("账号必须小写字母开头")
#     else:
#         print("账号长度是5-8位")
# checkname("asd")

# def jiafa(a,b):
#     """相加"""
#     if type(a) is int and type(b) is int:
#     # if type(a) == type(b):
#         # print(a+b)
#         return a+b
#     else:
#         print("输入的数据类型不正确")
# jiafa("23",88)
#返回值，返回后我们可以对这个值做其他的操作，而print不能
#a = []
#print(a.append("haha"))   #None
#print(a.count("haha"))    #1
# print(jiafa(1,1))    #None  #2:返回值
# print(jiafa(1,"1"))  #None

# a = [1,2,3,4,5,6,7]
# x = a.index(2)
# print(a[x])

# def checkname(username):   #方法的声明 方法的名字（方法的参数）
#     """自动的判断账号长度是5-8位，并且账号必须小写字母开头"""    #方法的说明
#     if len(username) >=5 and len(username) <= 8:   #方法的逻辑代码
#         if username[0] >= "a" and username[0] <= "z":
#             return True
#         else:
#             return "账号必须小写字母开头"
#     else:
#         return "账号长度是5-8位"

# username = input("请输入你的账号：")
# password = input("请输入你的密码：")
# if checkname(username) == True:
#     if len(password) >= 8 and len(password) <= 12:
#         print("注册成功",{username:password})
#     else:
#         print("密码必须8-12位")
# else:
#     print(checkname(username))
    
# try:
#     print(2+jskl)
# except Exception as e:
#     print("上面的代码写错了",e)

#异常类  
#包-》类-》方法-》变量
#既包含，又并列
#处理用户输入的数据
# a = input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try:
#     if int(b) > 18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确的年龄")

"""
定义一个方法，用来判断用户输入的账号密码是否符合规范（账号长度是5-8位，并且账号必须小写字母开头；密码8-12位）
"""
# name = input("请输入账号：")
# pwd = input("请输入密码：")
# def check(name,pwd):
#     if len(name) >= 5 and len(name) <= 8:
#         if name[0] >= "a" and name[0] <= "z":
#             if len(pwd) >= 8 and len(pwd) <= 12:
#                 return True
#             else:
#                 return "密码8-12位"
#         else:
#             return "账号必须小写字母开头"
#     else:
#         return "账号长度是5-8位"
# print(check(name,pwd))
    

# import time  #包,写在py文件的最上方
# import random
# import pymysql
# # for i in range(10):
# #     time.sleep(1)
# #     print(i)
# #print(random.randint(100,1000))
# db = pymysql.connect(host="localhost",user="root",password="",db="testdb")
# cur = db.cursor()
# try:
#     cur.execute("select * from t_class;")
#     res = cur.fetchall()
#     print(res)
# except:
#     print("sql语句错误")

"""
class声明类的名字，类的名字的首字母必须大写
面向对象编程
类里面所有的方法，都必须要传一个参数，叫self
"""
# class GirlFriend():
#     """
#     女朋友
#     """
#     def __init__(self,sex,height,weight,hair,age):
#         self.sex=sex
#         self.height=height
#         self.weight=weight
#         self.hair=hair
#         self.age=age
    
#     def caiyi(self,num):
#         """
#         才艺表演
#         """
#         print("你性别"+self.sex+"身高为"+self.height+"体重为"+self.weight+"头发为"+self.hair+"年龄为"+self.age+"开始了自己的才艺表演")
#         if num == 1:
#             print("胸口碎大石")
#         elif num == 2:
#             print("唱跳rap篮球")
#         else:
#             print("单手开瓶盖")
    
#     def chuyi(self):
#         """
#         厨艺持家
#         """
#         print("精通八大菜系，中外融合，啥都会做")

#     def work(self):
#         """
#         工作挣钱
#         """
#         print("你性别"+self.sex+"身高为"+self.height+"体重为"+self.weight+"头发为"+self.hair+"年龄为"+self.age+"开始了自己的工作")
#         print("开挖掘机")

# #类的实例化
# zhangsan = GirlFriend("男","170cm","55kg","黑长直","18岁")
# zhangsan.caiyi(2)
# zhangsan.chuyi()
# zhangsan.work()
# print(zhangsan.sex)

# class Car():
#     def __init__(self,pinpai,color,neishi,jilun):
#         self.pinpai=pinpai
#         self.color=color
#         self.neishi=neishi
#         self.jilun=jilun 
    
#     def bianxing(self):
#         print("车子变身为金刚葫芦娃")
    
#     def fly(self):
#         print("车子开始起飞")

# zhangsan =  Car("奥拓","五颜六色","豪华","独轮车")
# zhangsan.bianxing()
# zhangsan.fly()

# class Nvpengyou(GirlFriend): #GirlFriend是父类，Nvpengyou是子类
#     def work(self): #对类的重写
#         print("修电脑")
# #object是所有类的祖宗
# zhangsan = Nvpengyou("女","170cm","56kg","短发","25岁")
# zhangsan.work()

# import time
# now = time.strftime("%Y-%m-%d %H:%M:%S")
# #文件的读写
# text = input("请输入今天的心情：")
# # with open("日记.txt","w",encoding="utf-8") as f:  #默认的编码是GBK，需要把编码设置为UTF-8，w是完全重写内容
# #     f.write(text)
# # with open("日记.txt","a",encoding="utf-8") as f:  # a是追加内容
# with open("e:\日记.txt","a",encoding="utf-8") as f:  # a是追加内容
#     f.write(now+"\n")
#     f.write(text+"\n")
#     f.write("-----------------"+"\n")

# print("haha\nhaha")

#读
# with open("e:\日记.txt","r",encoding="utf-8") as r:
#     content = r.readlines()
# for i in content:
#     print(i)












