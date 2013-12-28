create table returned_cd (
cd_id int not null,
cd_title text not null,
returned_date date not null,
primary key (cd_title),
foreign key (cd_id) references cd_details(cd_id));