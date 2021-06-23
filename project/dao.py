import cx_Oracle
from selftest_dto import User
from signup_dto import USERDTO
import json
import collections

class Camera:
    def recommend(self, id, pw):
        data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select test_level from users where u_id=:id and u_pw=:pw", id=id, pw=pw)
                check = cur.fetchone()
                if check:
                    cur.execute("select * from cameras where test_level= :test_level order by price", test_level=check)
                    rows = cur.fetchall()
                    v = []
                    for row in rows:
                        d = collections.OrderedDict()
                        d['brand'] = row[0]
                        d['model'] = row[1]
                        d['price'] = row[2]
                        d['category'] = row[3]
                        d['shutter'] = row[4]
                        d['exposure'] = row[5]
                        d['test_level'] = row[6]
                        v.append(d)

                    data = json.dumps(v, ensure_ascii=False)
                    return data
                else:
                    return "false"
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return data

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
