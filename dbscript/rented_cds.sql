create table rented_cd (
cd_id int not null,
cd_title text not null,
primary key (cd_title),
foreign key (cd_ID) references cd_details(cd_id));