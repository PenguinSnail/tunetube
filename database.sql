CREATE TABLE IF NOT EXISTS PHOTOS(
	photoID SERIAL PRIMARY KEY,
	photo bytea
);


CREATE TABLE IF NOT EXISTS USERS(
	userID SERIAL PRIMARY KEY,
	username VARCHAR(15) NOT NULL,
	pass VARCHAR(15) NOT NULL,
	photoID int,
	FOREIGN KEY (photoID) REFERENCES PHOTOS,
	UNIQUE(username)
);


CREATE TABLE IF NOT EXISTS POSTS(
	postID SERIAL PRIMARY KEY,
	postName VARCHAR(15),
	song jsonb,
	userID int,
	FOREIGN KEY(userID) REFERENCES USERS
);


CREATE TABLE IF NOT EXISTS POSTCOMMENTS(
	postID int PRIMARY KEY REFERENCES POSTS,
	userID int,
	postedTime timestamp,
	commentString VARCHAR(255),
	FOREIGN KEY(userID) REFERENCES USERS
);


CREATE TABLE IF NOT EXISTS LIKES(
	postID int PRIMARY KEY REFERENCES POSTS,
	userID int,
	FOREIGN KEY(userID) REFERENCES USERS
);


CREATE TABLE IF NOT EXISTS FOLLOWERS(
	userID int PRIMARY KEY REFERENCES USERS,
	follerID int,
	FOREIGN KEY(follerID) REFERENCES USERS
);
