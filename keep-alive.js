const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Bot is alive!');
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Bot is listening on port ${PORT}`);
});

// Membuat interaksi setiap 1 menit (60000 ms)
setInterval(() => {
  console.log('Keeping session alive...');
}, 60000); // 60000 ms = 1 menit
