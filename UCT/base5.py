# test program for Gumatj calculations
# hussein suleman
# 6 april 2011

import gumatj

choice = input ("Choose test:\n")
action = choice[:1]
print ("calling function")
if action == 'g' or action == 'd':
   num = int(choice[2:])
   if action == 'g':
      answer = gumatj.gumatj_to_decimal (num)
   else:
      answer = gumatj.decimal_to_gumatj (num)
elif action == 'a' or action == 'm':
   num1, num2 = map (int, choice[2:].split(" "))
   if action == 'a':
      answer = gumatj.gumatj_add (num1, num2)
   else:
      answer = gumatj.gumatj_multiply (num1, num2)
print ("called function")
print (answer)
