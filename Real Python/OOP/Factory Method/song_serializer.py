import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
        # example of a client component
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    # example of a creator component
    # creator component decides which concrete implementation to use
    def _get_serializer(self, format):
        if format == "JSON":
            return self._serialize_to_json
        elif format == "XML":
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    # concrete implementation of an interface
    def _serialize_to_json(self, song):
        paylod = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(paylod)

    # concrete implementation of an interface
    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')


my_song = Song(1, "God's Plan", "Drake")
my_serializer = SongSerializer()
print(my_serializer.serialize(my_song, 'JSON'))
