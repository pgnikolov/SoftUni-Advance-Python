from song import Song


class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [s for s in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            for song_ in self.songs:
                if song_.name == song_name:
                    self.songs.remove(song_)
                    return f"Removed song {song_name} from album {self.name}."
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        text = f"Album {self.name}\n"
        for song_ in self.songs:
            text += f"== {song_.get_info()}\n"
        return text
