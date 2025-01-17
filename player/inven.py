"""
player 객체의 비대화를 완화하기 위해 Inventory를 별도의 객체로 분리했습니다.
"""
from item import Item

class Inventory():
    """
    리스트를 중심으로 인벤토리의 기능을 하는 클래스입니다.
    """
    def __init__(self):
        self.space:list = []
        self.max_inventory:int = 10
    
    def add_item(self, item_data:dict):
        if len(self.space) < self.max_inventory:
            #FIXME:일단 아이템의 보편성 구현을 우선하고, 사용 기능을 일시적으로 삭제함
            item = Item(
                item_data["name"],
                item_data["description"],
                **item_data
            )
            self.space.append(item)
            print(f"{item.name} 발견! 인벤토리에 추가했다.")
        else:
            print("인벤토리 가득 참!")
        
    def use_item(self, index:int):
        if 0 <= index < len(self.space):
            item = self.space.pop(index)
            item.use(self)
        else:
            print("Invalid item index!")
            
    def show_inventory(self):
        if not self.space:
            print("인벤토리에는 아무것도 없다!")
            return
        print("\n=== 인벤토리 ===")
        for i, item in enumerate(self.space):
            print(f"{i}. {item.name}: {item.description}")