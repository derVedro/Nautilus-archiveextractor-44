from gi.repository import Nautilus, GObject
import os, shlex

extention_2_command = {
    ".tar.bz2": "tar xvjf",
    ".tar.gz": "tar xvzf",
    ".tar.xz": "tar xvf",
    ".tar.zst": "tar axvf",
    ".xz": "xz -kd",
    ".bz2": "bunzip2",
    ".gz": "gunzip",
    ".tar": "tar xvf",
    ".tbz2": "tar xvjf",
    ".tgz": "tar xvzf",
    ".lzma": "xz -kd",
    ".rar": "unrar vbx",
    ".zip": "unzip",
    ".z": "uncompress",
    ".7z": "7z x",
    ".exe": "cabextract",
    ".deb": "ar x",
    ".jar": "jar xf",
}


class ArchiveExtacterMenuProvider(GObject.GObject, Nautilus.MenuProvider):

    def get_file_items(self, *args):
        files = args[-1]
        for file in files:
            command = self.suitable_command(file.get_name())
            if command:
                menu_entry = Nautilus.MenuItem(
                    name="ArchiveExtracterMenuProvider::extract", label="Extract"
                )
                menu_entry.connect("activate", self.extract, command, file)
                return [menu_entry]

    def suitable_command(self, file):
        for extendtion, command in extention_2_command.items():
            if file.lower().endswith(extendtion):
                return command
        return None

    def extract(self, shit, command, file):
        os.system(
            f"nohup {command} {shlex.quote(file.get_name())}; " # >/dev/null 2>&1; "
            "RESULT=$?; "
            "ICON=$([ $RESULT -gt 0 ] && echo 'dialog-error' || echo 'dialog-information'); "
            "MESSAGE=$([ $RESULT -gt 0 ] && echo 'ERROR' || echo 'EXTRACTED'); "
            f"notify-send -i $ICON $MESSAGE -a extractor '{file.get_name()}'"
        )
