Install
```
brew install tmux
```

Create a new tmux session
```
tmux
```

To attach to the last used session
```
tmux a
```

To see all tmux sessions
```
tmux ls
```

By default, `ctrl b` is the prefix in tmux


## Windows (tabs)
```
<prefix> c: create a new window
<prefix> d: detach tmux
<prefix> ,: rename the window
<prefix> p: previous window
<prefix> n: next window
<prefix> 0: go to window 0
```

## Panes (splits)
```
<prefix> %: vertial split
<prefix> ": horizontal split
<prefix> x: kill current window
<prefix> <left_key>: go to left pane
<prefix> <right_right>: go to right pane
```

### Resizing panes
```
<prefix> : resize-pane <direction> <number of cells>
```

Directions:
```
-D Down
-U Up
-L Left
-R Right
```

### Others

__To scroll in the pane__

```
ctrl + b
[
use arrow keys
ctrl + c to exit

```
