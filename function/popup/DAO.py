import cx_Oracle
import json
import collections

class FilmDAO:
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
                print(v)
                film_data = json.dumps(v,ensure_ascii=False)
                       
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return film_data 



if __name__ == "__main__":
    cam = FilmDAO()
    cam.allFilms()
    


# cam_data = '{"brand":"' + row[0] + '", "model":"' + row[1] + '", "price":' + str(row[2]) + '", "format":' + str(row[3]) + '}'
