use films;

/*
Например, в таблице создаются следующие столбцы:
1. уникальный идентификатор фильма,
2. название фильма
3. год выхода
4. длительность фильма в минутах
5. сюжетная линия, небольшое описание фильма
Все поля имеют ограничение NOT NULL. Первичный ключ PRIMARY KEY – поле id.
*/

DROP TABLE if exists Films;

CREATE TABLE Films (id int primary key auto_increment not null,
					name varchar(45) not null,
                    year YEAR not null,
                    duration int not null,
                    description text not null);

INSERT Films(name, year, duration, description) 
VALUES ('Harry Potter and the Philosophers Stone', 2001, 152, "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world."),
('Harry Potter and the Chamber of Secrets', 2002, 162,"An ancient prophecy seems to be coming true when a mysterious presence begins stalking the corridors of a school of magic and leaving its victims paralyzed."),
('The Green Mile', 1999, 188,'Death Row guards at a penitentiary, in the 1930s, have a moral dilemma with their job when they discover one of their prisoners, a convicted murderer, has a special gift.'),
('Forrest Gump', 1994, 142,"The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.");

RENAME TABLE Films TO Movies;

ALTER TABLE Movies ADD language VARCHAR(45); 

ALTER TABLE Movies DROP column language; 

CREATE TABLE Autor (id int primary key auto_increment not null,
                    name varchar(45) not null);

INSERT Autor(name) 
VALUES ('Ivan'),
('Yuliya');

ALTER TABLE Movies ADD id_autor int not null; 

ALTER TABLE Movies ADD FOREIGN KEY (id_autor) REFERENCES Autor (id) ON DELETE SET NULL; 

TRUNCATE TABLE movies;




