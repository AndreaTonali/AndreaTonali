from typing import Dict


def dict2bool(d: Dict, key: str):
    if key in d:
        dict_i_want = {k: v for k, v in d.items() if k == key}
        values = dict_i_want.values()
        for i in list(values):
            if i in range(0, 100):
                return True
            else:
                return False
