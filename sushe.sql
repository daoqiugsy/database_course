/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : sushe

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 22/11/2020 17:02:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
use newdb;
-- ----------------------------
-- Table structure for m_table
-- ----------------------------
DROP TABLE IF EXISTS `m_table`;
CREATE TABLE `M_table`  (
  `MID` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Mname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Msex` int(0) NULL DEFAULT NULL,
  `Mage` int(0) NULL DEFAULT NULL,
  `Mphone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`MID`)

) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for s_table
-- ----------------------------
DROP TABLE IF EXISTS `Dor_table`;
CREATE TABLE `Dor_table`  (
  `Dor` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `DID` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `L_n` int(0) NULL DEFAULT NULL,
  `C_n` int(0) NULL DEFAULT NULL,
  `K_n` int(0) NULL DEFAULT NULL,
  `ispositive` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (Dor,DID)

) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for x_table
-- ----------------------------
DROP TABLE IF EXISTS `Stutable`;
CREATE TABLE `Stutable`  (
  `SID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Sname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Ssex` int(0) NULL DEFAULT NULL,
  `isHethday` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `isHeth` varchar(2)CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Dor`  varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `DID` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `MID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`SID`) USING BTREE,
  FOREIGN KEY (Dor,DID)REFERENCES Dor_table(Dor,DID),

  FOREIGN KEY (MID)REFERENCES M_table(MID)


);

SET FOREIGN_KEY_CHECKS = 1;
