CREATE TABLE IF NOT EXISTS photos(
	id SERIAL PRIMARY KEY,
	photo bytea
);


CREATE TABLE IF NOT EXISTS users(
 	id SERIAL PRIMARY KEY,
	username VARCHAR(15) NOT NULL,
	pass VARCHAR(15) NOT NULL,
	photo_id int,
	FOREIGN KEY (photo_id) REFERENCES photos(id),
	UNIQUE(username)
);


CREATE TABLE IF NOT EXISTS posts(
	id SERIAL PRIMARY KEY,
	title VARCHAR(15),
	song jsonb,
	user_id int,
	FOREIGN KEY(user_id) REFERENCES users(id)
);


CREATE TABLE IF NOT EXISTS postcomments(
	id int,
	posted_time timestamp,
	comment_string VARCHAR(255),
	post_id int,
	FOREIGN KEY(post_id) REFERENCES posts(id)
);


CREATE TABLE IF NOT EXISTS likes(
	post_id int,
	user_id int,
	FOREIGN KEY(post_id) REFERENCES posts(id),
	FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS followers(
	user_id int,
	follower_id int,
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(follower_id) REFERENCES users(id)
);
