--NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML
INSERT INTO VACCINO VALUES ('Newcastle', 'Gallina', 'Pulcino', NULL, NULL, NULL, 1, 0, 0.05);
INSERT INTO VACCINO VALUES ('bronchite infettiva', 'Gallina', 'Giovane', 'Newcastle', 'Pulcino', 'Gallina', 1, 1, 0.05);
INSERT INTO VACCINO VALUES ('coccidiosi', 'Gallina', 'Pulcino', NULL, NULL, NULL, 0, 0, 0.05);

INSERT INTO VACCINO VALUES ('mixomatosi', 'Coniglio', 'Svezzamento', NULL, NULL, NULL, 1, 1, 0.5);
INSERT INTO VACCINO VALUES ('malattia emorragica', 'Coniglio', 'Giovane', 'mixomatosi', 'Svezzamento', 'Coniglio', 1, 2, 0.5);

INSERT INTO VACCINO VALUES ('clostridiosi', 'Capra', 'Svezzamento', NULL, NULL, NULL, 1, 3, 2.0);
INSERT INTO VACCINO VALUES ('enterotossiemia', 'Capra', 'Giovane', 'clostridiosi', 'Svezzamento', 'Capra', 1, 6, 2.0);

INSERT INTO VACCINO VALUES ('clostridiosi', 'Pecora', 'Svezzamento', NULL, NULL, NULL, 1, 3, 2.0);
INSERT INTO VACCINO VALUES ('enterotossiemia', 'Pecora', 'Giovane', 'clostridiosi', 'Svezzamento', 'Pecora', 1, 6, 2.0);

INSERT INTO VACCINO VALUES ('mal rosso', 'Maiale', 'Accrescimento', NULL, NULL, NULL, 1, 3, 2.0);
INSERT INTO VACCINO VALUES ('parvovirosi', 'Maiale', 'Adulto', 'mal rosso', 'Accrescimento', 'Maiale', 1, 8, 2.0);

INSERT INTO VACCINO VALUES ('respiratorio', 'Bovino', 'Svezzamento', NULL, NULL, NULL, 1, 3, 2.0);
INSERT INTO VACCINO VALUES ('clostridiosi', 'Bovino', 'Giovane', 'respiratorio', 'Svezzamento', 'Bovino', 1, 12, 2.0);
INSERT INTO VACCINO VALUES ('mastite', 'Bovino', 'Adulto', 'clostridiosi', 'Giovane', 'Bovino', 0, 24, 2.0);

INSERT INTO VACCINO VALUES ('Newcastle', 'Tacchino', 'Pulcino', NULL, NULL, NULL, 1, 0, 0.05);

COMMIT;

COMMIT;