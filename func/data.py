import datetime as dt


def yml (data):
      """
      ==Load Raw Yaml==
      ----------------------------------------------
      [[YAML STRING]]                   --> [[DICT]]
      ==============================================
      >>> Data    : str [[formatted yml]]
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      """
      import yaml
      return yaml.load(data, Loader=yaml.Loader)
    
def ymlFlattenDates (data):
      if type(data) == str:
            data = yml(data)
      else:
            pass

      dic = {}
      for yr,val in data.items():
            for mo,val in val.items():
                  for day,shift in val.items():
                        dic.update({str(yr)+"-"+str(mo)+"-"+str(day): shift})
      return dic

def accumulate (Set, specialReturn= None) -> list:
   """_summary_
            Running Total Accumulation 
            of List of numbers

      >>> Set = [2, 3,  7, 12, 14, 16, 2]
      >>> accumulate(Set)
                [2, 5, 12, 24, 38, 54, 56]
   ---------------------------------------
   """
   accum = [0]
   
   for x in Set:
      new = accum[-1] + x
      accum.append(new)
      
   if specialReturn == 'md':
      md_str = ""
      for x in range(len(Set)):
         ob = '{'; cb = '}'
         md_str += f'\\xrightarrow{ob}+{Set[x]}{cb} {accum[x+1]}'
      
      md = "$" + md_str + "$"
      
      return Markdown(md)
   else:
      pass
   
   if specialReturn == None:
      return accum[1:] 

