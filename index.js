const express=require('express');
const { request } = require('http');

const {open}=require('sqlite')
const sqlite3=require("sqlite3")
const app=express()

const cors = require('cors');
app.use(cors());

const path=require('path')



const dbpath=path.join(__dirname,"database.db")
let db=null;
const initializedbandserver=async()=>{
    try{
        db=await open({
            filename:dbpath,
            driver:sqlite3.Database
        });
        app.listen(3005,()=>{
            console.log("server running sucessfully")
        })
    }catch (e){
        console.log(`db error :${e.message}`)
        process.exit(1)
    }
}

initializedbandserver()


app.get("/",(request,response)=>{
    response.send("hello world")
})


app.get("/products/",async(request,response)=>{
    const {month}=request.query
    const getproduct=`select *
    from data where strftime('%m',dateofsale)="${month}"`
    const productarray=await db.all(getproduct)
    response.send(productarray)
})

app.get("/monthproducts/",async(request,response)=>{
    const{month}=request.query
  
    const getproduct=`select 
        (select sum(price) from data where sold=true and strftime('%m',dateofsale)="${month}")as totalprice,
        (select count() from data where sold=true and strftime('%m',dateofsale)="${month}")as sold,
        (select count() from data where sold=false and strftime('%m',dateofsale)="${month}")as unsold
         from data`
    const productarray=await db.get(getproduct)
    response.send(productarray)
})

app.get("/ranking/",async(request,response)=>{
    const{month}=request.query
    const getproduct=`select 
    (select count() from data where price between 100 and 200 and strftime('%m',dateofsale)="${month}")as "100-200",
    (select count() from data where price between 200 and 300 and strftime('%m',dateofsale)="${month}")as "200-300",
    (select count() from data where price between 300 and 400 and strftime('%m',dateofsale)="${month}")as "300-400",
    (select count() from data where price between 400 and 500 and strftime('%m',dateofsale)="${month}")as "400-500",
    (select count() from data where price between 500 and 600 and strftime('%m',dateofsale)="${month}")as "500-600",
    (select count() from data where price between 600 and 700 and strftime('%m',dateofsale)="${month}")as "600-700",
    (select count() from data where price between 700 and 800 and strftime('%m',dateofsale)="${month}")as "700-800",
    (select count() from data where price between 800 and 900 and strftime('%m',dateofsale)="${month}")as "800-900",
    (select count() from data where price>900 and strftime('%m',dateofsale)="${month}")as morethan900

    from data`
    const productarray=await db.get(getproduct)
    response.send(productarray)
})

app.get("/catergory/",async(request,response)=>{
    const{month}=request.query
    console.log(month)
    const getproduct=`SELECT
    category,
    COUNT(*) AS num_of_items
FROM
    data
WHERE
strftime('%m',dateofsale)="${month}"
GROUP BY category;`
    const productarray=await db.all(getproduct)
    response.send(productarray)
})

