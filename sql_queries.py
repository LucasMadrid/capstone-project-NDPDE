drop_immigration_table = "DROP TABLE IF EXISTS FactImmigration;"
drop_time_table = "DROP TABLE IF EXISTS DimTime;"
drop_airport_table = "DROP TABLE IF EXISTS DimAirport;"
drop_country_table = "DROP TABLE IF EXISTS DimCountry;"
drop_state_table = "DROP TABLE IF EXISTS DimState;"
drop_visa_table = "DROP TABLE IF EXISTS DimVisa;"


create_immigration_table = """
    CREATE TABLE IF NOT EXISTS FactImmigration(
        imm_id					DOUBLE PRIMARY KEY,
        port					VARCHAR(250) NOT NULL,
        country_origin			VARCHAR(250),
        arrival_date			INT NOT NULL,
        departure_date			INT,
        immigration_type		INT,
        temp_state_residence	VARCHAR(15),
        gender					VARCHAR(10) CHECK( gender IN ('F','M','X','U') ),
        visa_type				VARCHAR(15),
        visa_category			VARCHAR(10)

    );
"""

create_time_table = """
    CREATE TABLE IF NOT EXISTS DimTime (
        sas_date_id			DOUBLE PRIMARY KEY,
        day					INT,
        week				INT,
        month				INT,
        year				INT,
        quarter				INT CHECK ( quarter >=1 and quarter <=4 ),
        arrival_date_f		DATE
    );
"""

create_airport_table = """
    CREATE TABLE IF NOT EXISTS DimAirport (
        local_code		VARCHAR(100) PRIMARY KEY,
        airport_name	VARCHAR(250) NOT NULL,
        airport_type 	VARCHAR(100) NOT NULL,
        iso_country		VARCHAR(10) NOT NULL,
        continent		VARCHAR(30),
        municipality	varchar(50)
    );
"""

create_country_table = """
    CREATE TABLE IF NOT EXISTS DimCountry (
        country_code	VARCHAR(50) PRIMARY KEY,
        country_name	VARCHAR(150) NOT NULL
    );
"""

create_state_table = """
    CREATE TABLE IF NOT EXISTS DimState (
        state_code			VARCHAR(10) PRIMARY KEY,
        state_description	VARCHAR(100) NOT NULL,
        country_code		VARCHAR(10)
    );
"""

create_visa_table = """
    CREATE TABLE IF NOT EXISTS DimVisa (
        visa_category				VARCHAR(50) PRIMARY KEY,
        description					TEXT,
        initial_duration_of_staya	TEXT,
        annual_numeric_limit		VARCHAR(250)
    );
"""


copy_data = """
    COPY {table}
    FROM '{s3_bucket}'
    IAM_ROLE '{iam_role}'
    FORMAT AS PARQUET;
"""

create_sql_queries = [create_immigration_table, create_time_table, create_airport_table, create_country_table, create_state_table, create_visa_table]
drop_sql_queries = [drop_immigration_table, drop_time_table, drop_airport_table, drop_country_table, drop_state_table, drop_visa_table]

