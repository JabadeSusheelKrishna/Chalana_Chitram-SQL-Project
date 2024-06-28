DROP DATABASE IF EXISTS CHALANACHITRAM;
CREATE SCHEMA CHALANACHITRAM;
USE CHALANACHITRAM;

DROP TABLE IF EXISTS Actors;
CREATE TABLE Actors (
    F_Name varchar(30) NOT NULL,
    M_Name varchar(30) NOT NULL,
    L_Name varchar(30) NOT NULL,
    EXPERIENCE INT NOT NULL,
    Upcoming varchar(30) NOT NULL,
    Best_Role varchar(30) NOT NULL,
    Actor_ID int(9) PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS Characters;
CREATE TABLE Characters (
    Char_Id int(9) PRIMARY KEY,
    Name varchar(30),
    Movie varchar(30),
    Specials varchar(30),
    A_ID int(9),
    CONSTRAINT fk_characters_actors FOREIGN KEY (A_ID) REFERENCES Actors (Actor_ID)
    on delete set NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS Awards;
CREATE TABLE Awards (
    Name varchar(30) NOT NULL,
    Year int NOT NULL,
    Level varchar(20) NOT NULL,
    films varchar(30) NOT NULL,
    Since int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS Director;
CREATE TABLE Director (
    F_Name varchar(30) NOT NULL,
    M_Name varchar(30) NOT NULL,
    L_Name varchar(30) NOT NULL,
    DIRECTOR_ID int(9) PRIMARY KEY,
    EXPERIENCE INT NOT NULL,
    HITS_FLOPS DECIMAL(3,2) NOT NULL,
    Best_Movie varchar(30) NOT NULL,
    Upcoming varchar(30),
    Films int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS Actors_Names;
CREATE TABLE Actors_Names (
    O_FName varchar(30) NOT NULL,
    O_MName varchar(30) NOT NULL,
    O_LName varchar(30) NOT NULL,
    A_ID int(9),
    CONSTRAINT fk_actors_names_actors FOREIGN KEY (A_ID) REFERENCES Actors (Actor_ID)
        on delete set NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs (
    Music_Director varchar(30) NOT NULL,
    Singer varchar(30) NOT NULL,
    Song_ID INT(9) PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS Songs_Names;
CREATE TABLE Songs_Names (
    Name varchar(30) NOT NULL,
    Lyrics varchar(100) NOT NULL,
    Music_Directors varchar(30) NOT NULL,
    Media varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS Events;
CREATE TABLE Events (
    Name varchar(30) NOT NULL UNIQUE,
    Date Date NOT NULL,
    Budget int NOT NULL,
    Guest varchar(30) NOT NULL,
    Location varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS PRODUCER;
CREATE TABLE PRODUCER (
    fname varchar(20) NOT NULL,
    lname varchar(20) NOT NULL,
    mname varchar(20) NOT NULL,
    experience INT NOT NULL,
    prodution varchar(30) NOT NULL,
    Hits_flop_ratio decimal(3,2) NOT NULL,
    Investment INT NOT NULL,
    PRIMARY KEY (fname, lname, mname),
    UNIQUE KEY fname (fname),
    UNIQUE KEY lname (lname),
    UNIQUE KEY mname (mname)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS MOVIES;
CREATE TABLE MOVIES (
    Name varchar(20) NOT NULL,
    Budget int NOT NULL,
    Genre varchar(20),
    Censor char,
    Languages Varchar(10),
    Collection int,
    year int,
    HIT_or_FLOP INT,
    Production varchar(30),
    Duaration INT,
    A_id INT,
    S_id INT,
    PRIMARY KEY (Name),
    CONSTRAINT fk_movies_actors FOREIGN KEY (A_id) REFERENCES Actors (Actor_ID)
       on delete set NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS ASSISTANT_DIRECTORS;
CREATE TABLE ASSISTANT_DIRECTORS (
    D_id int ,
    fname varchar(30) NOT NULL,
    mname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    Department varchar(30) NOT NULL,
    work varchar(30) NOT NULL,
    PRIMARY KEY (fname),
    UNIQUE fname (fname),
    UNIQUE mname (mname),
    UNIQUE lname (lname),
    CONSTRAINT fk_assistant_directors_director FOREIGN KEY (D_id) REFERENCES Director (DIRECTOR_ID)
        on delete set NULL

) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS DISTRIBUTIONS;

CREATE TABLE DISTRIBUTIONS (
    fname varchar (30) NOT NULL,
    mname varchar (30) NOT NULL,
    lname varchar (30) NOT NULL,
    Theatre_count INT NOT NULL,
    OTT varchar (30) NOT NULL,
    Release_Date date NOT NULL,
    PRIMARY KEY (fname),
    UNIQUE(mname),
    UNIQUE (lname)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


LOCK TABLES Awards WRITE;
INSERT INTO Awards (Name, Year, Level, films, Since)
VALUES
    ('Nandi',2019,'State','RRR',1964),
    ('Nandi',2023,'State','Leo',1964),
    ('National Film Award', 2022, 'National', 'Bahubali', 1954),
    ('Filmfare Award', 2021, 'National', 'Chatrapathi', 1954),
    ('National Film Award', 2020, 'National', 'Gargi', 1954);    
UNLOCK TABLES;


LOCK TABLES Actors WRITE;
INSERT INTO Actors VALUES ('Gattamaneni','Mahesh','Babu',30,'Guntur Kaaram','Pandu gaadu',21),('Akkineni','Naga','Chaitanya',10,'Dootha','Balu',22),('Konidela','Ram','Charan',15,'Game Changer','Ram',23),('Uppalapati','Prabhas','Raju',13,'Saalar','Baahubali',24),('Nandamuri','Bala','Krishna',50,'NBK109','Legend',108);
UNLOCK TABLES;


LOCK TABLES Actors_Names WRITE;
INSERT INTO Actors_Names VALUES ('Gattamaneni','Mahesh','Babu',21),('Akkineni','Naga','Chaitanya',22),('Konidela','Ram','Charan',23),('Uppalapati','Prabhas','Raju',24),('Nandamuri','Bala','Krishna',108);
UNLOCK TABLES;

LOCK TABLES Songs WRITE;
INSERT INTO Songs VALUES ('Thaman S.S','Sid Sriram',41),('Anirudh Ravichandher','Anirudh Ravichandher',42),('A.R Rahman','Arijit Singh',43),('Keeravaani','SPB',44),('Devi Sri Prasad','Mano',45);
UNLOCK TABLES;


LOCK TABLES Songs_Names WRITE;
INSERT INTO Songs_Names VALUES ('Samajavaragamana','Nee kaallani pattuku vadalanannavi...','Thaman S.S','Youtube'),('Hukum','Hukum Tiger ka Hukum...','Anirudh Ravichandher','Instagram'),('Agar Tum saath ho','Agar Tum Saath ho...','A.R Rahman','Twitter'),('Chethilona Cheyyesi','Chethilona Cheyyesi cheppanu...','Keeravaani','T.V'),('Dhookudu','Neee Dhookudu...','Devi Sri Prasad','Youtube');
UNLOCK TABLES;


LOCK TABLES PRODUCER WRITE;
INSERT INTO PRODUCER VALUES ('Venkata', 'Ramana', 'Reddy', 20, 'Dil Raju Productions', 5.6, 200 );
INSERT INTO PRODUCER VALUES ('Prithviraj', 'Sukumaran', 'Mannar', 15, 'Prithviraj Productions', 9.0, 100 );
INSERT INTO PRODUCER VALUES ('Akkineni', 'Nagerswar', 'Rao', 30, 'Annapurna Productions', 8.0, 150 );
INSERT INTO PRODUCER VALUES ('Shobhu', 'Prasad', 'Yarlagadda', 10, 'ARKA productions', 2.0, 300 );
INSERT INTO PRODUCER VALUES ('Vijay', 'Karagadurg', 'shetty', 25, 'Hombale Films', 5.6, 500 );
UNLOCK TABLES;

LOCK TABLES Director WRITE;
INSERT INTO Director (F_Name,M_Name,L_Name,DIRECTOR_ID,EXPERIENCE,HITS_FLOPS,Best_Movie,Upcoming,Films)
VALUES
    ('Ravi', 'Kumar', 'Reddy',01, 12, 8, 'Bhagavanth Kesari',NULL,25),
    ('Suman', 'Rao', 'Sukumar',02, 13, 9, 'dhutha', NULL,30),
    ('Prakash', 'Babu', 'Chowdary',03, 13, 6, 'Akanda', NULL,20),
    ('Niharika', 'Srinivas', 'Varma',04, 17, 9, 'Manam', NULL,40),
    ('Vikram', 'Raj', 'Kumar',05, 9,7, 'Oopiri', NULL,10);
UNLOCK TABLES;


LOCK TABLES ASSISTANT_DIRECTORS WRITE;
INSERT INTO ASSISTANT_DIRECTORS VALUE (01, 'Rama', 'Rajamouli', 'Srisaila', 'Costume Director', 'Designing Costumes');
INSERT INTO ASSISTANT_DIRECTORS VALUE (01, 'Ashwin', 'Gangaraju', 'reddy', 'Screenplay Director', 'Screenplay Improvising');
INSERT INTO ASSISTANT_DIRECTORS VALUE (02, 'Buchi', 'Babu', 'Sana', 'Screenplay Director', 'Screenplay Improviser');
INSERT INTO ASSISTANT_DIRECTORS VALUE (02, 'Jakka', 'Hari', 'Prasad', 'writer director', 'Writing scripts');
INSERT INTO ASSISTANT_DIRECTORS VALUE (03, 'Dhana', 'Dan', 'Dhanraj', 'Dialogues Writer', 'writing Dialogues');
UNLOCK TABLES;


-- JAGAN's --
LOCK TABLES DISTRIBUTIONS WRITE;
INSERT INTO DISTRIBUTIONS VALUES ('Nallasingu','Jagan','Krishna',20,'Ahaa','2022-12-12'),('Gullapalli','Kiran ','Krish',242,'Prime','2023-06-08'),('Jabade','Susheel','Krishnan',131,'Netflix','2020-03-13'),('Pothuganti','Jakeer','Hussain',113,'Disney','2023-12-14'),('Beerelly','Vishwanth','vish',56,'Ahaa','2012-12-02');
UNLOCK TABLES;


-- KIRANS's --
LOCK TABLES Events WRITE;
INSERT INTO Events VALUES ('Bahubali pre-relese','2015-02-11',5000000,'balakrishna','hyderabad'),('Bahubali 2 success','2017-06-11',3000000,'chiranjeevi','vijayawada'),('AR rahman musical','2019-08-19',3000000,'arjit singh','delhi'),('sid sriram concert','2021-12-13',2004000,'thaman','hyderabad'),('RRR music release','2021-06-18',7000000,'allu arjun','Tirupati');
UNLOCK TABLES;

-- JAKEER's --




-- Doraemon --
LOCK TABLES MOVIES WRITE;
INSERT INTO MOVIES VALUES ('RRR', 500,'Drama', 'U','TELUGU', 1200, 2022, 1, 'ARKA Productions', 180, 21, 41);
INSERT INTO MOVIES VALUES ('Baahubali_1', 1000,'Action', 'U','Telugu',1200, 2015, 1, 'ARKA Productions',160,24,44);
INSERT INTO MOVIES VALUES ('Salaar', 200,'Emotion', 'A','TELUGU', 400, 2023, 1, 'Hombale Films', 200, 22, 42);
INSERT INTO MOVIES VALUES ('Salaar2', 200,'Action', 'A','KANNADA', 400, 2023, 1, 'Hombale Films', 200, 23, 42);
INSERT INTO MOVIES VALUES ('KGF', 50,'Violence', 'U','KANNADA', 600, 2020, 1, 'Hombale Films', 160, 24, 43);

UNLOCK TABLES;

LOCK TABLES Characters WRITE;
INSERT INTO Characters (Char_Id,Name,Movie,Specials,A_ID) 
VALUES 
    (12345,'Pandu','Pokiri','Undercover Spec',21),
    (12346,'raju','Manam','fighter',22),
    (12347,'Ram','RRR','Freedom Fighter',23),
    (12348,'Bahubali','Bahubali','Warrior',24),
    (12349,'Akhanda','Akhanda','God Savior',108);
UNLOCK TABLES;