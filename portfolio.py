def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    #crear clase que sea dolar y un argumento que sea 5 y eso van a ser nuestros 5 dolares.
    class Dollar:
        def __init__(self, amount):
            self.amount = amount

        def times(self, multiplier):
            self.amount *= multiplier

    def test_multiplication():
        # test that you can multiply a Dollar by a number and get the right amount.
        five = Dollar(amount=5)

        # a esos cinco usd le vamos a implementar el método multiplicacion
        five.times(multiplier=2)
        assert 10 == five.amount
