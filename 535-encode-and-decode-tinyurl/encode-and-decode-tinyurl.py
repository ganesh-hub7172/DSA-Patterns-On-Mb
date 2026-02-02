class Codec:
    def __init__(self):
        self.map = {}
        self.count = 0

    def encode(self, longUrl):
        shortUrl = "http://tinyurl.com/" + str(self.count)
        self.map[shortUrl] = longUrl
        self.count += 1
        return shortUrl

    def decode(self, shortUrl):
        return self.map[shortUrl]
