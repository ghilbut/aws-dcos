
$ docker build -t mynode:0.1 .
$ docker run -it -p 3000:3000 --rm --name node mynode:0.1

$ docker stop node
