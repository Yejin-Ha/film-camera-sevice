import cx_Oracle
from selftest_dto import User
from signup_dto import USERDTO
import json
import collections

class Camera:
    def allFilms(self):
        film_data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from films")
                rows = cur.fetchall()
                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['film_brand'] = row[0]
                    d['film_name'] = row[1]
                    d['film_type'] = row[2]
                    d['iso'] = row[3]
                    v.append(d)
                # print(v)
                film_data = json.dumps(v,ensure_ascii=False)
                       
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return film_data 

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
        
    def recommend(self, i_id, i_pw):
        data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select test_level from users where u_id=:u_id and u_pw=:u_pw", u_id=i_id, u_pw=i_pw)
                check = cur.fetchone()
                if check:
                    cur.execute("select * from cameras where test_level= :test_level order by price", test_level=check[0])
                    rows = cur.fetchall()
                    if rows: 
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
                        return "error_type_no_level"
                else:
                    return "error_type_no_user"
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
            cur.execute("select * from users where u_id=:id or nick=:nick", id=dto.getU_id(), nick=dto.getNick())
            if not cur.fetchone():
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
    c = USERDTO('hyj', 'q', 'e')
    print(a.recommend('a', 'asdf'))
    # a.userinsert(c)