-- creates a trigger that resets the attribute valid_email
-- only when the email has been changed
DROP TRIGGER IF EXISTS reset_email;
DELIMITER //

CREATE TRIGGER IF NOT EXISTS reset_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = DEFAULT;
	END IF;
END;
//

DELIMITER ;
