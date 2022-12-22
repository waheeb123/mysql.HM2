# Create one table to keep track of the videos. This table should include a unique ID, the title of the video, the length in minutes, and the URL. Populate the table with at least three related videos from YouTube or other publicly available resources.

CREATE
TABLE
Videos(
    Id
INT
PRIMARY
KEY,
Title
VARCHAR(50)
NOT
NULL,
Length
INT
NULL,
Url
VARCHAR(100)
NOT
NULL
);
INSERT
INTO
Videos(Id, Title, Length, Url)
VALUES(1, 'Vertigo', 128, 'https://www.youtube.com/watch?v=WrOKBmsOw7I');
INSERT
INTO
Videos(Id, Title, Length, Url)
VALUES(2, 'The Innocents', 100, 'https://www.youtube.com/watch?v=lIuEEP_4d0E');
INSERT
INTO
Videos(Id, Title, Length, Url)
VALUES(3, 'Amadeus', 160, 'https://www.youtube.com/watch?v=tgZhaFFNVc4');
INSERT
INTO
Videos(Id, Title, Length, Url)
VALUES(4, 'Titanic', 194, 'https://www.youtube.com/watch?v=kRC4e3pEIpI');
INSERT
INTO
Videos(Id, Title, Length, Url)
VALUES(5, 'Good Will Hunting', 126, 'https://www.youtube.com/watch?v=hIdsjNGCGz4');
SELECT * FROM
Videos;

----------------------------------------

# Create and populate Reviewers table. Create a second table that provides at least two user reviews for each of at least two of the videos. These should be imaginary reviews that include columns for the user's name ("Asher", "Cyd", etc.), the rating (which could be NULL, or a number between 0 and 5), and a short text review ("Loved it!"). There should be a column that links back to the ID column in the table of videos.

CREATE
TABLE
Reviewers(
    User
VARCHAR(50)
NOT
NULL,
Rating
INT
NULL,
Review
VARCHAR(10),
vidId
INT
REFERENCES
Reviewers
);   INSERT
INTO
Reviewers(Id, Title, Length, Url)
VALUES(1, 'Vertigo', 128, 'https://www.youtube.com/watch?v=WrOKBmsOw7I');
INSERT
INTO
Reviewers(User, Rating, Review, vidId)
VALUES('Cyd', 5, 'Loved it!', 3);
INSERT
INTO
Reviewers(User, Rating, Review, vidId)
VALUES('Bob', 5, 'Loved it!', 5);
SELECT * FROM
Reviewers;

----------------------------------------------------------------------

# Report on Video Reviews. Write a JOIN statement that shows information from both tables.
SELECT *
FROM
Videos
v
INNER
JOIN
Reviewers
r
ON
v.Id = r.vidId;

