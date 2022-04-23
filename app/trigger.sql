DELIMITER //
DROP TRIGGER IF EXISTS insertTrigger;
CREATE TRIGGER insertTrigger
	BEFORE Insert ON Rating 
    FOR EACH ROW
        BEGIN
            IF new.Rating >= 80 THEN
                SET new.Tag = "Excellent";
            ELSEIF new.Rating >= 60 THEN
            	SET new.Tag = "Fair";
			ELSE
				SET new.Tag = "Poor";
            END IF;
        END//   
  
DROP TRIGGER IF EXISTS updateTrigger;
CREATE TRIGGER updateTrigger
	BEFORE UPDATE ON Rating 
    FOR EACH ROW
        BEGIN
            IF new.Rating >= 80 THEN
                SET new.Tag = "Excellent";
            ELSEIF new.Rating >= 60 THEN
            	SET new.Tag = "Fair";
			ELSE
				SET new.Tag = "Poor";
            END IF;
        END//
DELIMITER ;