def uc_first(string: str) -> str:
    return str(string)[0].upper() + str(string)[1:] if string else ''
