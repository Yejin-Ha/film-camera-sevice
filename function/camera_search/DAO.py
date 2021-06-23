import cx_Oracle
from DTO import CameraDTO
import json
import collections

class CameraDAO:
    def allCams(self,brand,category,test_level):
        cam_data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                aa = {'brand':brand,'category':category,'test_level':test_level}
                if list(aa.values()).count(' ') == 3:
                    cur.execute("select * from cameras")
                if list(aa.values()).count(' ') == 2:
                    if aa['brand'] != ' ':
                        cur.execute("select * from cameras where brand=:brand order by price asc", brand = brand)
                    elif aa['category'] != ' ':
                        cur.execute("select * from cameras where category=:category order by price asc", category = category)
                    else:
                        cur.execute("select * from cameras where test_level=:test_level order by price asc", test_level = test_level)
                
                if list(aa.values()).count(' ') == 1:
                    if aa['brand'] == ' ':
                        cur.execute("select * from cameras where category=:category and test_level=:test_level order by price asc", category = category,test_level = test_level)
                    if aa['category'] == ' ':
                        cur.execute("select * from cameras where brand=:brand and test_level=:test_level order by price asc", brand = brand,test_level = test_level)
                    if aa['test_level'] == ' ':
                        cur.execute("select * from cameras where brand=:brand and category=:category order by price asc", brand = brand,category = category)

                if list(aa.values()).count(' ') == 0:
                    cur.execute("select * from cameras where brand=:brand and category=:category and test_level=:test_level order by price asc",brand = brand,category = category,test_level = test_level)

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
                    d['level'] = row[6]
                    v.append(d)
                print(v)
                cam_data = json.dumps(v,ensure_ascii=False)
                       
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return cam_data 



if __name__ == "__main__":
    cam = CameraDAO()
    cam.allCams("NIKON"," "," ")
    


# cam_data = '{"brand":"' + row[0] + '", "model":"' + row[1] + '", "price":' + str(row[2]) + '", "format":' + str(row[3]) + '}'
