CREATE TABLE IF NOT EXISTS FactImmigration(
	imm_id					DOUBLE PRIMARY KEY,
	port					VARCHAR(250),
	country_origin			VARCHAR(250),
	arrival_date			INT,
	departure_date			INT,
	immigration_type		INT,
	temp_state_residence	VARCHAR(15),
	gender					VARCHAR(10),
	visa_type				VARCHAR(15),
	visa_category			VARCHAR(10)
);


CREATE TABLE IF NOT EXISTS DimTime (
	sas_date_id			DOUBLE PRIMARY KEY,
	day					INT,
	week				INT,
	month				INT,
	year				INT,
	quarter				INT,
	arrival_date_f		DATE
);

CREATE TABLE IF NOT EXISTS DimAirport (
	local_code		VARCHAR(100) PRIMARY KEY,
	airport_name	VARCHAR(250),
	airport_type 	VARCHAR(100),
	iso_country		VARCHAR(10),
	continent		VARCHAR(30),
	municipality	varchar(50)
);

CREATE TABLE IF NOT EXISTS DimCountry (
	country_code	VARCHAR(50) PRIMARY KEY,
	country_name	VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS DimState (
	state_code			VARCHAR(10) PRIMARY KEY,
	state_description	VARCHAR(100),
	country_code		VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS DimVisa (
	visa_category				VARCHAR(50) PRIMARY KEY,
	description					TEXT,
	initial_duration_of_staya	TEXT,
	annual_numeric_limit		VARCHAR(250)
)