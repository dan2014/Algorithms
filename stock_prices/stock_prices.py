#!/usr/bin/python

import argparse

def find_max_profit(prices):
  prices_len = len(prices)
  # arr_min = {
  #             "index":len(prices)-1,
  #             "value":None
  #           }
  # arr_max = {
  #             "index":len(prices)-1,
  #             "value":None
  #           }
  cache = {
            "min":{
                    "index":0,
                    "value":prices[0]
                  },
            "max":{
                    "index":0,
                    "value":prices[0]
                  }
          }
  diff = float("-inf")

  for i in range(1,prices_len):
    if(prices[i-1] - prices[i] > diff and cache["min"]["index"] > i):
      diff = prices[i-1] - prices[i]
      cache["min"]["value"], cache["min"]["index"] = prices[i],i
      cache["max"]["value"], cache["max"]["index"] = prices[i-1],i
      print("min",cache["min"]["value"])
    
    # if(prices[i] < cache["min"]["value"]):
    #   cache["min"]["value"], cache["min"]["index"] = prices[i],i
    # if(prices[i] > cache["max"]["value"]):
    #   cache["max"]["value"], cache["max"]["index"] = prices[i],i

    print("diff",diff)

  print("sub",cache["max"]["value"] - cache["min"]["value"])
  print(cache["max"]["value"],cache["min"]["value"])


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  # parser = argparse.ArgumentParser(description='Find max profit from prices.')
  # parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  # args = parser.parse_args()

  # print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  find_max_profit([1050, 270, 1540, 3800, 2])