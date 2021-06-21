create table users (
    id number(3) constraint pk_users_id primary key,
    u_id varchar2(20) constraint pk_users not null,
    u_pw varchar2(20) constraint pk_users_pw not null,
    nick varchar2(20) constraint pk_users_nick unique,
    test_level number(1)
);

drop table users;