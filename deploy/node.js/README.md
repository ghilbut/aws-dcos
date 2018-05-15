# A. Build docker image with source code

**mynode:0.1**이라는 이름으로 docker 이미지를 생성한다.

```bash
$ cd /path/to/aws-dcos/deploy/node.js

$ docker build -t mynode:0.1 .
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mynode              0.1                 bd3e4427c2f1        9 minutes ago       234MB
node                8.11.1-slim         6549ea3fb839        10 days ago         231MB
```

# B. Run docker instance

**node**라는 이름으로 인스턴스를 생성한다.  
서버 포트는 로컬 머신의 3000번으로 연결된다.

```bash
$ docker run -it -p 3000:3000 --rm --name node mynode:0.1
server is listening on 3000
# after execute "docker kill --signal="SIGTERM" node"
ON SIGTERM
# after execute "docker stop node"
ON SIGTERM
```

# C. Check docker status and change health check response

docker 인스턴스의 상태를 확인하고 curl을 이용하여 request가 정상적으로 서빙 되는지 테스트한다.  
health check 상태를 같이 확인하다.

```bash
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
4bfb491e494e        mynode:0.1          "node ."            28 seconds ago      Up 36 seconds       0.0.0.0:3000->3000/tcp   node

# test request
$ curl -v http://localhost:3000
* Rebuilt URL to: http://localhost:3000/
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 3000 (#0)
> GET / HTTP/1.1
> Host: localhost:3000
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< X-Powered-By: Express
< Content-Type: text/html; charset=utf-8
< Content-Length: 13
< ETag: W/"d-CgqfKmdylCVXq1NV12r0Qvj2XgE"
< Date: Tue, 15 May 2018 10:25:56 GMT
< Connection: keep-alive
< 
* Connection #0 to host localhost left intact
Hello, World!

# health check
$ curl -v http://localhost:3000/health
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 3000 (#0)
> GET /health HTTP/1.1
> Host: localhost:3000
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< X-Powered-By: Express
< Content-Type: text/html; charset=utf-8
< Content-Length: 2
< ETag: W/"2-eoX0dku9ba8cNUXvu/DyeabcC+s"
< Date: Tue, 15 May 2018 10:29:24 GMT
< Connection: keep-alive
< 
* Connection #0 to host localhost left intact
ok
```

## send SIGTERM signal

docker 인스턴스에 SIGTERM signal을 발생시킨 후 curl을 통해 health check 상태 변화를 확인한다.

```bash
# send SIGTERM signal to docker instance
$ docker kill --signal="SIGTERM" node
node

# health check
$ curl -v http://localhost:3000/health
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 3000 (#0)
> GET /health HTTP/1.1
> Host: localhost:3000
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 404 Not Found
< X-Powered-By: Express
< Content-Type: text/html; charset=utf-8
< Content-Length: 13
< ETag: W/"d-rGgWVfgAikzl3guRjfI3uyRjcS0"
< Date: Tue, 15 May 2018 10:28:13 GMT
< Connection: keep-alive
< 
* Connection #0 to host localhost left intact
shutting down
```

## stop docker

docker stop 명령을 내리면 docker 인스턴스에 SIGTERM 시그널이 발생한 후  
일정시간 뒤에 SIGKILL이 발생하면서 프로세스가 종료된다.

curl을 통해 health check 상태 변화를 확인한다.

```bash
# stop docker instance
$ docker stop node
node

# health check
$ curl -v http://localhost:3000/health
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 3000 (#0)
> GET /health HTTP/1.1
> Host: localhost:3000
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 404 Not Found
< X-Powered-By: Express
< Content-Type: text/html; charset=utf-8
< Content-Length: 13
< ETag: W/"d-rGgWVfgAikzl3guRjfI3uyRjcS0"
< Date: Tue, 15 May 2018 10:28:13 GMT
< Connection: keep-alive
< 
* Connection #0 to host localhost left intact
shutting down

# docker instance is terminated
$ curl -v http://localhost:3000/health
*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 3000 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connection failed
* connect to 127.0.0.1 port 3000 failed: Connection refused
* Failed to connect to localhost port 3000: Connection refused
* Closing connection 0
curl: (7) Failed to connect to localhost port 3000: Connection refused
```
