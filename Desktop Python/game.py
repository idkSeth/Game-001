class Installation:
    def __init__(self, health=0, shield=0):
        self.__health = health
        self.__shield = shield
    
    def get_health(self) -> float:
        return self.__health
    
    def get_shield(self) -> float:
        return self.__shield
    
    def set_health(self, health:float) -> None:
        self.__health = health
    
    def set_shield(self, shield:float) -> None:
        self.__shield = shield

class Spy_Center(Installation):
    def __init__(self):
        super().__init__(100, 25) 
        self.__spies = 1
        self.__skill = 1

    def set_spies(self, spies:int) -> None:
        self.__spies = spies
    
    def get_spies(self) -> int:
        return self.__spies
    
    def get_skill(self) -> int:
        return self.__skill
    
    def train(self) -> None:
        self.__skill += 1
    
    def recruit(self) -> None:
        self.__spies += 1

class ICBM(Installation):
    def __init__(self):
        super().__init__(100, 50)
        self.__pt = 1
    
    def get_pt(self) -> int:
        return self.__pt

    def upgrade(self) -> None:
        self.__pt += 1

class ABM(Installation):
    def __init__(self):
        super().__init__(100, 50)
        self.__pt = 1

    def get_pt(self) -> int:
        return self.__pt
    
    def upgrade(self) -> None:
        self.__pt += 1

class Construction(Installation):
    def __init__(self):
        super().__init__(75, 0)
        self.__operation = None
    
    def get_operation(self) -> tuple:
        return self.__operation
    
    def set_operation(self, Installation:Installation, operation) -> None:
        self.__operation = (Installation, operation)

    def operate(self) -> None:
        pass

class Research_Center(Installation):
    def __init__(self):
        super().__init__(75, 0)
        self.__operation = None
    
    def get_operation(self) -> int:
        return self.__operation
    
    def set_operation(self, operation) -> int:
        self.__operation = operation

    def operate(self) -> None:
        pass

class Game:
    def __init__(self, player_name=""):
        self.__player_name = player_name
        self.__money = 5000
        self.__turn = 0
        self.__map = [
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    ]   

    def set_name(self, name:str) -> None:
        self.__player_name = name
        
    def inc_turn(self) -> None:
        self.__turn += 1
    
    def set_money(self, money:int) -> None:
        self.__money = money
    
    def get_money(self) -> int:
        return self.__money

    def get_map(self) -> list:
        return self.__map
    
    def update_map(self, coordinates:tuple, installation:Installation) -> None:
        self.__map[5-coordinates[1]][coordinates[0]] = installation
    
    def get_installation(self, coordinates:tuple) -> Installation:
        return self.__map[5-coordinates[1]][coordinates[0]]

    def set_farm(self, amt:int) -> None:
        self.__farm = amt
    
    def set_car(self, amt:int) -> None:  
        self.__car = amt
    
    def set_elec(self, amt:int) -> None:
        self.__elec = amt
    
    def set_social(self, amt:int) -> None:
        self.__social = amt
    
    def set_tech(self, amt:int) -> None:
        self.__tech = amt

    def set_spy(self, amt:int) -> None:
        self.__spy = amt
    
    def set_icbm(self, amt:int) -> None:
        self.__icbm = amt
    
    def set_abm(self, amt:int) -> None:
        self.__abm = amt

    def set_construct(self, amt:int) -> None:
        self.__construct = amt
    
    def set_rnd(self, amt:int) -> None:
        self.__rnd = amt
    
    def get_farm(self) -> int:
        return self.__farm
    
    def get_car(self) -> int:
        return self.__car
    
    def get_elec(self) -> int:
        return self.__elec
    
    def get_social(self) -> int:
        return self.__social
    
    def get_tech(self) -> int:
        return self.__tech
    
    def get_spy(self) -> int:
        return self.__spy

    def get_icbm(self) -> int:
        return self.__icbm
    
    def get_abm(self) -> int:
        return self.__abm
    
    def get_construct(self) -> int:
        return self.__construct
    
    def get_rnd(self) -> int:
        return self.__rnd
    
    def get_name(self) -> str:
        return self.__name
    
    def get_turn(self) -> int:
        return self.__turn

def income(player) -> int:
    return player.farm * 200 + player.car * 500 + player.elec * 1000 + player.socal * 2000 + player.tech * 3500
