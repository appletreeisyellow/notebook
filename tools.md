
## ack

Install
```
brew install ack
```

In your working directory, search 'Foo'
```
ack Foo
```

Search by file type. For example, html
```
ack --html Foo
```
Other supported files types are `--css`, `--go`, `--js`, `--json`, `--sql`, `--yaml`

[Here](https://kapeli.com/cheat_sheets/Ack.docset/Contents/Resources/Documents/index) are all the file types


## ncdu

`ncdu` is a disk usage analyzer. It is easy to use, and it meets my minimun need, which is to see my disk usage in a __clear__ and __visual__ way.

Install:
```
brew install ncdu
```

Run:
```
ncdu
```

#### Example

`ncdu` helped me to find out that Docker images occupy a lot of disk. If that happens to you as well, here is the command to delete docker images:


```
docker rmi $(docker images | grep <regex-pattern> | tr -s ' ' | cut -d ' ' -f 4 | tail)
```


