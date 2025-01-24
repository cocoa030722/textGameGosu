from typing import TypedDict, List, NotRequired, Union, Dict

class FocusEffect(TypedDict):
    add_behavior: NotRequired[Dict[str, str]]
    modify_field: NotRequired[Dict[str, int]]
    set_field: NotRequired[Dict[str, int]]

class Focus(TypedDict):
    id: str
    name: str
    description: str
    prerequisites: List[str]
    children: List[str]
    mutual_exclusion: List[str]
    effect: FocusEffect

class FocusTree(TypedDict):
    focus_tree: List[Focus]

class Item(TypedDict):
    type: str
    name: str
    description: str
    heal_amount: NotRequired[int]
    attack_bonus: NotRequired[int]
    reduce_resistance: NotRequired[int]

class ItemDict(TypedDict):
    items: Dict[str, Item]

class BossScript(TypedDict):
    before_fight: List[str]
    after_fight: List[str]

class Boss(TypedDict):
    name: str
    health: int
    attack_power: int
    defense_power: int
    exp: int
    behavior: List[str]
    script: BossScript

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
    name: str
    health: int
    attack_power: int
    defense_power: int
    speed: int
    exp: int
    behavior: List[str]