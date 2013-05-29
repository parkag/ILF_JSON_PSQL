CREATE TABLE "UZYTKOWNIK" (
	id serial primary key,
	nazwa_uzytkownika text
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
	nazwa text
);

CREATE TABLE "SERIE"(
	id serial primary key,
	sesja_id integer,
	data timestamp,
	wynik text
);

ALTER TABLE "EKSPERYMENTY_DOSTEP"
	ADD CONSTRAINT "EKSPERYMENTY_DOSTEP_uzytkownik_id_fk" FOREIGN KEY (id_uzytkownika)
	REFERENCES "UZYTKOWNIK"(id);

ALTER TABLE "EKSPERYMENTY_DOSTEP"
	ADD CONSTRAINT "EKSPERYMENTY_DOSTEP_sesja_id_fk" FOREIGN KEY (sesja_id)
	REFERENCES "SESJA_POMIAROWA"(id);

ALTER TABLE "SESJA_POMIAROWA"
	ADD CONSTRAINT "SESJA_POMIAROWA_eksperyment_nazwa_fk" FOREIGN KEY(nazwa_id)
	REFERENCES "EKSPERYMENT"(id);

ALTER TABLE "SERIE"
	ADD CONSTRAINT "SERIE_sesja_id_fk" FOREIGN KEY(sesja_id)
	REFERENCES "SESJA_POMIAROWA"(id); 


CREATE OR REPLACE FUNCTION put_json(IN result text, integer ses_id)
	RETURNS boolean
AS $$
	import json
	obj = json.loads(result)
	rec = plpy.execute('SELECT * FROM "SERIE" WHERE sesja_id = $1', ses_id)
	prev = json.loads(rec['wynik'])
	for x in obj.keys():
		if obj[x]["pragma"] == "append":
			prev[x]["value"].append(obj[x]["value"])
		elif obj[x]["pragma"] == "replace":
			prev[x]["value"] = (obj[x]["value"])
		elif obj[x]["pragma"] == "transient":
			pass
	new_result = json.dumps(prev)
	plpy.execute('UPDATE "SERIE" SET wynik = $1 WHERE sesja_id = $2', new_result, ses_id)
	return True
$$
LANGUAGE 'plpythonu' VOLATILE;

