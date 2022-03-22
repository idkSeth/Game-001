class Game:
    def __init__(self):
        self.palyer_name = ""
        self.money = 5000
        self.turn = 0
        self.map = [
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    ]   

    def set_name(self, name:str) -> None:
        self.plaer_name = name
        
    def inc_turn(self) -> None:
        self.turn += 1
    
    def set_money(self, money:str) -> None:
        self.money = money
    
    def get_map(self) -> list:
        return self.map
    
    def update_map(self, coordinates:tuple, installation) -> None:
        self.map[5-coordinates[1]][coordinates[0]] = installation
    
    def get_installation(self, coordinates:tuple):
        return self.map[5-coordinates[1]][coordinates[0]]

    def set_farm(self, amt:int) -> None:
        self.farm = amt
    
    def set_car(self, amt:int) -> None:  
        self.car = amt
    
    def set_elec(self, amt:int) -> None:
        self.elec = amt
    
    def set_social(self, amt:int) -> None:
        self.social = amt
    
    def set_tech(self, amt:int) -> None:
        self.tech = amt

    def set_spy(self, amt:int) -> None:
        self.spt = amt
    
    def set_icbm(self, amt:int) -> None:
        self.icbm = amt
    
    def set_abm(self, amt:int) -> None:
        self.abm = amt

    def set_construct(self, amt:int) -> None:
        self.construct = amt
    
    def set_rnd(self, amt:int) -> None:
        self.rnd = amt

class Installation:
    def __init__(self):
        self.health = 0
        self.shield = 0
    
    def get_health(self) -> float:
        return self.health
    
    def get_shield(self) -> float:
        return self.shield
    
    def set_health(self, health:float) -> None:
        self.health = health
    
    def set_shield(self, shield:float) -> None:
        self.shield = shield
    
    

def income(player) -> int:
    return player.farm * 200 + player.car * 500 + player.elec * 1000 + player.socal * 2000 + player.tech * 3500

def start():
    player1, player2 = Game(), Game()