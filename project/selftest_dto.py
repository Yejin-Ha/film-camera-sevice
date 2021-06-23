class User:
    def __init__(self, newu_id, newu_pw, test_level=0):
        self.u_id = newu_id
        self.u_pw = newu_pw
        # self.nick = newnick
        self.level = test_level

    def getU_id(self):
        return self.u_id
    
    def setU_id(self, newu_id):
        self.u_id = newu_id

    def getU_pw(self):
        return self.u_pw
    
    def setU_pw(self, newu_pw):
        self.u_pw = newu_pw

    # def getNick(self):
    #     return self.nick
    
    # def setNick(self, newnick):
    #     self.nick = newnick
    
    def getLevel(self):
        return self.level
    
    def setLevel(self, newlevel):
        self.level = newlevel

    def __str__(self):
        return '아이디 : ' + self.u_id + '- 비밀번호 : ' + self.u_pw + '-레벨 : ' + self.level