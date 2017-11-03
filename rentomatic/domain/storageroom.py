class StorageRoom:
    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dictionary(cls, dictionnary):
        return StorageRoom(
            code=dictionnary['code'],
            size=dictionnary['size'],
            price=dictionnary['price'],
            latitude=dictionnary['latitude'],
            longitude=dictionnary['longitude'],
        )
