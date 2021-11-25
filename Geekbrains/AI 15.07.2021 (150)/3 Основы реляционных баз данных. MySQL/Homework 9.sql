/*
 * 1.
 * В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
 * Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
 * 
 */

START TRANSACTION;

INSERT INTO sample.users
SELECT * FROM shop.users sh WHERE sh.id = 1;

DELETE FROM shop.users sh
WHERE sh.id = 1;

COMMIT;



/*
 * 2. 
 * Создайте представление, которое выводит название name товарной позиции из таблицы products 
 * и соответствующее название каталога name из таблицы catalogs.
 * 
 */
CREATE VIEW cat_products AS
SELECT 
	p.*
	,c.name AS cat_name
FROM 
	shop.products p 
	JOIN shop.catalogs c ON c.id = p.catalog_id;
	

/*
 * 3. (по желанию) 
 * Пусть имеется таблица с календарным полем created_at. 
 * В ней размещены разряженые календарные записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и 2018-08-17. 
 * Составьте запрос, который выводит полный список дат за август, выставляя в соседнем поле значение 1, 
 * если дата присутствует в исходном таблице и 0, если она отсутствует.
 * 
 */

CREATE VIEW digit AS
	(
	SELECT 0 AS digit FROM dual UNION ALL 
	SELECT 1 FROM DUAL UNION ALL 
	SELECT 2 FROM DUAL UNION ALL 
	SELECT 3 FROM DUAL UNION ALL 
	SELECT 4 FROM DUAL UNION ALL 
	SELECT 5 FROM DUAL UNION ALL 
	SELECT 6 FROM DUAL UNION ALL 
	SELECT 7 FROM DUAL UNION ALL 
	SELECT 8 FROM DUAL UNION ALL 
	SELECT 9 FROM DUAL
	);

SELECT 
	ten_pos.digit * 10 + unit_pos.digit AS day_num
	,ifnull((
		SELECT 1 
		FROM table3 t 
		WHERE 	t.created_at = DATE_ADD("2018-08-01", INTERVAL (ten_pos.digit * 10 + unit_pos.digit - 1) DAY)
	 ), 0) AS is_exist
FROM digit AS unit_pos
	JOIN digit AS ten_pos
WHERE ten_pos.digit * 10 + unit_pos.digit BETWEEN 1 AND 31
;


/*
 * 4. (по желанию) 
 * Пусть имеется любая таблица с календарным полем created_at. 
 * Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей.
 * 
 */

-- через редактируемое представление 
-- (работает, но для этого всегда нужно уникальное поле id и не уверен, что это хорошее решение)
CREATE OR REPLACE VIEW temp AS 
SELECT table4.*
FROM table4  
ORDER BY table4.created_at DESC 
LIMIT 18446744073709551615 offset 5;

DELETE 
FROM table4 
WHERE EXISTS (SELECT 1 FROM temp WHERE temp.id = table4.id);


-- удаление через сохранение во временной таблице
-- (в этом случае поле id вообще не требуется, но работает слегка не по ТЗ - удаляет все, а потом восстанавливает нужные)
START TRANSACTION;

CREATE TEMPORARY TABLE temp (id bigint, created_at DATETIME);
truncate TABLE temp;

INSERT INTO temp
SELECT table4.*
FROM table4  
ORDER BY table4.created_at DESC 
LIMIT 5;

TRUNCATE TABLE table4;

INSERT INTO table4 
SELECT * FROM temp;

DROP TEMPORARY TABLE temp;

COMMIT;


/*
 * 1. 
 * Создайте двух пользователей которые имеют доступ к базе данных shop. 
 * Первому пользователю shop_read должны быть доступны только запросы на чтение данных, 
 * второму пользователю shop — любые операции в пределах базы данных shop.
 */

DROP USER IF EXISTS shop_read;
CREATE USER shop_read;
GRANT SELECT ON shop.* TO shop_read;

DROP USER IF EXISTS shop;
CREATE USER shop;
GRANT ALL ON shop.* TO shop;


