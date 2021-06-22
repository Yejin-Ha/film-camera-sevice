class User:
    def __init__(self, insert_id, insert_pw):
        self.id = insert_id
        self.pw = insert_pw

    def getId(self):
        return self.id

    def getPw(self):
        return self.pw

    def __str__(self):
        return self.id, self.pw