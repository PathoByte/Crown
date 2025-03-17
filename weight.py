weight = int(input('what is your weight'))
unit = input('Kgs or Lbs')
if unit.upper() == 'Kgs': 
    converted = weight/0.45
    print('weight in Lbs:' + str(converted ))
else:  
    converted = weight * 0.45
    print ('weight in Kgs:' + str(converted))
