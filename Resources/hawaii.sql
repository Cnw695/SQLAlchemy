DROP TABLE IF EXISTS station;
DROP TABLE IF EXISTS measurements;

CREATE TABLE station (
    station VARCHAR(255)   NOT NULL,
    name VARCHAR(255)   NOT NULL,
    latitude FLOAT   NOT NULL,
    longitude FLOAT  NOT NULL,
    elevation FLOAT  NOT NULL,
    CONSTRAINT "pk_station" PRIMARY KEY (
        "station"
     )
);

CREATE TABLE measurements (
    station VARCHAR(255)   NOT NULL,
    date date   NOT NULL,
    prcp FLOAT,
    tobs INT   
);

ALTER TABLE measurements ADD CONSTRAINT fk_measurements_station FOREIGN KEY(station)
REFERENCES station (station);