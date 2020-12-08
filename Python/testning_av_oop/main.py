class VehicleA:
    va_class_var1 = None
    va_class_var2 = None

    def __init__(self):
        print('va__init__')
        self.va_inst_self1 = None
        self.va_inst_self2 = None

    def va_first_met(self):
        print('va_first_met')


class VehicleB:
    vb_class_var1 = None
    vb_class_var2 = None

    def __init__(self):
        print('vb__init__')
        self.vb_inst_self1 = None
        self.vb_inst_self2 = None

    def vb_first_met(self):
        print('vb_first_met')


class Car(VehicleA, VehicleB):

    def __init__(self):
        super().__init__()
        self.vab_class_self1 = None


a = lambda x: x * 2
for i in range(1, 5):
    b = a(i)
    print(b)
