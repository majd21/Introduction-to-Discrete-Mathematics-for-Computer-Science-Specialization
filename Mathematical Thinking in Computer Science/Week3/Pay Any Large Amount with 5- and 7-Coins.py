def change(amount):
  if amount == 24:
    return [5, 5, 7, 7]
  if amount % 5 == 0:
    return [5] * (amount//5)
  if amount % 7 == 0:
    return [7] * (amount//7)

  coins = change(amount-5)
  coins.append(5)
  return coins


