class Track():
    def __init__(self, description, length):
        self.description = description
        self.length = length
    
class CD_ROM(Track):
    def __init__(self, max_length = 74):
        self.max_length = max_length
        self.tracks = []
        self.duration = 0

    def total(self):
        return self.duration
        
    def add_track(self, track):
        self.tracks.append(track.description)
        self.duration += track.length
    
    def can_add_track(self):
        return self.max_length > self.duration


cd1 = CD_ROM()
track1 = Track("Thriller", 3.30)
track2 = Track("Bad", 2.30)
track3 = Track("Smooth Criminal", 3.15)
cd1.add_track(track1)
cd1.add_track(track2)
cd1.add_track(track3)
print(cd1.tracks, cd1.total(), cd1.can_add_track())