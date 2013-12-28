create table cd_details (
	cd_id int Primary Key not null,
	cd_title char (50),
	genre char(20),
	amount int not null,
	nocopies int not null,
	manufac_date date
	);