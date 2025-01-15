"""
Player 객체의 비대화를 완완화하기 위해
Party 객체를 별도 클래스로 분리했습니다.
"""
from ally.ally import Ally

class Party():
    """
    딕셔너리를 기반으로 파티를 구현현하는 클래스입니다.
    """
    def __init__(self):
        self.space = {}
        
    def get_party(self)->dict:
        return self.space
        
    def join_party(self, ally:Ally):
        self.space[ally.name] = ally

    def show_party(self):
        print("\n=== 파티 멤버 ===")
        for i, ally in enumerate(self.space):
            print(f"{i}. {self.space[ally].name}/저항도:{self.space[ally].resistance}, 순응도:{self.space[ally].compliance}")
            
    def call_party_member(self, ally_name) -> Ally:
        return self.space[ally_name]