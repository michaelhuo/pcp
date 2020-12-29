class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second

def merge_intervals(v):
  # write your code here
  if not v:
    return None
  result = []
  start, end = v[0].first, v[0].second
  for p in v[1:]:
    if p.first <= end:
      if end < p.second:
        end = p.second
    else:
      pair = Pair(start, end)
      result.append(pair)
      start, end = p.first, p.second
  pair = Pair(start, end)
  result.append(pair)
  
  return result
