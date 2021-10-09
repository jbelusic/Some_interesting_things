
case_var = 'off'

def switch_case(msg):
    cases = {
        'close':  'sound1',
        'open':   'sound2',
        'on':     'sound3',
        'off':    'sound4',
        'motion': 'sound5',
    }
    result = cases.get(msg, 'none or default')
    return ('CASE %s: %s' % (msg, result))

print("First case",switch_case(case_var))

###############################
def switch_case1(key):
  choices = {
      'a': 1,
      'b': 2,
      'c': 3
  }
  return choices.get(key, 'default')

print("Second case",switch_case1("b"))
