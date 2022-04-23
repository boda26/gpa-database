DELIMITER //
DROP PROCEDURE IF EXISTS Result;
CREATE PROCEDURE Result(IN input VARCHAR(10))
    BEGIN
        DECLARE cur_Subject VARCHAR(255);
        DECLARE cur_Number INTEGER;
        DECLARE cur_gpa REAL;
        DECLARE cur_Description VARCHAR(255);
        DECLARE cur_CreditHours INTEGER;
        DECLARE exit_flag BOOLEAN DEFAULT FALSE;
        
        DECLARE mycursor CURSOR FOR
        SELECT Course.Subject as Subject, Course.Number as Number, 
            ROUND((SUM(A_plus)*4 + SUM(A)*4 + SUM(A_minus) * 3.67 + 
            SUM(B_plus) * 3.33 + SUM(B) * 3 + SUM(B_minus) * 2.67 + 
            SUM(C_plus) * 2.33 + SUM(C) * 2 + SUM(C_minus) * 1.67 +
            SUM(D_plus) * 1.33 + SUM(D) * 1 + SUM(D_minus) * 0.67) / 
            (SUM(A_plus) + SUM(A) + SUM(A_minus) + 
            SUM(B_plus) + SUM(B) + SUM(B_minus) + 
            SUM(C_plus) + SUM(C) + SUM(C_minus) +
            SUM(D_plus) + SUM(D) + SUM(D_minus) +SUM(F)),3) AS avg_gpa, 
            left(Description.Description,40) AS Description, Description.CreditHours
        FROM Course 
            JOIN Description USING (Title)
        WHERE Title IN (SELECT A.Title FROM Attribute A WHERE HUM = input OR ACP = input OR CS = input OR NAT = input OR QR = input OR SBS = input)
        GROUP BY Course.Subject, Course.Number, Description.Title;
    
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET exit_flag=TRUE;
        
        CREATE TABLE NewTable(
            Subject 	VARCHAR(255),
            Number 		INTEGER,
            avg_gpa 	REAL,
            avg_grade	VARCHAR(10),
            Description VARCHAR(255),
            CreditHours INTEGER,
            PRIMARY KEY (Subject, Number)
        );
        
        OPEN mycursor;
            REPEAT
                FETCH mycursor INTO cur_Subject, cur_Number, cur_gpa, cur_Description, cur_CreditHours;
                IF cur_gpa >= 3.00 THEN
                    INSERT IGNORE INTO NewTable VALUES(cur_Subject, cur_Number, cur_gpa, "A", cur_Description, cur_CreditHours);
                ELSEIF cur_GPA >= 2.00 THEN
                    INSERT IGNORE INTO NewTable VALUES(cur_Subject, cur_Number, cur_gpa, "B", cur_Description, cur_CreditHours);
				ELSEIF cur_GPA >= 1.00 THEN
                    INSERT IGNORE INTO NewTable VALUES(cur_Subject, cur_Number, cur_gpa, "C", cur_Description, cur_CreditHours);
                ELSE
                	INSERT IGNORE INTO NewTable VALUES(cur_Subject, cur_Number, cur_gpa, "F", cur_Description, cur_CreditHours);
                END IF;
            UNTIL exit_flag
            END REPEAT;
        CLOSE mycursor;
    
        SELECT *
        FROM NewTable
        ORDER BY avg_gpa DESC;
end//
DELIMITER ;