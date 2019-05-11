class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        songs_in_playlist = set()
        current_song = self
        while(current_song):
            if current_song.name in songs_in_playlist:
                return True
            songs_in_playlist.add(current_song.name)
            current_song = current_song.next
        return False 
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())