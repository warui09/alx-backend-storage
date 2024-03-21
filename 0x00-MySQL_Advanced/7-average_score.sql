-- creates a stored procedure that computes and stores
-- the average score for a student
DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score INT;
	DECLARE total_projects INT;

	SELECT SUM(score)
		INTO total_score
		FROM corrections
		WHERE corrections.user_id = user_id;

	SELECT COUNT(*)
		INTO total_projects 
		FROM corrections
		WHERE corrections.user_id = user_id;

	UPDATE users
		SET average_score = IF(total_projects = 0, 0, total_score / total_projects)
		WHERE users.id = user_id;
	
END //
DELIMITER ;
