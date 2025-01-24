
from typing import TypedDict, List, NotRequired

class DungeonType(TypedDict):
    """
    "2":{
        "enemy":[],
        "item":[],
        "boss":["karsen"]
    },
    """
    enemy: List[str]
    item: List[str]
    boss: NotRequired[List[str]]

class EnemyType(TypedDict):
    """
    "goblin": {
        "name": "고블린",
        "health": 30,
        "attack_power": 10,
        "defense_power": 0,
        "speed": 50,
        "exp":100,
        "behavior":["common_attack"]
    },
    """
    users: List[User]
    total: int
    name: str
    health: int
    attack_power: int
    defense_power: int
    speed: int
    exp: int
    behavior: List[str]

class DungeonType(TypedDict):
    """
    "2":{
        "enemy":[],
        "item":[],
        "boss":["karsen"]
    },
    """
    enemy: List[str]
    item: List[str]
    boss: NotRequired[List[str]]
    
class DungeonType(TypedDict):
        """
        "2":{
            "enemy":[],
            "item":[],
            "boss":["karsen"]
        },
        """
        enemy: List[str]
        item: List[str]
        boss: NotRequired[List[str]]
    
class DungeonType(TypedDict):
            """
            "2":{
                "enemy":[],
                "item":[],
                "boss":["karsen"]
            },
            """
            enemy: List[str]
            item: List[str]
            boss: NotRequired[List[str]]
            