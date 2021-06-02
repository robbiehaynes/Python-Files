#Rob Haynes
#20 May 2021

"""
>>> import timeutil
>>> timeutil.validate("14:61 a.m.")
False
>>> timeutil.validate("00:59 a.m.")
False
>>> timeutil.validate("112:59 a.m.")
False
>>> timeutil.validate(":59 a.m.")
False
>>> timeutil.validate("11:59 x.m.")
False
>>> timeutil.validate("11:5 a.m.")
False

"""
import doctest
doctest.testmod(verbose=True)