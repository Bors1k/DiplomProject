const mysql = require("mysql2");
const express = require("express");
const dbConfig = require("./app/config/db.config")

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

app.get("/", function (req, res, next) {
    pool.query("SELECT * FROM `GOST_TYPES`", function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data)
    });
});


// app.get("/:COLUMN/:COLUMN_VALUE", function (req, res, next) {
//     const COLUMN = req.params.COLUMN;
//     const COLUMN_VALUE = req.params.COLUMN_VALUE;
//     var queryStr = "SELECT * FROM `GOST_TYPES` WHERE `" + COLUMN + "` = ?";
//     pool.query(queryStr, COLUMN_VALUE, function (err, data) {
//         if (err) return console.log(err);
//         console.log(data);
//         res.json(data)
//     });
// });


app.get("/:GOST", function (req, res, next) {
    const GOST = req.params.GOST;
    var queryStr = "SELECT * FROM `GOST_TYPES` WHERE GOST = ?";
    pool.query(queryStr, GOST, function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.get("/:GOST/:TYPE", function (req, res) {
    const GOST = req.params.GOST;
    const TYPE = req.params.TYPE;
    var queryStr = "SELECT * FROM `GOST_TYPES` WHERE GOST = ? AND TYPE = ?"
    pool.query(queryStr, [GOST, TYPE], function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.get("/:GOST/:TYPE/:COMMAND", function (req, res) {
    const GOST = req.params.GOST;
    const TYPE = req.params.TYPE;
    const COMMAND = req.params.COMMAND;
    var ID = 0;
    if (COMMAND == "SIZES") {
        var queryStr = "SELECT  `8328-75`.* " +
            "FROM `GOST_TYPES` " +
            "LEFT JOIN `8328-75` ON `8328-75`.`GOST` = `GOST_TYPES`.`ID` WHERE `GOST_TYPES`.`GOST` = ? AND `GOST_TYPES`.`TYPE` = ? "
        pool.query(queryStr, [GOST, TYPE], function (err, data) {
            if (err) return console.log(err);
            console.log(data);
            res.json(data);
        });
    }
});

app.listen(3000, function () {
    console.log("Сервер ожидает подключения...");
});