-- creates a function that divides (and returns) the first by the second number
DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE ans DEFAULT 0;

	IF b != 0 THEN
		SET ans = a / b;
	END IF

	RETURN ans;
END //
DELIMITER ;
