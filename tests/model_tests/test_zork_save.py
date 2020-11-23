import unittest, random, string
from model.zork_save import ZorkGame, ZorkSave
from config import Config
from unittest.mock import patch


class TestZorkSave(unittest.TestCase):

    def test_persistence(self):
        # Arrange
        Config().connect_to_db()
        letters = string.ascii_letters
        slack_channel = ''.join(random.choice(letters) for i in range(32))
        game_type = random.choice(list(ZorkGame))
        session_id = ''.join(random.choice(letters) for i in range(32))
        zs = ZorkSave(slack_channel, game_type, session_id)

        # Act
        zs.save()

        # Assert
        retrieved_saves = ZorkSave.objects.raw({'_id': slack_channel})
        self.assertEqual(1, retrieved_saves.count())
        self.assertEqual(zs, retrieved_saves[0])

        # Tear down
        zs.delete()