import requests


def get_randint(floor: int, ceil: int, url:str='https://www.google.com') -> int:
    '''
    get random integer in range [floor, ceiling] (both inclusive)
    '''
    if ceil < floor:
        raise RuntimeError('ceiling must be greater than floor')
    response = requests.get(url)
    return int(str(response.elapsed.total_seconds())[-1]) % (ceil-floor+1)    
