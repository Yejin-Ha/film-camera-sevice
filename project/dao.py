import cx_Oracle
from selftest_dto import User
from signup_dto import USERDTO

class Camera:
    def update_level(self, user):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("update users set test_level=:test_level where u_id=:u_id and u_pw=:u_pw",\
                    test_level=int(user.getLevel()), u_id=user.getU_id(), u_pw=user.getU_pw()) 
                conn.commit()
                return "성공"
            except Exception as e:
                print(e) 
                return '실패'
        finally:
            cur.close() 
            conn.close()


    def userinsert(self, dto):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into users values (seq_users.nextval, :u_id, :u_pw, :nick, 0)", u_id=dto.getU_id(), u_pw=dto.getU_pw(), nick=dto.getNick())
            conn.commit()
        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()
    
    
    def id_check(self, u_id):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("select * from users where u_id= :u_id", u_id = u_id)
            row = cur.fetchone()
            return row
        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()


    def nick_check(self, nick):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("select * from users where nick= :nick", nick = nick)
            row = cur.fetchone()
            return row
        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

if __name__=="__main__":
    a = Camera()
    b = User('hyj', 'asdf', 3)
    print(a.update_level(b))
