const express = require('express');
const app = express();

let health_code = 200;
let health_message = 'ok';

app.get('/', function (req, res) {
  res.send('Hello, World!');
});

app.get('/health', function (req, res) {
  res.status(health_code).send(health_message);
});

const server = app.listen(3000, function () {
  console.log('server is listening on 3000.');
});

process.on('SIGTERM', () => {
  console.log('ON SIGTERM');
  health_code = 404;
  health_message = 'shutting down';
});
