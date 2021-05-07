# # -----------------------------------------------------------------------------------------------------
# # ----------------------------------------

# # class tanımlama
# class Ogrenci:
#     pass

# # nesne türetme
# ogrenci = Ogrenci()

# # ----------------------------------------

# # __init__ => constructor method
# class Product:
#     def __init__(self):
#         self.name = "ürün oluşturuldu"

# p1 = Product()
# p2 = Product()

# print(p1.name, p2.name)

# # ----------------------------------------

# class Product:
#     def __init__(self, name, price, isActive = False): # constructor'a parametre gönderme
#         self.name = name
#         self.price = price
#         self.isActive = isActive
#         print("ürün oluşturuldu")

# p1 = Product("samsung", 10000)
# p2 = Product("IPhone", 12000)

# print(p1.name, p1.price, p1.isActive)
# print(p2.name, p2.price, p2.isActive)

# # -----------------------------------------------------------------------------------------------------

# # çalışma sorusu

# class Comment:
#     def __init__(self, userName, text, likes, dislikes):
#         self.userName = userName
#         self.text = text
#         self.likes = likes
#         self.dislikes = dislikes

# comm1 = Comment("ali", "güzel müzik", 5, 0)
# comm2 = Comment("ahmet", "beğenmedim bu nedir", 2, 5)
# comm3 = Comment("mehmet", "deli fişek", 10, 0)
# comm4 = Comment("ayşe", "bele vaziyete", 1, 3)
# comm5 = Comment("fatma", "efsane", 7, 2)

# comments = [comm1, comm2, comm3, comm4, comm5]

# for comm in comments:
#     print(comm.text)

# # -----------------------------------------------------------------------------------------------------

# # çalışma sorusu 2

# class Person:
#     def __init__(self, name, surName, year):
#         self.name = name
#         self.surName = surName
#         self.year = year
    
#     def intro(self):
#         return f"Benim adım : {self.name}, soyadım : {self.surName}"

#     def calculateAge(self):
#         return 2021 - self.year
    
# p1 = Person("Harun", "Calis", 2000)
# p2 = Person("Betül", "Calis", 2003)
# print(p1.intro())
# print(p2.intro())
# print(p1.calculateAge())
# print(p2.calculateAge())

# # -----------------------------------------------------------------------------------------------------

# # çalışma sorusu 3

# class BankAccount:
#     def __init__(self, owner) -> None:
#         self.owner = owner
#         self.balance = 0.0

#     def deposit(self, miktar):
#         self.balance += miktar
#         return self.balance

#     def withDraw(self, miktar):
#         self.balance -= miktar
#         return self.balance

# musteri = BankAccount("Harun Calis")

# print(musteri.deposit(1000))
# print(musteri.withDraw(250))
# print(musteri.balance)

# # -----------------------------------------------------------------------------------------------------

# # init ile değil class seviyesinde değişken tanımlama
# class User:
#     activeUsers = 0 # *** her nesne oluştuğunda sıfırdan başlamaz bu class için bir defa oluşturulur ve kalır ***
#     def __init__(self, name, surName):
#         self.name = name
#         self.surName = surName
#         User.activeUsers += 1 # class seviyesindeki değişkene class ismi ile ulaşılır

#     def fullName(self):
#         return self.name + " " + self.surName

#     def logOut(self):
#         User.activeUsers -= 1
#         print(f"{self.fullName()} çıkış yaptı.")

# print(User.activeUsers)
# kullanici1 = User("harun", "calis")
# kullanici2 = User("betül", "calis")
# kullanici3 = User("yusuf", "calis")
# print(User.activeUsers)
# kullanici3.logOut()
# print(User.activeUsers)

# # -----------------------------------------------------------------------------------------------------

# # class seviyesinde method oluşturma
# class User:
#     activeUsers = 0

#     @classmethod # decorater
#     def displayActiveUsers(cls): # self parametresi almadı
#         print(f"{cls.activeUsers} kişi aktif.")

#     @classmethod
#     def fromString(class, dataStr):
#         name, surName, age = dataStr.split(",")
#         return class(name, surName, age)

#     def __init__(self, name, surName, age):
#         self.name = name
#         self.surName = surName
#         self.age = age
#         User.activeUsers += 1
    
#     def fullName(self):
#         return self.name + " " + self.surName

#     def logOut(self):
#         User.activeUsers -= 1
#         print(f"{self.fullName()} çıkış yaptı.")

# print(User.displayActiveUsers())
# kullanici1 = User("harun", "calis", 21)
# kullanici2 = User("betül", "calis", 18)
# kullanici3 = User("yusuf", "calis", 13)
# print(User.displayActiveUsers())
# kullanici3.logOut()
# print(User.displayActiveUsers())
# kullanici4 = User.fromString("burak berk,akdemir,20")
# print(User.displayActiveUsers())

# # -----------------------------------------------------------------------------------------------------

# # çalışma sorusu 4

