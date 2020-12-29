def find_buy_sell_stock_prices(array):
  #TODO: Write - Your - Code
  if not array:
    return -1, -1
  size = len(array)
  if size < 2:
    return -1, -1
  max_profit = float('-inf')
  buy_price = float('inf')
  sell_price = float('-inf')
  min_buy_price = buy_price
  max_sell_price = sell_price
  for i, cost in enumerate(array):
    if buy_price == float('inf'):
      buy_price = cost
    elif cost > sell_price:
        sell_price = cost
        profit = sell_price - buy_price
        if profit > max_profit:
          max_profit = profit
          max_sell_price = sell_price
          min_buy_price = buy_price
    elif cost < buy_price:
        buy_price = cost
        sell_price = float('-inf')
  return min_buy_price, max_sell_price

