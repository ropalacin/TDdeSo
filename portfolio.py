def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    #crear clase que sea dolar y un argumento que sea 5 y eso van a ser nuestros 5 dolares.
    class Dollar:
        def __init__(self, amount):
            self.amount = amount

        def times(self, multiplier):
            return Dollar(self.amount * multiplier)
    #queremos traer un objeto de la clase dolar (instanciar el dolar en una cantidad que sea eso por multiplicar)

    def test_multiplication():
        # test that you can multiply a Dollar by a number and get the right amount.
        five = Dollar(amount=5)
        # a esos cinco usd le vamos a implementar el método multiplicacion
        #este paso no es muy bueno porque modifica el objeto original
        five.times(multiplier=2)
        assert 10 == five.amount
        #si el 5 no cambió, al multiplicarlo por 3 debería ser 15!
        five.times(multiplier=3)
        assert 15 == five.amount
        
