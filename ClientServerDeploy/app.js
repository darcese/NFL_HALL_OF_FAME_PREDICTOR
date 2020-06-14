const express = require('express');
const app = express();
const path = require('path');
const port = process.env.PORT || 3000;
const redirectToHTTPS = require('express-http-to-https').redirectToHTTPS;


//Dont need /insecure. delete that part later
app.use(redirectToHTTPS([/localhost:(\d{4})/], [/\/insecure/], 301));

app.use(express.static(path.join(__dirname, 'public')));
app.get('/', (req, res) => res.sendFile('index.html'));

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`));