# class Question:
#     def __init__(self, text, choices, answer):
#         self.text = text
#         self.choices = choices
#         self.answer = answer

#     def checkAnswer(self, ans):
#         if ans not in self.choices:
#             raise ValueError("şıklarda bu yok :/")
#         return self.answer == ans

# class Quiz:

#     def __init__(self, questions):
#         self.questions = questions
#         self.questionIndex = 0
#         self.score = 0

#     def getQuestion(self):
#         return self.questions[self.questionIndex]

#     def displayQuestion(self):
#         self.displayProgress()
#         soru = self.getQuestion()
        
#         print(f"soru {self.questionIndex + 1} : {soru.text}")
#         for c in soru.choices:
#             print("-" + c)
        
#         ans = input("cevap: ")
#         if soru.checkAnswer(ans):
#             self.score += 1

#     def loadQuestion(self):
#         if(self.questionIndex < len(self.questions)):
#             self.displayQuestion()
#             self.questionIndex += 1
#             self.loadQuestion()
#         else:
#             self.displayScore()
            
#     def displayScore(self):
#         print(100 / len(self.questions) * self.score)

#     def displayProgress(self):
#         print(f"{len(self.questions)} sorudan {self.questionIndex + 1}. sorudasınız.")

# s1 = Question("en iyi prog. dili?", ["python", "c#", "java", "php"], "c#")
# s2 = Question("en popüler prog. dili?", ["python", "c#", "java", "php"], "python")
# s3 = Question("en çok kazandıran prog. dili?", ["python", "c#", "java", "php"], "java")

# sorular = [s1, s2, s3]

# quiz1 = Quiz(sorular)

# quiz1.loadQuestion()

# # -----------------------------------------------------------------------------------------------------

# # çalışma sorusu 5 => detaylandırılabilir tamamlanmadı.

# from random import shuffle, sample

# class Kart:
#     def __init__(self, tip, deger):
#         self.tip = tip
#         self.deger = deger
   
#     def __repr__(self): # nesne print edilirken ram'deki adresi değil burdaki return değeri yazdırılır 
#         return f"{self.tip} {self.deger}"

# """
#     def kartiGetir(self):
#         return f"{self.tip} {self.deger}"
# """

# class Deste:
#     kartTipleri = ["karo", "sinek", "kupa", "maça"]
#     kartDegerleri = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
#     def __init__(self):
#         self.kartlar = [Kart(a, b) for a in Deste.kartTipleri for b in Deste.kartDegerleri]
#         self.kartCount = len(self.kartlar)
#         self.kartlariKaristir()

#     def kartlariKaristir(self):
#         return shuffle(self.kartlar)

#     def kartAt(self):
#         self.kartCount -= 1
#         return self.kartlar.pop()

#     def kartDagit(self, num):
#         self.kartCount -= num
#         return sample(self.kartlar, num)

#     def kartSayisi(self):
#         return self.kartCount

# deste = Deste()
# print(deste.kartSayisi())
# print([a for a in deste.kartDagit(5)])
# print(deste.kartSayisi())
# print(deste.kartAt())
# print(deste.kartSayisi())

# # -----------------------------------------------------------------------------------------------------

# inheritance: kalıtım => Kisi: ogrenci, ogretmen
# base_class parent_class => kisi; child_class => ogrenci, ogretmen

class Person: # base, parent class
    def __init__(self, name, surName):
        self.name = name
        self.surName = surName
        print("person nesnesi türetildi.")

    def intro(self):
        print(self.name, self.surName)

class Student(Person): # student class'ı persen class'ının child class'ı
    def __init__(self, name, surName, number):
        Person.__init__(self, name, surName)
        # veya super().__init__(name, surName) => self parametresine gerek olmayan hali
        self.number = number
        print("student nesnesi türetildi.")

    def intro(self):
        print(self.name, self.surName, self.number)

    def dersCalis(self):
        print(f"{self.name} ders çalışıyor.")

class Teacher(Person): # teacher class'ı persen class'ının child class'ı
    def __init__(self, name, surName, branch):
        super().__init__(name, surName)
        self.branch = branch
        print("teacher nesnesi türetildi.")

    def dersIsle(self):
        print(f"{self.name}, {self.branch} dersi anlatıyor.")

p1 = Person("harun", "ethem")  # person nesnesi türetildi. 
s1 = Student("yusuf", "calis", "183301051")  # person nesnesi türetildi.  
t1 = Teacher("hande", "betul", "edebiyat")  # person nesnesi türetildi.
print("---")
print(p1.name, p1.surName)
print(s1.name, s1.surName, s1.number)  # hepsi person nesnesidir fakat isimleri kendine has kalır
print(t1.name, t1.surName, t1.branch)
print("---")
p1.intro()
t1.intro()  # base class içerisindeki methodlara child'lar üzerinden erişilebilir
s1.intro()  # aynı method child class içerisinde de varsa içteki geçerli olur
print("---")
s1.dersCalis()
t1.dersIsle()