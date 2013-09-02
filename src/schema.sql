DROP TABLE IF EXISTS "UZYTKOWNIK" CASCADE;
DROP TABLE IF EXISTS "EKSPERYMENTY_DOSTEP" CASCADE;
DROP TABLE IF EXISTS "SESJA_POMIAROWA" CASCADE;
DROP TABLE IF EXISTS "EKSPERYMENT" CASCADE;
DROP TABLE IF EXISTS "SERIE" CASCADE;

CREATE TABLE "UZYTKOWNIK" (
	id SERIAL PRIMARY KEY,
	nazwa_uzytkownika TEXT
);

CREATE TABLE "EKSPERYMENTY_DOSTEP"(
	id SERIAL PRIMARY KEY,
	id_uzytkownika INTEGER,
	sesja_id INTEGER
);

CREATE TABLE "SESJA_POMIAROWA"(
	id SERIAL PRIMARY KEY,
	nazwa_id INTEGER
);

CREATE TABLE "EKSPERYMENT"(
	id SERIAL PRIMARY KEY,
	nazwa TEXT
);

CREATE TABLE "SERIE"(
	id SERIAL PRIMARY KEY,
	sesja_id INTEGER,
	data TIMESTAMP,
	wynik TEXT
);
/*
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
*/

CREATE OR REPLACE FUNCTION put_json()
	RETURNS TRIGGER AS
	$$
	import json
	from datetime import datetime

	get_curr_rec = plpy.prepare('SELECT * FROM "SERIE" WHERE sesja_id = $1', [ "int" ])	
	rec = plpy.execute(get_curr_rec, [TD['new']['sesja_id']])
	delete_old_serie = plpy.prepare('DELETE FROM "SERIE" WHERE sesja_id = $1', [ "int" ])
	plpy.execute(delete_old_serie, [TD['new']['sesja_id']] )
	obj = json.loads( TD['new']['wynik'] ) 
	
	if len(rec) == 0:
		for x in obj.keys():
			del obj[x]["pragma"]
		TD['new']['wynik'] = json.dumps(obj, separators=(',',':'))
	else:
		prev = json.loads(rec[0]['wynik'])
		for x in obj.keys():
			if x not in prev.keys() and obj[x]["pragma"] != "transient":
				prev[x] = {}
				prev[x]['value'] = obj[x]["value"]
			elif obj[x]["pragma"] == "append":
				for v in obj[x]["value"]:
					prev[x]["value"].append(v)
			elif obj[x]["pragma"] == "replace":
				prev[x]["value"] = obj[x]["value"]
			elif obj[x]["pragma"] == "transient":
				pass
			else:
				#raise exception?
				return "SKIP"
		TD['new']['wynik'] = json.dumps(prev, separators=(',',':'))
		TD['new']['data'] = datetime.now();
	return "MODIFY"
	$$
LANGUAGE 'plpythonu' VOLATILE;


CREATE TRIGGER manage_json 
	BEFORE INSERT ON "SERIE" 
	FOR EACH ROW EXECUTE PROCEDURE put_json();

