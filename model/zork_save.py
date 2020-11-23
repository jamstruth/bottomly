from pymodm import MongoModel, fields
from pymongo import WriteConcern
from enum import Enum
from config import Config


class ZorkGame(Enum):
    ZORK_ONE ="zork1"
    ZORK_TWO ="zork2"
    ZORK_THREE="zork3"

class ZorkSave(MongoModel):

    slack_channel = fields.CharField(primary_key=True)
    game_type = fields.CharField()
    session_id = fields.CharField()
    session_id = fields.CharField()

    @staticmethod
    def get_save_by_channel(channel_id):
        saves = list(ZorkSave.objects.raw({'_id': channel_id}))
        if (len(saves) == 0):
            return None
        else:
            return saves[0]

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = Config.Connection