import json


class StorageRoomEncoder(json.JSONEncoder):
    def default(self, storage_room):
        try:
            to_serialize = {
                'code': storage_room.code,
                'size': storage_room.size,
                'price': storage_room.price,
                "latitude": storage_room.latitude,
                "longitude": storage_room.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(storage_room)
