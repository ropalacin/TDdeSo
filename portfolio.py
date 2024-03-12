class Dollar:
        def __init__(self, amount):
            self.__amount = amount

        def times(self, multiplier):
            return Dollar(self.__amount * multiplier)
        
        def __eq__(self,dollar):
            return self.__amount == dollar.__amount
          
def test_franc_multiplication():
        five = Dollar(amount=5)
        assert Dollar(amount=10) == five.times(multiplier=2)
        assert Dollar(amount=15) == five.times(multiplier=3) 

def test_equality():
        assert Dollar(3)== Dollar(3)
        assert Dollar(3)!= Dollar(4)

        #modifico el test para que "amount" sea un atributo prviado (no modificable)