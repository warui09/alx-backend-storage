-- creates a function that divides (and returns)
-- the first by the second number
DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
	DECLARE ans FLOAT DEFAULT 0;

	IF b != 0 THEN
		SET ans = CAST(a AS FLOAT) / b;
	END IF;

	RETURN ans;
END //
DELIMITER ;
