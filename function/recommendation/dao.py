import cx_Oracle
from dto import LEVELDTO
import json
import collections


class LEVELDAO:

    def levelselect(self, test_level):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("select * from cameras where test_level= :test_level order by price", test_level=test_level)
            rows = cur.fetchall()
            for i in range(len(rows)):
                
            return rows
        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()


if __name__ == "__main__":
    dao = LEVELDAO()
