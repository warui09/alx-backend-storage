-- creates a stored procedure that computes and stores
-- the average score for a student
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
	UPDATE userS SET average_score = avg_score WHERE id = user_id;
END //
DELIMITER;
