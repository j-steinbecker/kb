def monthlyPayment (P, apr, yrs):
   """----MORTGAGE PAYMENT--------------------------------
   Returns MONTHLY PAYMENT IN $
   -------------------------------------------------------
   from args:
      >>> P     : principle
      >>> apr   : decimal APR
      >>> yrs   : length of term in years
   ======================================================
   """
      
   r = apr / 12
   n = yrs * 12
   
   mp = round(P * r * ((r+1)**n) / ((r+1)**n-1) , 2)
   #print (f'Monthly Payment:\t\t${mp}')
  
   return mp
   #------------------------------------------------------------------ 
