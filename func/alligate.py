def Alligate (Drug, higherConc, lowerConc, desiredConc, Amount):
      """
      |=Alligate========================|
      |    Drug  :          str
      |    higherConc       [0-1]
      |    lowerConc        [0-1]
      |    desiredConc      [0-1]
      |    Amount (mL) :    INT
      |=================================|
      """

      hc = higherConc ; lc = lowerConc ; dc = desiredConc ; A = Amount

      numer = dc - lc                                 # PROPORTION OF FINAL FROM THE HIGHER CONC
      denom = hc - dc                                 # PROPORTION OF FINAL FROM THE LOWER  CONC

      U = round(A * numer / (numer + denom),2)        # UPPER CONC. VOLUME
      L = round(A * denom / (numer + denom),2)        # LOWER CONC. VOLUME


      #  [hi]\    /numer
      #       [dc]           numer : denom = (parts per)
      #  [lc]/    \denom

      out =  f'RECEPIE FOR\n{Amount}mL of {desiredConc*100}% {Drug}\n{"-"*45}'
      out += f'\n\n\t+ {U}mL of {round(hc*100,2)}% {Drug}'
      out += f'\n\n\t+ {L}mL of {round(lc*100,2)}% {Drug}'
      out += f'\n\n{"-"*45}'
      out += f'\n\\t   {Amount}mL of {round(dc*100,2)}% {Drug}'
      
      
      print (out)
