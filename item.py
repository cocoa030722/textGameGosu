"""
게임에서의 아이템을 구현하는 코드입니다.
"""

class Item():
    """
    아이템의 정보와 행동을 저장하는 클래스입니다.
    각 아이템을 개별적인 클래스로 구현현하는 것이 아닌, Item 클래스의 정보만을 달리하여 각각의 아이템을 구현합니다.
    """
    def __init__(self, name:str, description:str):
        self.name:str = name
        self.description:str = description
        
    def use(self, player:"Player"):
        """
        모든 아이템은 사용 시 호출되는 use 메소드를 가집니다.
        구체적 구현은 아직 없습니다.
        """
        pass

