from pymodm import MongoModel, fields
from pymongo import WriteConcern
from config import Config


class Zork_Game(Enum):
    Zork_One="zork1"
    Zork_Two="zork2"
    Zork_Three="zork3"

class Zork_Save(MongoModel):

    slackChannel = fields.CharField(primary_key=True)
    gameType = fields.CharField()
    session_id = fields.CharField()

    @staticmethod
    def get_save_by_channel(channel_id):
        saves = list(Zork_Save.objects.raw({'_id': channel_id}))
        if (len(saves) == 0):
            return None
        else:
            return saves[0]

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = Config.Connection