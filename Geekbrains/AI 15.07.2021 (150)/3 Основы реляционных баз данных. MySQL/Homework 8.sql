-- 1 Пусть задан некоторый пользователь. 
-- Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем.*/
select 
	from_user_id
	, concat(u.firstname, ' ', u.lastname) as name
	, count(*) as 'messages count'
from messages m
join users u on u.id = m.from_user_id
where to_user_id = 1
group by from_user_id
order by count(*) desc
limit 1;


-- 2 общее количество лайков, которые получили пользователи младше 10 лет.
select count(*)
from likes l
join media m on l.media_id = m.id
join profiles p on p.user_id = m.user_id
where  YEAR(CURDATE()) - YEAR(birthday) < 10;


-- 3 Определить: кто больше поставил лайков (всего) - мужчины или женщины.
SELECT  gender, COUNT(*)
from likes
join profiles on likes.user_id = profiles.user_id 
group by gender;