DROP DATABASE IF EXISTS reviews;
CREATE DATABASE reviews;
USE reviews;

-- Далее представленны таблицы и комментарии к ним

-- Таблица пользователей и данных для авторизации
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL,
    firstname VARCHAR(50) NOT NULL COMMENT 'Имя пользователя',
    lastname VARCHAR(50) NOT NULL COMMENT 'Фамилия пользователя',
    email VARCHAR(120) UNIQUE COMMENT 'Почта пользователя',
    password_hash CHAR(128) NOT NULL COMMENT 'Хеш пароля', #SHA-512 генерирует 512-bit hash value
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Тарифы
DROP TABLE IF EXISTS tariffs;
CREATE TABLE tariffs(
	id SERIAL,
	title VARCHAR(150) NOT NULL COMMENT 'Название тарифа',
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO tariffs VALUES
(1, 'without tariff',now(),now());

-- Компании
DROP TABLE IF EXISTS companies;
CREATE TABLE companies(
	id SERIAL,
	title VARCHAR(150) NOT NULL COMMENT 'Название компании',
	tariff_plan_id BIGINT UNSIGNED DEFAULT 1 COMMENT 'Тарифный план компании',
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tariff_plan_id) REFERENCES tariffs(id)
);
INSERT INTO companies VALUES
(1, 'without company', 1,now(),now());

