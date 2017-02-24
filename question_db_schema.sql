DROP TABLE IF EXISTS stonesquestions;
CREATE TABLE stonesquestions (
number INTEGER PRIMARY KEY,
qtext VARCHAR(30),
answers VARCHAR(30));
/* Needs some way of representing the matrix with Stones members corresponding 
to the answers */
