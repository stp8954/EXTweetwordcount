DROP TABLE IF EXISTS Tweetwordcount;
CREATE TABLE Tweetwordcount (word VARCHAR(250) PRIMARY KEY NOT NULL, count INTEGER NOT NULL);
CREATE LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_word(w VARCHAR(250), c INTEGER) 
    RETURNS void AS $$
    BEGIN
      	raise notice 'trigger called';
        IF NOT (SELECT exists (SELECT * FROM tweetwordcount WHERE word = w)) THEN
            INSERT INTO Tweetwordcount (word,count) VALUES (w, c);
        ELSE
        	UPDATE Tweetwordcount SET count = count + c WHERE word = w ;
        END IF;
    END;
$$ LANGUAGE plpgsql;