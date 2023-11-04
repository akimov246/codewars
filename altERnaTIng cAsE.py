text = "Hello World 1488!"

def to_alternating_case(string: str) -> str:
    return "".join([char.upper() if char.islower() else char.lower() for char in string])


to_alternating_case(text)


