from song import Song
from album import Album


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        for album_ in self.albums:
            if album_.name == album_name:
                if not album_.published:
                    self.albums.remove(album_)
                else:
                    return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        text = f"Band {self.name}\n"
        for x in self.albums:
            text += x.details()
        return text
