

def validate_login(authorization):
    if authorization is None:
        print('Bearer token missing')
        return False
    elif authorization != 'Bearer random_bearer_token':
        print('Bearer token invalid')
        return False
    return True