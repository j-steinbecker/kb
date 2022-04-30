def yml (data):
      """ ==Load Raw Yaml==
      ----------------------------------------------
      in:    YAML STRING
      out:   DICT
      ===============================================
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
