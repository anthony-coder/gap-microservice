# gap-microservice

To use first build the gap environment container
```
$ docker build -t gap gap-env
```
then build python environment
```
$ docker build -t mypython python-env
```
Now launch the python app in a container
```
docker run --name flask -v /var/run/docker.sock:/var/run/docker.sock -d mypython
```
You can send requests to flask with
```
$ docker exec flask curl -sg "localhost:5000/[1,2,3]"
```
where [1,2,3] can be any array.
The algorithm doubles each element and can be changed in gap.env/script.sh
