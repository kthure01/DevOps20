# En klass innehållande viss fast köksutrustning
class Fast_utrustning:
    """Fast utrustning i köket"""
    ugn = 'ugnen'

    # Konstruktorn ska inte finnas i en abstrakt klass
    # def __init__(self):

    def stall_in_ugns_temparatur(self, temp):
        return f'{temp} grader'
