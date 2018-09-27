# Vim mini cheat sheet

#### Exist Vim

```
:q! - trash all changes
:wq - save the changes and quit
```

#### Insert Mode
```
i - insert
a - insert after the cursor
o - open a line below the cursor and place you in Insert mode
```

#### Operators and Motions
```
 operator  [number]  motion

 operator:
   d - delete/cut
   y - yank, copy
   p - paste

 [number]:
   an optional count to repeat the motion

 motion:
   w - beginning of a word forward
   b - beginning of a word backward
   e - end of a word
   0 - beginning of a line
   $ - end of a line
   c - change (= delete + insert)
```

#### Select
```
v - select characters
V - select whole lines
```

#### Delete
```
x  - delete the character at the cursor
d  - delete/cut
dw - delete/cut a word
d$ - delete/cut to the end of line
dd - delete/cut the whole line
```

#### Copy / Paste
```
y  - copy
yy - copy the whole line
p  - paste
```

#### Undo
```
u  - undo previous actions
U  - undo all the changes on a line
CRTL-R - undo the undo's
```

#### Search and Substitute
```
/  - search
n  - search the next one
N  - search in the opposition direction
%  - matching parentheses
```

#### Substitute
```
:s/old/new      - substitute the new for the first old in a line
:s/old/new/g    - substitute the new for all 'old's on a line
:%s/old/new/g   - substitute globally
:%s/old/new/gc  - to find every occurrance in the whole file,
                  with a prompt whether to substitute or not
:#,#s/old/new/g - sbustitute between line #,#
```

#### Cursor Location and File Status
```
CTRL-G - display current line number and the file status
G      - move to the end of the file
#G     - move to # line
gg     - move to the first line
```
