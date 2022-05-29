-- USER TABLE
create table if not exists "user" (
	user_id VARCHAR (100) primary key,
	created TIMESTAMPTZ,
	"storage" numeric
) ;


-- EVENT TABLE
create type direction_enum as enum ('upload',
'download');

create type status_enum as enum ('success',
'fail');

create table "event" (
	user_id VARCHAR (100),
	direction direction_enum,
	"size" numeric,
	status status_enum,
	"timestamp" TIMESTAMPTZ,
	transfer_time BIGINT,
	transfer_speed numeric,
	constraint fk_user
      foreign key(user_id)
	  references "user"(user_id)
);