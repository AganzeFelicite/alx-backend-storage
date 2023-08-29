-- script to devide in a function
DELIMITER $$

CREATE FUNCTION IF NOT EXISTS SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END $$

DELIMITER ;

