const mysql = require("mysql2");
const express = require("express");
// const dbConfig = require("./app/config/db.config")
const dbConfig = require("./app/config/local.db.config")

const app = express();

const pool = mysql.createPool({
    connectionLimit: 5,
    host: dbConfig.HOST,
    port: dbConfig.PORT,
    user: dbConfig.USER,
    database: dbConfig.DB,
    password: dbConfig.PASSWORD
});

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get("/GOSTS", function (req, res, next) {
    pool.query("SELECT * FROM `GOST_TYPES`", function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data)
    });
});
app.get("/TreeView", function (req, res, next) {
    pool.query("SELECT * FROM `treeviewtable`", function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data)
    });
});

app.get("/GOSTS/:GOST", function (req, res, next) {
    const GOST = req.params.GOST;
    var queryStr = "SELECT * FROM `GOST_TYPES` WHERE GOST = ?";
    pool.query(queryStr, GOST, function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.get("/HEADERS/:ID", function (req, res, next) {
    const ID = req.params.ID;
    var queryStr = "SELECT headers FROM `pageSizeHeaders` WHERE gostTypesId = ?";
    pool.query(queryStr, ID, function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.get("/GOSTS/:GOST/:TYPE", function (req, res) {
    const GOST = req.params.GOST;
    const TYPE = req.params.TYPE;
    var queryStr = "SELECT * FROM `GOST_TYPES` WHERE GOST = ? AND TYPE = ?"
    pool.query(queryStr, [GOST, TYPE], function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.get("/GOSTS/:GOST/:TYPE/SIZES", function (req, res) {
    const GOST = req.params.GOST;
    const TYPE = req.params.TYPE;
    const COMMAND = req.params.COMMAND;
    var ID = 0;
    var queryStr = "SELECT  `"+GOST+"`.* " +
        "FROM `GOST_TYPES` " +
        "LEFT JOIN `"+GOST+"` ON `"+GOST+"`.`GOST` = `GOST_TYPES`.`ID` WHERE `GOST_TYPES`.`GOST` = ? AND `GOST_TYPES`.`TYPE` = ? "
    pool.query(queryStr, [GOST, TYPE], function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.listen(3000, function () {
    console.log("Сервер ожидает подключения...");
});