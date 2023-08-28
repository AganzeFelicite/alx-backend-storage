-- a procedure to compute average
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)
BEGIN
	UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id =  user_id)
	WHERE id = user_id;
END;
