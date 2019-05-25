SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for query_table
-- ----------------------------
DROP TABLE IF EXISTS `articles_infos`;
CREATE TABLE `articles_infos` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `sid` int(11) NOT NULL COMMENT '来源id',
  `title` varchar(100) NOT NULL COMMENT '标题',
  `content` longtext NOT NULL COMMENT '内容',
  FOREIGN KEY (sid) REFERENCES articles_query_table(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;