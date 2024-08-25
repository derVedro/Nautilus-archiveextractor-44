
# nautilus-archiveextractor

A python script to extend your Nautilus to extract all kind of archive files
strait from the context menu.

## Features

Handles `.tar.bz2`, `.tar.gz`, `.tar.xz`, `.tar.zst`, `.xz`, `.bz2`,
        `.gz`, `.tar`, `.tbz2`, `.tgz`, `.lzma`, `.rar`, `.zip`,
        `.z`, `.7z`, `.exe`, `.deb`, `.jar` archive files.
All you need is to install the suitable system tools like
        `tar`, `gzip`, `7zip`, `unrar`, `cabextract`, `xz-utils`, `bzip2`, ...  

## Installing

Download `nautilus-archiveextractor.py` and put it into your `~/.local/share/nautilus-python/extensions/`.

```bash
wget https://github.com/derVedro/Nautilus-archiveextractor-44/blob/main/nautilus-archiveextractor.py -O ~/.local/share/nautilus-python/extensions/nautilus-archiveextractor.py
```

Restart Nautilus.

```bash
nautilus -q
```