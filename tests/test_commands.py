
import pytest
from unittest.mock import patch
from commands import InfoCommand, ExploreCommand, QuitCommand, FocusCommand
from game import Game
from dungeon import Dungeon
from player import Player

def test_info_command():
    game = Game()
    command = InfoCommand()
    try:
        command.execute(game, game.dungeon, game.player)
        assert True
    except Exception:
        assert False

def test_explore_command():
    game = Game()
    command = ExploreCommand()
    
    # "passage" 이벤트 발생 시 다음 층으로 이동하는 경우
    with patch('builtins.input', return_value="1"):
        with patch('dungeon.Dungeon.get_random_element', return_value="passage"):
            command.execute(game, game.dungeon, game.player)
            assert game.dungeon.current_floor > 0

def test_focus_command():
    game = Game()
    command = FocusCommand()
    
    # "체크" 명령어 테스트
    with patch('builtins.input', return_value="1"):
        command.execute(game, game.dungeon, game.player)
        
    # "픽" 명령어 테스트
    with patch('builtins.input', side_effect=["2", "begin_the_game"]):
        command.execute(game, game.dungeon, game.player)
