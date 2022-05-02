def monthlypayment (P, apr, yrs):
   """
   |----MORTGAGE PAYMENT-----------------------------------
   |                       --> Returns MONTHLY PAYMENT IN $
   |-------------------------------------------------------
   |   >>> P     : principle
   |   >>> apr   : decimal APR
   |   >>> yrs   : length of term in years
   |======================================================
   """
      
   r = apr / 12       # MONTHLY PERCENTAGE RATE
   n = yrs * 12       # NUMBER OF MONTHS
   
   # MONTHLY PAYMENT
   mp = round(P * r * ((r+1)**n) / ((r+1)**n-1) , 2)

   return mp
  
   #-----------------------------------------------------