-- Роль
DROP TABLE IF EXISTS roles;
CREATE TABLE roles(
	id SERIAL,
	title VARCHAR(150) NOT NULL COMMENT 'Аккаунтная роль. Например, администратор',
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO roles VALUES
(1, 'without role',now(),now());

-- Команды
DROP TABLE IF EXISTS teams;
CREATE TABLE teams(
	id SERIAL,
	title VARCHAR(150) NOT NULL COMMENT 'Наименование команды',
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO teams VALUES
(1, 'without team',now(),now());

-- Командная роль
DROP TABLE IF EXISTS team_roles;
CREATE TABLE team_roles(
	id SERIAL,
	title VARCHAR(150) NOT NULL COMMENT 'Название командной ролию Например, Customer Support Manager (CSM)',
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO team_roles VALUES
(1, 'without team role',now(),now());

-- Типы мультимедиа
DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL,
    title VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT NOW()
);

-- Таблица мультимедиа
DROP TABLE IF EXISTS media;
CREATE TABLE media(
	id SERIAL,
    media_type_id BIGINT UNSIGNED NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
  	body text,
    filename VARCHAR(255),
    size INT,
	metadata JSON,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	INDEX (user_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

-- Дополнительные сведения о пользователях и его роли в команде и т.д.
DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
	user_id BIGINT UNSIGNED NOT NULL UNIQUE, 
	company_id BIGINT UNSIGNED DEFAULT 1,
	role_id BIGINT UNSIGNED DEFAULT 1,
    team_id BIGINT UNSIGNED DEFAULT 1,
    team_role_id BIGINT UNSIGNED DEFAULT 1,
	gender BIT,
    birthday DATE,
	photo_id BIGINT UNSIGNED NULL,
    hometown VARCHAR(100),
    default_source_country_id BIGINT UNSIGNED NULL COMMENT 'Отзывы из какой страны загружать по умолчанию',
    default_language_id BIGINT UNSIGNED NULL COMMENT 'Отзывы на каком языке загружать по умолчанию',
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE restrict,
    FOREIGN KEY (company_id) REFERENCES companies(id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (team_id) REFERENCES teams(id),
    FOREIGN KEY (team_role_id) REFERENCES team_roles(id),
    FOREIGN KEY (photo_id) REFERENCES media(id),
    FOREIGN KEY (default_source_country_id) REFERENCES companies(id),
    FOREIGN KEY (default_language_id) REFERENCES media(id)
);

-- Запросы на вступление в аккаунт компании
DROP TABLE IF EXISTS company_requests;
CREATE TABLE company_requests (
	initiator_user_id BIGINT UNSIGNED NOT NULL,
    target_user_id BIGINT UNSIGNED NOT NULL,
    company_id BIGINT UNSIGNED NOT NULL,
    `status` ENUM('requested', 'approved', 'unapproved', 'declined'),
	requested_at DATETIME DEFAULT NOW(),
	confirmed_at DATETIME,
	INDEX (initiator_user_id),
    INDEX (target_user_id),
    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    FOREIGN KEY (target_user_id) REFERENCES users(id),
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- Запрос для предоставления аккаунтных ролей внутри компании
DROP TABLE IF EXISTS role_requests;
CREATE TABLE role_requests (
	initiator_user_id BIGINT UNSIGNED NOT NULL,
    target_user_id BIGINT UNSIGNED NOT NULL,
    role_id_now BIGINT UNSIGNED NOT NULL,
    role_id_requests BIGINT UNSIGNED NOT NULL,
    `status` ENUM('requested', 'approved', 'unapproved', 'declined'),
	requested_at DATETIME DEFAULT NOW(),
	confirmed_at DATETIME,
	INDEX (initiator_user_id),
    INDEX (target_user_id),
    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    FOREIGN KEY (target_user_id) REFERENCES users(id),
    FOREIGN KEY (role_id_now) REFERENCES profiles(role_id),
    FOREIGN KEY (role_id_requests) REFERENCES roles(id)
);

-- Запросы на вступление в команду внутри компании
DROP TABLE IF EXISTS team_requests;
CREATE TABLE team_requests (
	initiator_user_id BIGINT UNSIGNED NOT NULL,
    target_user_id BIGINT UNSIGNED NOT NULL,
    `status` ENUM('requested', 'approved', 'unapproved', 'declined'),
	requested_at DATETIME DEFAULT NOW(),
	confirmed_at DATETIME,
	INDEX (initiator_user_id),
    INDEX (target_user_id),
    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    FOREIGN KEY (target_user_id) REFERENCES users(id)
);

-- Запросы для предоставления ролей внутри команды
DROP TABLE IF EXISTS team_role;
CREATE TABLE team_role (
	initiator_user_id BIGINT UNSIGNED NOT NULL,
    target_user_id BIGINT UNSIGNED NOT NULL,
    role_id_now BIGINT UNSIGNED NOT NULL,
    role_id_requests BIGINT UNSIGNED NOT NULL,
    `status` ENUM('requested', 'approved', 'unapproved', 'declined'),
	requested_at DATETIME DEFAULT NOW(),
	confirmed_at DATETIME,
	INDEX (initiator_user_id),
    INDEX (target_user_id),
    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    FOREIGN KEY (target_user_id) REFERENCES users(id),
    FOREIGN KEY (role_id_now) REFERENCES profiles(team_role_id),
    FOREIGN KEY (role_id_requests) REFERENCES team_roles(id)
);

-- Сообщения между пользователем
DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
	id SERIAL,
	from_user_id BIGINT UNSIGNED NOT NULL,
    to_user_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX messages_from_user_id (from_user_id),
    INDEX messages_to_user_id (to_user_id),
    FOREIGN KEY (from_user_id) REFERENCES users(id),
    FOREIGN KEY (to_user_id) REFERENCES users(id)
);

-- Команды пользователя
DROP TABLE IF EXISTS user_teams;
CREATE TABLE users_teams(
	user_id BIGINT UNSIGNED NOT NULL,
	team_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (user_id, team_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

-- Таблица лайков
DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL,
    user_id BIGINT UNSIGNED NOT NULL,
    media_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE restrict,
    FOREIGN KEY (media_id) REFERENCES media(id)
);

-- Таблица источников отзывов
DROP TABLE IF EXISTS reviews_source;
CREATE TABLE reviews_source (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	company_owner VARCHAR(50) COMMENT 'Владелец источника отзывов',
    domen VARCHAR(50) COMMENT 'Домен сайта с отзывами',
    accout_name VARCHAR(50) COMMENT 'Название аккаунта(приложение/сайт/магазин)',
    account_url VARCHAR(120) COMMENT 'Ссылка на личный кабинет',
    account_login VARCHAR(120) COMMENT 'Логин от аккаунта',
    account_password_hash CHAR(128) COMMENT 'Хеш пароля от аккаунта', #SHA-512 генерирует 512-bit hash value
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX company_domen_accountname_idx(company_owner, domen, accout_name)
) COMMENT 'Обязательные данные пользователя';

-- Таблица отзывов
DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
	id SERIAL,
	from_source_id BIGINT UNSIGNED NOT NULL,
    to_company_id BIGINT UNSIGNED NOT NULL,
    review_date DATETIME NOT NULL,
    review_country VARCHAR(50),
    review_region VARCHAR(50),
    review_author VARCHAR(50) NOT NULL COMMENT 'Никнейм автора отзыва',
    review_rating INT UNSIGNED NOT NULL COMMENT 'Рейтинг в отзыве. Например, 1 звезда или 9 (из 10 баллов)',
    review_title TEXT COMMENT 'Заголовок(если имеется)',
    review_content TEXT NOT NULL COMMENT 'Содержание отзыва',
    review_content_lenght SMALLINT UNSIGNED NOT NULL COMMENT 'Длина отзыва',
    review_media_id BIGINT UNSIGNED COMMENT 'ID медиа из отзыва',
    review_status VARCHAR(30) NOT NULL COMMENT 'Статус отзыва. Например, удален, обновлен.',
    review_reputation SMALLINT UNSIGNED COMMENT 'Репутация отзыва. Если нет разделения на кол-во лайков/дислайков. Например, -15 или +34',
    review_like SMALLINT UNSIGNED,
    review_dislike SMALLINT UNSIGNED,
    review_device_model VARCHAR(30) COMMENT 'Модель устройства',
    review_device_model_disc_url VARCHAR(300) COMMENT 'Ссылка на описания устройства',
    review_app_version VARCHAR(30),
    review_app_version_code VARCHAR(30),
    review_os_version VARCHAR(30) COMMENT 'Версия ОС пользователя. Например, iOS',
    review_language VARCHAR(30),
    review_tags TEXT, #
    review_created_at DATETIME DEFAULT NOW(),
    review_updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    review_url VARCHAR(300) NOT NULL COMMENT 'Ссылка на отзыв',
    reply_author_id BIGINT UNSIGNED,
    reply_content TEXT COMMENT 'Содержание ответа',
    reply_status VARCHAR(50) COMMENT 'Статус ответа. Например, удален, устарел',
    reply_authoreply_rule VARCHAR(50) COMMENT 'Если ответ автоматический, то с помощью какого правила он был дан',
    reply_created_at DATETIME DEFAULT NOW(),
    reply_updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (from_source_id) REFERENCES reviews_source(id),
    FOREIGN KEY (to_company_id) REFERENCES companies(id),
    FOREIGN KEY (reply_author_id) REFERENCES users(id),
    FOREIGN KEY (review_media_id) REFERENCES media(id)
);

-- Типы продуктов компании
DROP TABLE IF EXISTS product_type;
CREATE TABLE product_type(
	id SERIAL,
    name VARCHAR(255),
    created_at DATETIME DEFAULT NOW()
);

-- Продукты компании
DROP TABLE IF EXISTS products;
CREATE TABLE products(
	id SERIAL,
    product_title VARCHAR(50),
    product_type_id BIGINT UNSIGNED,
    source_id BIGINT UNSIGNED,
    company_id BIGINT UNSIGNED NOT NULL,
    creator_id BIGINT UNSIGNED NOT NULL,
    updater_id BIGINT UNSIGNED,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_type_id) REFERENCES product_type(id),
    FOREIGN KEY (source_id) REFERENCES reviews_source(id),
    FOREIGN KEY (company_id) REFERENCES companies(id),
    FOREIGN KEY (creator_id) REFERENCES users(id),
    FOREIGN KEY (updater_id) REFERENCES users(id)
);

-- Категории тегов
DROP TABLE IF EXISTS tags_categories;
CREATE TABLE tags_categories(
	id SERIAL,
    name VARCHAR(255),
    created_at DATETIME DEFAULT NOW()
);

-- Теги
DROP TABLE IF EXISTS tags;
CREATE TABLE tags(
	id SERIAL,
    tag_title VARCHAR(50),
    category_tag_id BIGINT UNSIGNED NOT NULL,
    creator_company_id BIGINT UNSIGNED NOT NULL,
    creator_id BIGINT UNSIGNED NOT NULL,
    updater_id BIGINT UNSIGNED,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_tag_id) REFERENCES tags_categories(id),
    FOREIGN KEY (creator_company_id) REFERENCES companies(id),
    FOREIGN KEY (creator_id) REFERENCES users(id),
    FOREIGN KEY (updater_id) REFERENCES users(id)
);

-- Авто-теги
DROP TABLE IF EXISTS auto_tags;
CREATE TABLE auto_tags(
	id SERIAL,
    name VARCHAR(255),
    created_at DATETIME DEFAULT NOW()
);

-- Шаблоны ответов
DROP TABLE IF EXISTS templates;
CREATE TABLE templates(
	id SERIAL,
    name VARCHAR(255),
    created_at DATETIME DEFAULT NOW()
);

-- Авто-ответы
DROP TABLE IF EXISTS auto_reply;
CREATE TABLE auto_reply(
	id SERIAL,
    name VARCHAR(255),
    created_at DATETIME DEFAULT NOW()
);

-- Отчеты
/*
 * ДОБАВИТЬ
 * создателя
 * источник
 * направление отправки(почта, слак и т.д)
 * адрес(а) или user_id если внутренняя рассылка на сервисе*/
DROP TABLE IF EXISTS reports;
CREATE TABLE reports(
	id SERIAL,
    title VARCHAR(255),
    created_at DATETIME DEFAULT NOW()
);

-- Уведомления


-- Список стран


-- Список языков






































