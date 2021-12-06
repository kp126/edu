-- 1 Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем (написал ему сообщений).
SELECT 
	(SELECT firstname from users WHERE id = best_friend_id) AS best_friend,
	MAX(count_messages) as count_messages 
		FROM 
			(SELECT best_friend_id, COUNT(*) AS count_messages -- пользователи с которыми переписывается пользоватлеь №1 + подсчет кто сколько сообщений написал
				FROM 
					(SELECT to_user_id AS best_friend_id FROM messages WHERE from_user_id = 1 -- пользователи которым пишет сообщения пользователь №1
						UNION ALL SELECT from_user_id  FROM messages WHERE to_user_id = 1) as FRIENDS -- пользователи которые пишут сообщения пользователю №1
			GROUP BY best_friend_id) AS BF
GROUP BY best_friend
ORDER BY  count_messages DESC
LIMIT 1;

-- 2 Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.
SELECT count(*)
FROM 
	(SELECT * 
	FROM 
		(SELECT user_id, 
			(SELECT birthday FROM profiles as B WHERE B.user_id = L.user_id) as birthday
		FROM likes as L) AS T) as UL
WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) <= 10;

-- 3 Определить кто больше поставил лайков (всего): мужчины или женщины.
SELECT IF(
	(SELECT COUNT(id) FROM likes WHERE user_id IN 
		(SELECT user_id FROM profiles WHERE gender = "m")) 
	> 
	(SELECT COUNT(id) FROM likes WHERE user_id IN 
		(SELECT user_id FROM profiles WHERE gender = "f")), 
   'male', 'female');