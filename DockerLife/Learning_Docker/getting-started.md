docker run --name repo alpinegit clone \
https://github.com/docker/getting-started.git docker cp repo:/git/getting-started/ .


cd getting-started
docker build -t docker101tutorial .

docker run -d -p 80:80 \
    --name docker-tutorial docker101tutorial


docker tag docker101tutorial triyanshu/docker101tutorial

docker push triyanshu/docker101tutorial