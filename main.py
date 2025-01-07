"""
프로그램의 최초 진입점입니다.
실질적으로는 Game 객체를 만들고 실행하는 기능만을 수행하고, 실질적인 제어 흐름은 Game 내에 있습니다.
main.py는 진입점의 기능만을 담당하도록 의도되었습니다. 이 파일의 수정은 최소화할 것을 권장합니다.
"""
from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
