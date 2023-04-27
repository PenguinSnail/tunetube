CREATE TABLE IF NOT EXISTS "photo" (
    id    SERIAL PRIMARY KEY,
    photo varChar(255)
);

INSERT INTO "photo"
VALUES
    (1, 'src\static\images\cheese.png'),
    (2,	'src\static\images\coffee.png'),
    (3,	'src\static\images\default.png'),
    (4,	'src\static\images\dinosaur.png'),
    (5,	'src\static\images\hand.png')
    ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS "user" (
    id       SERIAL      PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    photo_id INTEGER,
    password VARCHAR(127) NOT NULL,
    FOREIGN KEY (photo_id) REFERENCES "photo"(id)
);


INSERT INTO "user"
VALUES
    (1,'frankyToast',1),
    (2,	'bubbybumble',2),
    (3,	'korby',3),
    (4,	'joey',4),
    (5,	'Lost',5)
    ON CONFLICT DO NOTHING;


CREATE TABLE IF NOT EXISTS "post" (
    id      SERIAL       PRIMARY KEY,
    title   VARCHAR(100) NOT NULL,
    song    JSONB        NOT NULL,
    user_id INTEGER      NOT NULL,

    FOREIGN KEY (user_id) REFERENCES "user"(id)
);

INSERT INTO "post"
VALUES
    (1,'title1','[{"time": 564,"frequency": 440,"playing": true},{"time": 2401,"frequency": 440,"playing": false}]', 1),
    (2,'title2','[{"time": 564,"frequency": 440,"playing": true},{"time": 2401,"frequency": 440,"playing": false}]', 2),
    (3,'title3','[{"time": 564,"frequency": 440,"playing": true},{"time": 2401,"frequency": 440,"playing": false}]', 3),
    (4,'title4','[{"time": 564,"frequency": 440,"playing": true},{"time": 2401,"frequency": 440,"playing": false}]', 4),
    (5,'title5','[{"time": 564,"frequency": 440,"playing": true},{"time": 2401,"frequency": 440,"playing": false}]', 5)
    ON CONFLICT DO NOTHING;


CREATE TABLE IF NOT EXISTS "comment" (
    id        SERIAL    PRIMARY KEY,
    post_time TIMESTAMP NOT NULL,
    comment   TEXT      NOT NULL,
    post_id   INTEGER   NOT NULL,
    user_id   INTEGER   NOT NULL,

    FOREIGN KEY (post_id) REFERENCES "post"(id),
    FOREIGN KEY (user_id) REFERENCES "user"(id)
);

INSERT INTO "comment"
VALUES
    (1,'2013-03-21 04:05:06.789','comment1', 1,1),
	(2,'2013-04-21 05:05:06.789','comment2', 2,2),
    (3,'2013-04-21 06:05:06.789','comment3', 1,3),
    (4,'2013-04-21 07:05:06.789','comment4', 4,4),
    (5,'2013-04-21 08:05:06.789','comment5', 5,5),
	(6,'2013-04-21 03:05:06.789','comment6', 2,1),
	(7,'2013-04-21 02:05:06.789','comment7', 3,2),
    (8,'2013-04-21 01:05:06.789','comment8', 4,3),
    (9,'2013-04-21 00:05:06.789','comment9', 5,4),
    (10,'2013-04-21 09:05:06.789','comment10',3,5)
    ON CONFLICT DO NOTHING;


CREATE TABLE IF NOT EXISTS "liked_by" (
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,

    PRIMARY KEY (post_id, user_id),
    FOREIGN KEY (post_id) REFERENCES "post"(id),
    FOREIGN KEY (user_id) REFERENCES "user"(id)
);


CREATE TABLE IF NOT EXISTS "followed_by" (
    user_id     INTEGER NOT NULL,
    follower_id INTEGER NOT NULL,

    PRIMARY KEY (user_id, follower_id),
    FOREIGN KEY (user_id)     REFERENCES "user"(id),
    FOREIGN KEY (follower_id) REFERENCES "user"(id)
);
