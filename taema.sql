-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 15, 2025 at 08:10 PM
-- Server version: 11.6.2-MariaDB
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `taema`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add activity', 7, 'add_activity'),
(26, 'Can change activity', 7, 'change_activity'),
(27, 'Can delete activity', 7, 'delete_activity'),
(28, 'Can view activity', 7, 'view_activity'),
(29, 'Can add address model', 8, 'add_addressmodel'),
(30, 'Can change address model', 8, 'change_addressmodel'),
(31, 'Can delete address model', 8, 'delete_addressmodel'),
(32, 'Can view address model', 8, 'view_addressmodel'),
(33, 'Can add benefit', 9, 'add_benefit'),
(34, 'Can change benefit', 9, 'change_benefit'),
(35, 'Can delete benefit', 9, 'delete_benefit'),
(36, 'Can view benefit', 9, 'view_benefit'),
(37, 'Can add board member', 10, 'add_boardmember'),
(38, 'Can change board member', 10, 'change_boardmember'),
(39, 'Can delete board member', 10, 'delete_boardmember'),
(40, 'Can view board member', 10, 'view_boardmember'),
(41, 'Can add category membership', 11, 'add_categorymembership'),
(42, 'Can change category membership', 11, 'change_categorymembership'),
(43, 'Can delete category membership', 11, 'delete_categorymembership'),
(44, 'Can view category membership', 11, 'view_categorymembership'),
(45, 'Can add category model', 12, 'add_categorymodel'),
(46, 'Can change category model', 12, 'change_categorymodel'),
(47, 'Can delete category model', 12, 'delete_categorymodel'),
(48, 'Can view category model', 12, 'view_categorymodel'),
(49, 'Can add comment', 13, 'add_comment'),
(50, 'Can change comment', 13, 'change_comment'),
(51, 'Can delete comment', 13, 'delete_comment'),
(52, 'Can view comment', 13, 'view_comment'),
(53, 'Can add contact', 14, 'add_contact'),
(54, 'Can change contact', 14, 'change_contact'),
(55, 'Can delete contact', 14, 'delete_contact'),
(56, 'Can view contact', 14, 'view_contact'),
(57, 'Can add downloads', 15, 'add_downloads'),
(58, 'Can change downloads', 15, 'change_downloads'),
(59, 'Can delete downloads', 15, 'delete_downloads'),
(60, 'Can view downloads', 15, 'view_downloads'),
(61, 'Can add gallery', 16, 'add_gallery'),
(62, 'Can change gallery', 16, 'change_gallery'),
(63, 'Can delete gallery', 16, 'delete_gallery'),
(64, 'Can view gallery', 16, 'view_gallery'),
(65, 'Can add membership', 17, 'add_membership'),
(66, 'Can change membership', 17, 'change_membership'),
(67, 'Can delete membership', 17, 'delete_membership'),
(68, 'Can view membership', 17, 'view_membership'),
(69, 'Can add mission', 18, 'add_mission'),
(70, 'Can change mission', 18, 'change_mission'),
(71, 'Can delete mission', 18, 'delete_mission'),
(72, 'Can view mission', 18, 'view_mission'),
(73, 'Can add news', 19, 'add_news'),
(74, 'Can change news', 19, 'change_news'),
(75, 'Can delete news', 19, 'delete_news'),
(76, 'Can view news', 19, 'view_news'),
(77, 'Can add objective', 20, 'add_objective'),
(78, 'Can change objective', 20, 'change_objective'),
(79, 'Can delete objective', 20, 'delete_objective'),
(80, 'Can view objective', 20, 'view_objective'),
(81, 'Can add partner', 21, 'add_partner'),
(82, 'Can change partner', 21, 'change_partner'),
(83, 'Can delete partner', 21, 'delete_partner'),
(84, 'Can view partner', 21, 'view_partner'),
(85, 'Can add slider', 22, 'add_slider'),
(86, 'Can change slider', 22, 'change_slider'),
(87, 'Can delete slider', 22, 'delete_slider'),
(88, 'Can view slider', 22, 'view_slider'),
(89, 'Can add specialization', 23, 'add_specialization'),
(90, 'Can change specialization', 23, 'change_specialization'),
(91, 'Can delete specialization', 23, 'delete_specialization'),
(92, 'Can view specialization', 23, 'view_specialization'),
(93, 'Can add team member', 24, 'add_teammember'),
(94, 'Can change team member', 24, 'change_teammember'),
(95, 'Can delete team member', 24, 'delete_teammember'),
(96, 'Can view team member', 24, 'view_teammember'),
(97, 'Can add vision', 25, 'add_vision'),
(98, 'Can change vision', 25, 'change_vision'),
(99, 'Can delete vision', 25, 'delete_vision'),
(100, 'Can view vision', 25, 'view_vision'),
(101, 'Can add visitor', 26, 'add_visitor'),
(102, 'Can change visitor', 26, 'change_visitor'),
(103, 'Can delete visitor', 26, 'delete_visitor'),
(104, 'Can view visitor', 26, 'view_visitor'),
(105, 'Can add welcome note', 27, 'add_welcomenote'),
(106, 'Can change welcome note', 27, 'change_welcomenote'),
(107, 'Can delete welcome note', 27, 'delete_welcomenote'),
(108, 'Can view welcome note', 27, 'view_welcomenote'),
(109, 'Can add who are we', 28, 'add_whoarewe'),
(110, 'Can change who are we', 28, 'change_whoarewe'),
(111, 'Can delete who are we', 28, 'delete_whoarewe'),
(112, 'Can view who are we', 28, 'view_whoarewe'),
(113, 'Can add working group', 29, 'add_workinggroup'),
(114, 'Can change working group', 29, 'change_workinggroup'),
(115, 'Can delete working group', 29, 'delete_workinggroup'),
(116, 'Can view working group', 29, 'view_workinggroup'),
(117, 'Can add organization', 30, 'add_organization'),
(118, 'Can change organization', 30, 'change_organization'),
(119, 'Can delete organization', 30, 'delete_organization'),
(120, 'Can view organization', 30, 'view_organization'),
(121, 'Can add individual', 31, 'add_individual'),
(122, 'Can change individual', 31, 'change_individual'),
(123, 'Can delete individual', 31, 'delete_individual'),
(124, 'Can view individual', 31, 'view_individual');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$fcLCzdfThx7yG0fVm6d0uQ$WJOP0l0W8JZ1hbhe6JCCSNr7n89vtS84Y3z0fk1fx/k=', NULL, 1, 'admin', '', '', '', 1, 1, '2025-10-15 20:09:45.140875');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'mainapp', 'activity'),
(8, 'mainapp', 'addressmodel'),
(9, 'mainapp', 'benefit'),
(10, 'mainapp', 'boardmember'),
(11, 'mainapp', 'categorymembership'),
(12, 'mainapp', 'categorymodel'),
(13, 'mainapp', 'comment'),
(14, 'mainapp', 'contact'),
(15, 'mainapp', 'downloads'),
(16, 'mainapp', 'gallery'),
(31, 'mainapp', 'individual'),
(17, 'mainapp', 'membership'),
(18, 'mainapp', 'mission'),
(19, 'mainapp', 'news'),
(20, 'mainapp', 'objective'),
(30, 'mainapp', 'organization'),
(21, 'mainapp', 'partner'),
(22, 'mainapp', 'slider'),
(23, 'mainapp', 'specialization'),
(24, 'mainapp', 'teammember'),
(25, 'mainapp', 'vision'),
(26, 'mainapp', 'visitor'),
(27, 'mainapp', 'welcomenote'),
(28, 'mainapp', 'whoarewe'),
(29, 'mainapp', 'workinggroup'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-10-15 20:09:01.824489'),
(2, 'auth', '0001_initial', '2025-10-15 20:09:07.808992'),
(3, 'admin', '0001_initial', '2025-10-15 20:09:09.152039'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-10-15 20:09:09.183554'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-15 20:09:09.246707'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-10-15 20:09:09.984144'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-10-15 20:09:10.406635'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-10-15 20:09:10.768018'),
(9, 'auth', '0004_alter_user_username_opts', '2025-10-15 20:09:10.808081'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-10-15 20:09:11.276214'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-10-15 20:09:11.289049'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-10-15 20:09:11.324745'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-10-15 20:09:11.752054'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-10-15 20:09:12.068653'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-10-15 20:09:12.435225'),
(16, 'auth', '0011_update_proxy_permissions', '2025-10-15 20:09:12.454370'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-10-15 20:09:12.920855'),
(18, 'mainapp', '0001_initial', '2025-10-15 20:09:21.370864'),
(19, 'sessions', '0001_initial', '2025-10-15 20:09:21.840435');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_activity`
--

DROP TABLE IF EXISTS `mainapp_activity`;
CREATE TABLE IF NOT EXISTS `mainapp_activity` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `sub_title` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_addressmodel`
--

DROP TABLE IF EXISTS `mainapp_addressmodel`;
CREATE TABLE IF NOT EXISTS `mainapp_addressmodel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `address` longtext NOT NULL,
  `phone_number` varchar(13) NOT NULL,
  `email` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_benefit`
--

DROP TABLE IF EXISTS `mainapp_benefit`;
CREATE TABLE IF NOT EXISTS `mainapp_benefit` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) DEFAULT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_boardmember`
--

DROP TABLE IF EXISTS `mainapp_boardmember`;
CREATE TABLE IF NOT EXISTS `mainapp_boardmember` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `proffesion` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_categorymembership`
--

DROP TABLE IF EXISTS `mainapp_categorymembership`;
CREATE TABLE IF NOT EXISTS `mainapp_categorymembership` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_categorymodel`
--

DROP TABLE IF EXISTS `mainapp_categorymodel`;
CREATE TABLE IF NOT EXISTS `mainapp_categorymodel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_comment`
--

DROP TABLE IF EXISTS `mainapp_comment`;
CREATE TABLE IF NOT EXISTS `mainapp_comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `status` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_contact`
--

DROP TABLE IF EXISTS `mainapp_contact`;
CREATE TABLE IF NOT EXISTS `mainapp_contact` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_downloads`
--

DROP TABLE IF EXISTS `mainapp_downloads`;
CREATE TABLE IF NOT EXISTS `mainapp_downloads` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(200) NOT NULL,
  `file_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_gallery`
--

DROP TABLE IF EXISTS `mainapp_gallery`;
CREATE TABLE IF NOT EXISTS `mainapp_gallery` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_individual`
--

DROP TABLE IF EXISTS `mainapp_individual`;
CREATE TABLE IF NOT EXISTS `mainapp_individual` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile_number` varchar(13) NOT NULL,
  `id_number` varchar(20) NOT NULL,
  `name_of_the_organization` varchar(200) NOT NULL,
  `number_of_year_of_experience_in_emobility_sector` int(11) NOT NULL,
  `registration_fee` varchar(20) NOT NULL,
  `annual_membership_subscription` varchar(20) NOT NULL,
  `describe_your_contribution` longtext NOT NULL,
  `what_are_the_individual_expectations` longtext NOT NULL,
  `i_agree` varchar(20) NOT NULL,
  `introduce` varchar(20) NOT NULL,
  `area_of_specialization_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mainapp_individual_area_of_specializati_4ea0eb72_fk_mainapp_s` (`area_of_specialization_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_membership`
--

DROP TABLE IF EXISTS `mainapp_membership`;
CREATE TABLE IF NOT EXISTS `mainapp_membership` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `benefit` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_mission`
--

DROP TABLE IF EXISTS `mainapp_mission`;
CREATE TABLE IF NOT EXISTS `mainapp_mission` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) DEFAULT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_news`
--

DROP TABLE IF EXISTS `mainapp_news`;
CREATE TABLE IF NOT EXISTS `mainapp_news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_objective`
--

DROP TABLE IF EXISTS `mainapp_objective`;
CREATE TABLE IF NOT EXISTS `mainapp_objective` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) DEFAULT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_organization`
--

DROP TABLE IF EXISTS `mainapp_organization`;
CREATE TABLE IF NOT EXISTS `mainapp_organization` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `organization_name` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile_number` varchar(13) NOT NULL,
  `address` varchar(200) NOT NULL,
  `number_of_existing_employees` int(11) NOT NULL,
  `name_of_the_organization_representative` varchar(200) NOT NULL,
  `email_the_representative` varchar(200) NOT NULL,
  `mobile_number_of_representative` varchar(13) NOT NULL,
  `describe_the_motivation_to_join_the_association` longtext NOT NULL,
  `organization_expectations` longtext NOT NULL,
  `upload_Company_Profile` varchar(100) NOT NULL,
  `terms_and_constitution_of_the_organization` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_organization_category`
--

DROP TABLE IF EXISTS `mainapp_organization_category`;
CREATE TABLE IF NOT EXISTS `mainapp_organization_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `organization_id` bigint(20) NOT NULL,
  `categorymodel_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mainapp_organization_cat_organization_id_category_48b2a8f3_uniq` (`organization_id`,`categorymodel_id`),
  KEY `mainapp_organization_categorymodel_id_f0b70513_fk_mainapp_c` (`categorymodel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_organization_membership_category`
--

DROP TABLE IF EXISTS `mainapp_organization_membership_category`;
CREATE TABLE IF NOT EXISTS `mainapp_organization_membership_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `organization_id` bigint(20) NOT NULL,
  `categorymembership_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mainapp_organization_mem_organization_id_category_ad2d3225_uniq` (`organization_id`,`categorymembership_id`),
  KEY `mainapp_organization_categorymembership_i_096e2a42_fk_mainapp_c` (`categorymembership_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_partner`
--

DROP TABLE IF EXISTS `mainapp_partner`;
CREATE TABLE IF NOT EXISTS `mainapp_partner` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_slider`
--

DROP TABLE IF EXISTS `mainapp_slider`;
CREATE TABLE IF NOT EXISTS `mainapp_slider` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` longtext NOT NULL,
  `image` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_specialization`
--

DROP TABLE IF EXISTS `mainapp_specialization`;
CREATE TABLE IF NOT EXISTS `mainapp_specialization` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `area_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_teammember`
--

DROP TABLE IF EXISTS `mainapp_teammember`;
CREATE TABLE IF NOT EXISTS `mainapp_teammember` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `position` varchar(150) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_vision`
--

DROP TABLE IF EXISTS `mainapp_vision`;
CREATE TABLE IF NOT EXISTS `mainapp_vision` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) DEFAULT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_visitor`
--

DROP TABLE IF EXISTS `mainapp_visitor`;
CREATE TABLE IF NOT EXISTS `mainapp_visitor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ip_address` char(39) NOT NULL,
  `visit_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `mainapp_visitor`
--

INSERT INTO `mainapp_visitor` (`id`, `ip_address`, `visit_time`) VALUES
(1, '127.0.0.1', '2025-10-15 20:10:05.879825');

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_welcomenote`
--

DROP TABLE IF EXISTS `mainapp_welcomenote`;
CREATE TABLE IF NOT EXISTS `mainapp_welcomenote` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) DEFAULT NULL,
  `title` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_whoarewe`
--

DROP TABLE IF EXISTS `mainapp_whoarewe`;
CREATE TABLE IF NOT EXISTS `mainapp_whoarewe` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) DEFAULT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mainapp_workinggroup`
--

DROP TABLE IF EXISTS `mainapp_workinggroup`;
CREATE TABLE IF NOT EXISTS `mainapp_workinggroup` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `mainapp_individual`
--
ALTER TABLE `mainapp_individual`
  ADD CONSTRAINT `mainapp_individual_area_of_specializati_4ea0eb72_fk_mainapp_s` FOREIGN KEY (`area_of_specialization_id`) REFERENCES `mainapp_specialization` (`id`);

--
-- Constraints for table `mainapp_organization_category`
--
ALTER TABLE `mainapp_organization_category`
  ADD CONSTRAINT `mainapp_organization_categorymodel_id_f0b70513_fk_mainapp_c` FOREIGN KEY (`categorymodel_id`) REFERENCES `mainapp_categorymodel` (`id`),
  ADD CONSTRAINT `mainapp_organization_organization_id_891343fc_fk_mainapp_o` FOREIGN KEY (`organization_id`) REFERENCES `mainapp_organization` (`id`);

--
-- Constraints for table `mainapp_organization_membership_category`
--
ALTER TABLE `mainapp_organization_membership_category`
  ADD CONSTRAINT `mainapp_organization_categorymembership_i_096e2a42_fk_mainapp_c` FOREIGN KEY (`categorymembership_id`) REFERENCES `mainapp_categorymembership` (`id`),
  ADD CONSTRAINT `mainapp_organization_organization_id_8802cc69_fk_mainapp_o` FOREIGN KEY (`organization_id`) REFERENCES `mainapp_organization` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
