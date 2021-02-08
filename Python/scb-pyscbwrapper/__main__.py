from pyscbwrapper import SCB
from tabulate import tabulate
import json


# scb = SCB('sv', 'BE0101', 'BE0101A', )
scb = SCB('sv', 'BE', 'BE0101', 'BE0101A', 'BefolkManad')

print(json.dumps((scb.info()), indent=3, ensure_ascii=False))

print(json.dumps(scb.get_variables(), indent=3, ensure_ascii=False))
