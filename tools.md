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

`ncdu` is a disk usage analyzer. It is easy to use, and it meets my minimun need, which is to see my disk usage in a **clear** and **visual** way.

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

## tree

`tree` is a recursive directory listing command that produces a depth indented listing of files.

Install:

```
brew install tree
```

Run:

```
tree      # to show the structure of the files in the current dir
tree -L 1 # to limit the recursion
```

## youtube-dl

Download YouTube videos into `m4a`, `mp3`, `mp4` and so on

Install:

```
brew install youtube-dl
```

Download `mp3`:

```
youtube-dl --extract-audio --audio-format mp3 <video URL>
```

## zip

Compress a folder and set password for the zip file

```
zip -er <zip_file_name.zip> <original_folder_name>
```

## ffmpeg

Convert Quicktime movies to mp4 format

Install:

```
brew install ffmpeg
```

Convert

```
ffmpeg -i my-video.mov my-video.mp4
```

## qpdf

Tools for and transforming and inspecting PDF files

Install:

```
brew install qpdf
```

Combine and merge multiple PDFs into one

```
qpdf --empty --pages *.pdf -- out.pdf
```

Select certain pages from each file and merge into one. e.g. the following command takes all the pages from `1.pdf`, all the pages from `2.pdf`, and page 1 and 2 from `3.pdf` and write the result to `out.pdf`

```
qpdf --empty --pages 1.pdf 2.pdf 3.pdf 1-2 -- out.pdf
```

QPDF supports 40-bit, 128-bit and 256-bit encryption and the key length must be specified. The examples below show 256-bit encryption.

```
qpdf --encrypt PASSWORD PASSWORD 256 -- input.pdf output.pdf
```

Use --modify=none restrictions to block users from modifying the file.

```
qpdf --encrypt PASSWORD PASSWORD 256 --modify=none -- input.pdf output.pdf
```

The format for the encryption option is:

```
--encrypt user-password owner-password key-length [ restrictions ] --
```

[qpdf doc](https://qpdf.readthedocs.io/en/stable/)

## Calibre

Install:

```
brew install --cask calibre
```

Convert ePub file to PDF:

```
ebook-convert <file>.epub <file>.pdf
```

Try to open your PDF and see if readable. If the output is not appealing, then try:

```
ebook-convert myfile.epub myfile.pdf --enable-heuristics
```

## imessage-exporter

[imessage-exporter](https://github.com/ReagentX/imessage-exporter) is a tool to export iMessage data

Install (recommended):

```
cargo install imessage-exporter
```

Other ways of [installation](https://github.com/ReagentX/imessage-exporter/blob/develop/imessage-exporter/README.md)

Example:

```
imessage-exporter -f html -o ./imessage-export-2022 -s 2022-01-01 -e 2023-01-01 -a MacOS
```
