#!/usr/bin/python

import argparse

def find_max_profit(prices):
  prices_len = len(prices)
  left = prices[0]
  right = prices[1]
  diff = right - left
  for i in range(2,prices_len):
    if(prices[i] - left > diff):
      right = prices[i]
      diff = right - left
      if(right - prices[i-1] > diff):
        left = prices[i-1]
        diff = right - left
  
  return diff


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))