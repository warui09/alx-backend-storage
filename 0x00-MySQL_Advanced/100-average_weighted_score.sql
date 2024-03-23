-- creates a stored procedure that computes and store the
-- average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
	DECLARE sum_weights INT DEFAULT 0;
	DECLARE sum_weighted_score FLOAT DEFAULT 0;

	SELECT SUM(corrections.score * projects.weight)
		INTO sum_weighted_score
		FROM corrections
			INNER JOIN projects
			ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

	SELECT SUM(projects.weight)
		INTO sum_weights
		FROM corrections
			INNER JOIN projects
			ON corrections.project_id = projects.id
		WHERE corrections.user_id = user_id;

	UPDATE users
		SET users.average_score = sum_weighted_score / sum_weights
		WHERE users.id = user_id;


END //
DELIMITER ;
