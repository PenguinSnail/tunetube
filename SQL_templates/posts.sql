create table if not exists posts(
    post_id serial not null,
    post_name varchar(225),
    song jsonb not null,
    creator int not null
);