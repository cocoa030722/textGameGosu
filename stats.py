
class Stats:
    """
    Entity의 요소 중 단순한 int 및 원시 자료형으로 처리할 수 있는, 계산의 기본값이 되는 모든 요소는 여기에 포함합니다.
    이 클래스는 가장 데이터 자체에 근접한 원시적 처리(getter/setter 등)믈 담당하도록 합니다.
    """
    def __init__(self, health:int, attack_power:int, defense_power:int, exp:int, mp:int, max_mp:int, speed:int):
        self._health:int = health
        self._max_health:int = health
        self._attack_power:int = attack_power
        self._defense_power:int = defense_power
        self._exp:int = exp
        self._mp:int = mp
        self._max_mp:int = max_mp
        self._speed:int = speed

    @property
    def health(self)->int:
        return self._health

    @health.setter
    def health(self, value:int)->None:
        if value < 0:
            self._health = 0
        elif self.max_health < value:
            self._health = self.max_health
        else:
            self._health = value

    @property
    def mp(self)->int:
        return self._mp

    @mp.setter
    def mp(self, value:int)->None:
        if value < 0:
            self._mp = 0
        elif self.max_mp < value:
            self._mp = self.max_mp
        else:
            self._mp = value

    @property
    def max_health(self)->int:
        return self._max_health

    @max_health.setter
    def max_health(self, value:int)->None:
        self._max_health = value

    @property
    def attack_power(self)->int:
        return self._attack_power

    @attack_power.setter
    def attack_power(self, value:int) -> None:
        #immutability above all
        #self.attack += amount
        self._attack_power = value

    @property
    def defense_power(self)->int:
        return self._defense_power

    @defense_power.setter
    def defense_power(self, value:int) -> None:
        self._defense_power = value

    @property
    def exp(self)->int:
        return self._exp

    @exp.setter
    def exp(self, value:int)->None:
        self._exp = value

    @property
    def max_mp(self)->int:
        return self._max_mp

    @max_mp.setter
    def max_mp(self, value:int)->None:
        self._max_mp = value

    @property
    def speed(self)->int:
        return self._speed

    @speed.setter
    def speed(self, value:int)->None:
        self._speed = value
