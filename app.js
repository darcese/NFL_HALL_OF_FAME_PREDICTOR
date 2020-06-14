const http = require('http');
const fs = require('fs');
const express = require('express');
const port = process.env.PORT || 3000;

var app = express();

var server = http.Server(app);

app.use(express.static('/Users/danielarcese/Desktop/Code/WebProjectsAndTests/NFL_Hall_Of_Fame_Predictor'));




// const server = http.createServer(function(req, res){
//     res.writeHead(200, {'Content-Type': 'text/html'})
//     fs.readFile('index.html', function(error, data){
//         if(error){
//             res.writeHead(404)
//             res.write('Error: File Not Found')
//         }else{
//             res.write(data)
//         }
//         res.end()
//     })
   
// })

server.listen(port, function(error){
    if(error){
        console.log('Something went wrong', error)
    }else{
        console.log('server is listening on port' + port)
    }   
})