CREATE TABLE "UZYTKOWNIK" (
	id serial primary key,
	nazwa_uzytkownika character varying
);

CREATE TABLE "EKSPERYMENTY_DOSTEP"(
	id serial primary key,
	id_uzytkownika integer,
	sesja_id integer
);

CREATE TABLE "SESJA_POMIAROWA"(
	id serial primary key,
	nazwa_id integer
);

CREATE TABLE "EKSPERYMENT"(
	id serial primary key,
	nazwa character varying
);

CREATE TABLE "SERIE"(
	id serial primary key,
	sesja_id integer,
	data timestamp,
	wynik character varying
);