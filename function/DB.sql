create table users (
    id number(3) constraint pk_users_id primary key,
    u_id varchar2(20) not null,
    u_pw varchar2(20) not null,
    nick varchar2(20) unique,
    test_level number(1) not null
);

create sequence seq_users;

-- test 샘플 넣기
insert into users values (seq_users.nextval, 'hyj', 'asdf', '예진', 3);
commit;

