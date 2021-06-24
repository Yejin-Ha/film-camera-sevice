create table users (
    id number(3) constraint pk_users_id primary key,
    u_id varchar2(20) not null,
    u_pw varchar2(20) not null,
    nick varchar2(20) unique,
    test_level number(1)
);

create sequence seq_users;

-- test 샘플 넣기
insert into users values (seq_users.nextval, 'hyj', 'asdf', '예진', 3);
commit;

create table cameras (
    brand varchar2(30) not null,
    model varchar2(30) primary key,
    price number(3) not null,
    category varchar2(20) not null,
    shutter number(5) not null,
    exposure number(1) not null,
    test_level number(1) not null
);

create table films (
    film_brand varchar2(20) not null,
    film_name varchar2(30) primary key,
    film_type varchar2(5) not null,
    iso number(5) not null
);