/*
 * 2. (по желанию)
 * Пусть имеется таблица accounts содержащая три столбца 
 * id, name, password, содержащие первичный ключ, имя пользователя и его пароль. 
 * Создайте представление username таблицы accounts, предоставляющий доступ к столбца id и name. 
 * Создайте пользователя user_read, который бы не имел доступа к таблице accounts, 
 * однако, мог бы извлекать записи из представления username.
 */

DROP TABLE IF EXISTS account;
CREATE TABLE account (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	pass VARCHAR(255)
);

INSERT INTO account (name, pass) VALUES
  ('name1', 'SDFf64gfh$'),
  ('name2', 'K67gh#gHUd'),
  ('name3', 'НРО56:dfhg');
 
CREATE OR REPLACE VIEW acc_view AS 
SELECT a.id, a.name
FROM account a; 

DROP USER IF EXISTS shop_read;
CREATE USER shop_read;
GRANT SELECT ON shop.acc_view TO shop_read;


/* 
 * 1. Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
 * с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
*/

DELIMITER ||
DROP FUNCTION IF EXISTS hello||
CREATE FUNCTION hello()
RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
	DECLARE now_hour int DEFAULT hour(now());
	DECLARE greet varchar(255) DEFAULT '';
	IF 		now_hour >= 6 	AND now_hour < 12 THEN SET greet = 'Доброе утро';
	ELSEIF 	now_hour >= 12 	AND now_hour < 18 THEN SET greet = 'Добрый день';
	ELSEIF 	now_hour >= 18 	AND now_hour < 24 THEN SET greet = 'Добрый вечер';
	ELSEIF 	now_hour >= 0 	AND now_hour < 6  THEN SET greet = 'Доброй ночи';
	END IF;
	RETURN greet;
END;
||
DELIMITER ;

/* 
 * for test
  SELECT hello() FROM dual
*/


/* 
 * 2. 
 * В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
 * Допустимо присутствие обоих полей или одно из них. 
 * Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 * Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
 * При попытке присвоить полям NULL-значение необходимо отменить операцию.
*/

DELIMITER ||
DROP TRIGGER IF EXISTS notnulldescription||
CREATE TRIGGER null_control_description_on_insert BEFORE INSERT ON products
FOR EACH ROW 
BEGIN
	IF NEW.name IS NULL AND NEW.description IS NOT NULL THEN SET NEW.name = NEW.description;
	END IF;
	IF NEW.name IS NOT NULL AND NEW.description IS NULL THEN SET NEW.description = NEW.name;
	END IF;
	IF NEW.name IS NULL AND NEW.description IS NULL THEN SIGNAL SQLSTATE '45000' SET message_text = 'cannot insert both nullable description';
	END IF;
END;
||
DELIMITER ;

/* 
 * for test
INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  ('exist name', null, 20, 1);
 
INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  (null, 'exist description', 20, 1);
 
INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  (null, null, 20, 1);
 
SELECT * FROM products p2 
 */



/* 
 * 3. (по желанию) 
 * Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
 * Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
 * Вызов функции FIBONACCI(10) должен возвращать число 55.
 * 0	1	2	3	4	5	6	7	8	9	10	
 * 0	1	1	2	3	5	8	13	21	34	55
*/

DELIMITER ||
DROP FUNCTION IF EXISTS FIBONACCI||
CREATE FUNCTION FIBONACCI(num int)
RETURNS int DETERMINISTIC
BEGIN
	DECLARE result_2 int DEFAULT 0;
	DECLARE result_1 int DEFAULT 1;
	DECLARE result_c int DEFAULT 1;
	DECLARE i int DEFAULT 1;
	IF num < 2 THEN 
		IF num = 0 THEN SET result_c = 0;
		END IF;
		IF num = 1 THEN SET result_c = 1;
		END IF;
	ELSE 
		WHILE i < num DO
			SET result_c = result_2 + result_1;
			SET result_2 = result_1;
			SET result_1 = result_c;
			SET i = i + 1;
		END WHILE;
	END IF; 
	RETURN result_c;
END;
||
DELIMITER ;