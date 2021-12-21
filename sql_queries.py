drop_immigration_table = "DROP TABLE IF EXISTS FactImmigration;"
drop_time_table = "DROP TABLE IF EXISTS DimTime;"
drop_airport_table = "DROP TABLE IF EXISTS DimAirport;"
drop_country_table = "DROP TABLE IF EXISTS DimCountry;"
drop_state_table = "DROP TABLE IF EXISTS DimState;"
drop_visa_table = "DROP TABLE IF EXISTS DimVisa;"


create_immigration_table = """
    CREATE TABLE IF NOT EXISTS FactImmigration(
        imm_id					DOUBLE PRECISION PRIMARY KEY,
        port					VARCHAR(250),
        country_origin			DOUBLE PRECISION,
        immigration_type		DOUBLE PRECISION,
        temp_state_residence	VARCHAR(15),
        gender					VARCHAR(10),
        visa_type				DOUBLE PRECISION,
        visa_category			VARCHAR(10),
        arrival_date_sas			DOUBLE PRECISION,
        departure_date_sas			DOUBLE PRECISION

    );
"""

create_time_table = """
    CREATE TABLE IF NOT EXISTS DimTime (
        sas_date_id			DOUBLE PRECISION PRIMARY KEY,
        arrival_date_f		VARCHAR(30),
        day					INT,
        week				INT,
        month				INT,
        year				INT,
        weekday             INT,
        quarter				INT
    );
"""

create_airport_table = """
    CREATE TABLE IF NOT EXISTS DimAirport (
        local_code		VARCHAR(100) PRIMARY KEY,
        airport_name	VARCHAR(250),
        airport_type 	VARCHAR(100),
        iso_country		VARCHAR(10),
        continent		VARCHAR(30),
        municipality	varchar(50)
    );
"""

create_country_table = """
    CREATE TABLE IF NOT EXISTS DimCountry (
        country_code	DOUBLE PRECISION PRIMARY KEY,
        country_name	VARCHAR(150)
    );
"""

create_state_table = """
    CREATE TABLE IF NOT EXISTS DimState (
        state_code			VARCHAR(20) PRIMARY KEY,
        state_description	VARCHAR(100),
        country_code		VARCHAR(20)
    );
"""

create_visa_table = """
    CREATE TABLE IF NOT EXISTS DimVisa (
        visa_category				VARCHAR(250) PRIMARY KEY,
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

