from typing import Optional

def str_to_float(string:str) -> Optional[float]:
    try:
        strfloat = float(string)
        return strfloat
    except:
        return None