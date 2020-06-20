const express = require("express");
const path=require("path");
const sqlite3 = require("sqlite3").verbose();
var spawn = require ('child_process').spawn;

const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname,"/views"));
app.use(express.static(path.join(__dirname, "public")));
app.use(express.urlencoded({ extended: false }));

const db_name = path.join(__dirname, "data", "database.db");
const db = new sqlite3.Database(db_name, err => {
  if (err) {
    return console.error(err.message);
  }
  console.log("Successful connection to the database 'database.db'");
});

const sql_create = `CREATE TABLE IF NOT EXISTS QR
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        reponse TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);`;

db.run(sql_create, err => {
  if (err) {
    return console.error(err.message);
  }
  console.log("Successful creation of the 'QR' table");
});

app.listen(3000, () => { {
  console.log("Server started (http://localhost:3000/) !");
}});

app.get("/", (req, res) => { {
  const sql = "SELECT * FROM QR"
  db.all(sql, [], (err, rows) => {
    if (err) {
      return console.error(err.message);
    }
  res.render("index.ejs", { model: rows.slice(rows.length-10,rows.length)});
  });
}});

app.post("/send",(req, res)=> {
  var py = spawn('python',['backend.py']);

  var inputString = JSON.stringify(req.body.usermsg);
  var outputString='';
  console.log("Question receveid :",inputString);
  py.stdin.write(String(inputString));
  py.stdin.end();

  console.log("waiting for python process");
  py.stdout.on('data',function(data){
    console.log("Computation finished :", String(data));
    outputString += clean(String(data));
  });

  py.stdout.on('end',function(){  
    const sql = "INSERT INTO QR (question, reponse) VALUES (?,?);";
    const message=[inputString,outputString]
    db.run(sql, message, err => {
      res.redirect("/");
    });  
  });

});

//this function is here because the api print unwanted things in the python consol so I clean the message read on the consol to get only what is interresting
function clean(data){
  return data.slice(data.indexOf('Crypto-currency Master:'))
}