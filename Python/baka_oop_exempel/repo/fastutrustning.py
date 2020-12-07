# En klass innehållande viss fast köksutrustning
class FastUtrustning:
    """Fast utrustning i köket"""
    ugn = 'ugnen'
    ugnstemperatur = 0

    def stall_in_ugns_temparatur(self, temp):
        self.ugnstemperatur = temp
        # return f' {ugnstemperatur} grader'
