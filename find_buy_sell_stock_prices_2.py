def find_buy_sell_stock_prices(array):
  #TODO: Write - Your - Code
  if not array:
    return -1, -1
  size = len(array)
  if size < 2:
    return -1, -1
  min_left = [float('inf')] * size;
  max_right = [float('-inf')] * size;
  minimum = float('inf')
  maximum = float('-inf')
  for i, n in enumerate(array[:-1]):
    minimum = min(minimum, n)
    min_left[i] = minimum
  for i in range(size - 1, 0, -1):
    maximum = max(maximum, array[i])
    max_right[i] = maximum
  max_profit = float('-inf')
  min_buy_price = float('inf')
  max_sell_price = float('-inf')
  for i in range(size - 1):  
    profit = max_right[i + 1] - min_left[i]
    if profit > max_profit:
      max_profit = profit
      min_buy_price = min_left[i]
      max_sell_price = max_right[i + 1]
  return min_buy_price, max_sell_price

