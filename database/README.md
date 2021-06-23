# 사용되는 DB의 초기 설정, 데이터 입력에 대한 폴더입니다.

## db.sql
db의 초기 설정을 넣어둔다.

# csv 파일의 데이터를 db에 넣는 방법
## CAMERA.csv
cameras table에 넣을 데이터들이 들어있다.
## camera_table.txt
csv 파일의 데이터를 cameras table로 import 하는 control 파일
```
options(load=-1, errors=-1)             # 모든 파일을 로드하고(load=-1) 발생하는 모든 에러를 실행해라(error=-1)
load data                               # 데이터를 로드해라
infile 'C:\Users\Playdata\Desktop\Mini Project\Tea-Time\database\CAMERA.csv'
                                        # 원하는 파일(CAMERA.csv)을 로드하는 명령어, local의 디렉토리를 적으면 된다.
append into table cameras               # cameras 테이블에 데이터를 추가해라
fields terminated by ','                # 각 필드는 , 기호로 구분한다.
(                                       # cameras 테이블의 컬럼 지정, csv의 데이터를 어떤 순서대로 어떤 컬럼에 넣을지 지정
    brand,
    model,
    price,
    category,
    shutter,
    exposure,
    test_level
)



options(load=-1, errors=-1)
load data
infile 'C:\Users\Playdata\Desktop\Mini Project\Tea-Time\database\FILM.csv'
append into table films
fields terminated by ','  
(
    film_brand,
    film_name,
    film_type,
    iso
)

```


## cmd 창에서 실행 방법
1. csv파일과 컨트롤 파일이 존재하는 디렉토리로 이동한다.
2. cameras table이 존재하는 id/pw를 이용하여 다음의 명령문을 실행한다.
> sqlldr 'SCOTT/TIGER' control='camera_table.txt'
> sqlldr 'SCOTT/TIGER' control='film_table.txt'
