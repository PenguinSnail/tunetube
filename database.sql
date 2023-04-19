CREATE TABLE IF NOT EXISTS "photo" (
    id    SERIAL PRIMARY KEY,
    photo BYTEA
);

ALTER TABLE IF EXISTS "user"
ADD COLUMN IF NOT EXISTS password VARCHAR(127) NOT NULL;

CREATE TABLE IF NOT EXISTS "user" (
    id       SERIAL      PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    photo_id INTEGER,
    password VARCHAR(127) NOT NULL,
    FOREIGN KEY (photo_id) REFERENCES "photo"(id)
);


CREATE TABLE IF NOT EXISTS "post" (
    id      SERIAL       PRIMARY KEY,
    title   VARCHAR(100) NOT NULL,
    song    JSONB        NOT NULL,
    user_id INTEGER      NOT NULL,

    FOREIGN KEY (user_id) REFERENCES "user"(id)
);


CREATE TABLE IF NOT EXISTS "comment" (
    id        SERIAL    PRIMARY KEY,
    post_time TIMESTAMP NOT NULL,
    comment   TEXT      NOT NULL,
    post_id   INTEGER   NOT NULL,
    user_id   INTEGER   NOT NULL,

    FOREIGN KEY (post_id) REFERENCES "post"(id),
    FOREIGN KEY (user_id) REFERENCES "user"(id)
);


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
