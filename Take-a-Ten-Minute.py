def is_valid_walk(walk):
    if (walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10):
            return True
    return False


print(is_valid_walk(['n']))