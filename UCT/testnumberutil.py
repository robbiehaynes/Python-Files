#testnumberutil.py
#20 May 2021
#Rob Haynes

"""
>>> import numberutil
>>> numberutil.aswords(200)
'two hundred'
>>> numberutil.aswords(204)
'two hundred and four'
>>> numberutil.aswords(330)
'three hundred and thirty'
>>> numberutil.aswords(8)
'eight'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(456)
'four hundred and fifty six'
>>> numberutil.aswords(52)
'fifty two'

"""
import doctest
doctest.testmod(verbose=True)