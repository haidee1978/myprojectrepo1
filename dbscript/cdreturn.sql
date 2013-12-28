create table return_cd(
cd_ID int not null,
cd_status text not null,
returned_date date not null,
incharge text not null,
primary key (cd_ID),
foreign key (cd_ID)references cd_details(cd_ID));
