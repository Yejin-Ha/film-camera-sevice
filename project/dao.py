import cx_Oracle
from dto import User

class Camera:
    def login(self, user):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from users where u_id=:id", id=user.getId()) 
                row = cur.fetchone()
                if row:
                    return row
                else:
                    return False
            except Exception as e:
                print(e) 
        finally:
            cur.close() 
            conn.close()


if __name__=="__main__":
    a = Camera()
    b = User('hyj', 'asdf')
    print(a.login(b))
