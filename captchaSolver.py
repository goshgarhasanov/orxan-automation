# https://github.com/2captcha/2captcha-python

import sys
import os
from twocaptcha import TwoCaptcha
def solveCaptcha(imgUrl):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    api_key = os.getenv('APIKEY_2CAPTCHA', '71ac287898523b5356b152e08d23ab59')
    solver = TwoCaptcha(api_key)
    try:
        result = solver.normal(imgUrl)
        return result
    except Exception as e:
        sys.exit(e)
    else:
        sys.exit('solved: ' + str(result))