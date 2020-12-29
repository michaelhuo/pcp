def find_buy_sell_stock_prices(array):
  #TODO: Write - Your - Code
  if not array:
    return -1, -1
  size = len(array)
  if size < 2:
    return -1, -1
  buy_price, sell_price = array[0], array[1]
  max_profit = sell_price - buy_price
  min_buy_price = buy_price
  max_sell_price = sell_price
  for cost in array[1:]:
    if cost > sell_price:
      sell_price = cost
      profit = sell_price - buy_price
      if profit > max_profit:
        max_profit = profit
        max_sell_price = sell_price
        min_buy_price = buy_price
    if cost < buy_price:
      buy_price = cost
      sell_price = float('-inf')
  return min_buy_price, max_sell_price
  return -1, -1 #Return a tuple with (high, low) price values
