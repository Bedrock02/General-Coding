def CaesarCharShift(charPassed,shiftNum):
  shiftNum = shiftNum%26
  ascciiNum = ord(charPassed)-shiftNum
  if ascciiNum < 65:
    ascciiNum = ascciiNum + 26
  return chr(ascciiNum)