script = f'''
sudo apt install docker.io
sudo apt update; sudo apt install nodejs build-essential -y
mkdir hello-node
cd hello-node

cat << EOF1 > server.js
#!/usr/bin/env nodejs
var http = require('http');
var os = require('os');

var handleRequest = function(request, response) {{
    console.log('Received request for URL: ' + request.url);
    response.writeHead(200);
    response.end('{{ "host": ' + os.hostname() + ', "message": "Hello World!"}}');
}};

var www = http.createServer(handleRequest);
www.listen(8080);
EOF1
chmod +x server.js

cat << EOF2 > Dockerfile
FROM node:6.9.2
EXPOSE 8080
COPY server.js .
CMD node server.js
EOF2

sudo usermod -aG docker ubuntu
newgrp docker
cd ..
docker build -t hello-node:v1 ./hello-node/
'''