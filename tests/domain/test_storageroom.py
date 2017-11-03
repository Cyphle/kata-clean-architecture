import unittest
import uuid
from rentomatic.domain.storageroom import StorageRoom


class StorageRoomTest(unittest.TestCase):
    def test_initialize_storage_room(self):
        storage_room_code = uuid.uuid4()
        storage_room = StorageRoom(
            storage_room_code,
            size=200,
            price=10,
            longitude=-0.09998975,
            latitude=51.75436293
        )
        assert storage_room.code == storage_room_code
        assert storage_room.size == 200
        assert storage_room.price == 10
        assert storage_room.longitude == -0.09998975
        assert storage_room.latitude == 51.75436293

    def test_initialize_storage_room_from_dictionary(self):
        storage_room_code = uuid.uuid4()
        storage_room = StorageRoom.from_dictionary(
            {
                'code': storage_room_code,
                'size': 200,
                'price': 10,
                'longitude': -0.09998975,
                'latitude': 51.75436293
            }
        )
        assert storage_room.code == storage_room_code
        assert storage_room.size == 200
        assert storage_room.price == 10
        assert storage_room.longitude == -0.09998975
        assert storage_room.latitude == 51.75436293
