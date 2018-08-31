
## Removing Docker cotainers

List all exited containers
```
docker ps -aq -f status=exited
```

Remove stopped containers
```
docker ps -aq --no-trunc -f status=exited | xargs docker rm
```

## Removing Docker images

Remove dangling/untagged images
```
docker images -q --filter dangling=true | xargs docker rmi
```

Remove images by pattern match
```
docker images | grep <regex-pattern> | tr -s ' ' | cut -d ' ' -f 4 | xargs docker rmi
```
