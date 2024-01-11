def abbrev_name(name):
  name_split = name.split()
  return f"{name_split[0][0].upper()}.{name_split[1][0].upper()}"
