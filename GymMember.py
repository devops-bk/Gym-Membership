class GymMember:

    def __init__(self, name = '', age = '', gender = '', contactno = '', emailid = '', bmi = '', duration = ''):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__contactno = contactno
        self.__emailid = emailid
        self.__bmi = bmi
        self.__duration = duration

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setContactno(self, contactno):
        self.__contactno = contactno

    def getContactno(self):
        return self.__contactno

    def setEmailid(self, emailid):
        self.__emailid = emailid

    def getEmailid(self):
        return self.__emailid

    def setBmi(self, bmi):
        self.__bmi = bmi

    def getBmi(self):
        return self.__bmi

    def setDuration(self, duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration

    def __str__(self):
        return self.getName()+" "+self.getAge()+" "+self.getGender()+" "+self.getContactno()+" "+self.getEmailid()+" "+self.getBmi()+" "+self.getDuration()