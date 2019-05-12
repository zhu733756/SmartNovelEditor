SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for query_table
-- ----------------------------
DROP TABLE IF EXISTS `articles_query_table`;
CREATE TABLE `articles_query_table` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `site` varchar(255) NOT NULL COMMENT '来源网站',
  `author` varchar(100) NOT NULL COMMENT '作者名',
  `name` varchar(100) NOT NULL COMMENT '书籍名称',
  `url` varchar(255) NOT NULL COMMENT 'url',
  `category` date DEFAULT NULL COMMENT '分类',
  `update_datetime` datetime DEFAULT NULL COMMENT '更新时间',
  `fetch_datetime` datetime NOT NULL COMMENT '抓取时间',
  `is_finished` boolean NOT NULL COMMENT '是否为完本',
  `status` int(11) NOT NULL COMMENT '抓取状态，0:未加入队列，1：正在爬取；2：已完成',
  UNIQUE KEY `url` (`url`),
  KEY `update_datetime` (`update_datetime`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;