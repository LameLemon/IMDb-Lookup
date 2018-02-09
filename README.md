
# IMDb-Lookup
Python script to automatically open up imdb link of the movie whose filename is given as a parameter. It also creates a spreadsheet with all the movies metadata if a folder is passed in.

## Requirements
Python 2

## Getting Started
The API key for the OMDb API can be [generated here](http://www.omdbapi.com/apikey.aspx). After you have authenticated the key paste it in the `config.json` file. 

### Usage and Examples
In the Terminal or Command Prompt:
* For single files `python imdb-lookup.py [filename]`.
* For folders `python imdb-folder.py [folder-path]`.

For example:
```
LameLemon@Food-t420 ~/git/imdb $ python imdb-lookup.py "Maze.Runner.The.Scorch.Trials.2015.1080p.BluRay.H264.AAC-RARBG"
Opening new tab
Opened
LameLemon@Food-t420 ~/git/imdb $ python imdb-folder.py "/media/scruffy/Bobolink/Media/Movies/Movies/"
Creating moviefile.xls
Done
```

## Original author
**Manoj M J** - [manojmj92](https://github.com/manojmj92)

## Notes
If there are any words in the file names that are not being filtered add them to `keywords.txt`.

Usage using the file explorer for both Windows and Ubuntu has not been thoroughly tested and is buggy.
### Windows setup

Copy `imdb-lookup.py` and `imdb-folder.py` to `C:\`. Next type `shell:sento` into Run and paste `IMDB-lookup.cmd` and `IMDB-folder.cmd`.

### Ubuntu setup
Place open_in_browser.sh and send_folde.sh in ~/.gnome2/nautilus-scripts. U can see them in Scripts -> when u right click.
Place imdb-lookup and imdb-folder.py on desktop.

### Other
[More explanation](http://qr.ae/GxOcx)
[A how-to video](http://youtu.be/JANNcimQGyk)
