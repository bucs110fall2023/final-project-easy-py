from src.sample_controller import *
def test():
    test = Controller()
    test.state = "BATTLE"
    test.battle_gameloop()
test()