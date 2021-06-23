import cx_Oracle
from dto import LEVELDTO
import json
import collections

class LEVELDAO:
    def levelselect(self, test_level):
        data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from cameras where test_level= :test_level order by price", test_level=test_level)
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
                # print(data)

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return data

if __name__ == "__main__":
    dao = LEVELDAO()
    dao.levelselect(1)