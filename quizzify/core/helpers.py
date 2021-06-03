import time
import random
import uuid

START_TIME = 343897500

def generate_random_id():
  # inspired by http://instagram-engineering.tumblr.com/post/10853187575/sharding-ids-at-instagram
  t = int(time.time()*1000) - START_TIME
  u = random.SystemRandom().getrandbits(3)
  id = (t << 3 ) | u
  return id

def reverse_random_id(id):
  t  = id >> 3
  return t + START_TIME


def generate_random_hash():
  return uuid.uuid5(uuid.NAMESPACE_DNS, str(generate_random_id()))

def error_to_array(err):
  dictlist = []
  for key, value in err.items():
    print(value)
    if value[0]:
      temp = key + ': ' + value[0]
    dictlist.append(temp)
  return dictlist

def key_and_value_exists(element, *keys):
    '''
    Check if *keys (nested) exists in `element` (dict).
    '''
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False

    if _element is None:
        return False
    return True