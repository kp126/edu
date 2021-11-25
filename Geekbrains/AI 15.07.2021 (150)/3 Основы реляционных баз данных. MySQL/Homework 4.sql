-- i. Заполнить все таблицы БД vk данными (по 10-20 записей в каждой таблице)
-- Использовал http://filldb.info/

-- ii. Написать скрипт, возвращающий список имен (только firstname) пользователей
-- без повторений в алфавитном порядке
SELECT DISTINCT firstname
FROM users
order by firstname;


-- iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных
-- (поле is_active = false). Предварительно добавить такое поле в таблицу profiles
-- со значением по умолчанию = true (или 1)
ALTER TABLE profiles ADD COLUMN is_active bit DEFAULT 1 COMMENT '1=True, 0=False';


 UPDATE profiles 
 SET is_active = 0
 WHERE (birthday + INTERVAL 18 YEAR) > now() ;
 
 SELECT *
FROM profiles
WHERE  is_active = 0
ORDER by birthday;
 
-- iv. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)
DELETE FROM messages 
WHERE created_at > now();

SELECT body, created_at 
FROM messages
WHERE created_at > now();

-- v. Написать название темы курсового проекта (в комментарии)
