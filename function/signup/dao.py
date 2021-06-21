import cx_Oracle
from dto import USERDTO
import json
import collections

class USERDAO:
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

if __name__=="__main__":
    dao = USERDAO()
    dto = USERDTO('hyj', 'asdf', '예')
    dao.userinsert(dto)
