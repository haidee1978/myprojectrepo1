create table cd_rent (
cd_ID int not null,
custo_ID int not null,
custo_name char (20),
address char(50),
contact_num int not null,
rent_date date not null,
incharge char(20),
Primary key (custo_ID),
foreign key (cd_ID)references cd_details (cd_id));