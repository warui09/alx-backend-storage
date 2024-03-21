-- creates a stored procedure that computes and stores
-- the average score for a student
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score FLOAT;
	DECLARE total_projects INT;

	SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;
	SELECT COUNT(*) INTO total_projects FROM corrections WHERE user_id = usr_id;

	UPDATE users SET average_score = IF(projects_count = 0, 0, total_score / total_projects)
	WHERE users.id = user_id;
	
END //
DELIMITER;
