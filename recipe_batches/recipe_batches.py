#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  arr_batches = []
  if(len(recipe) != len(ingredients)):
    return batches
  else:
    for i,z in zip(recipe.values(),ingredients.values()):
      arr_batches.append(z//i)

    arr_min = arr_batches[0]
    for a in arr_batches:
      if(a < arr_min):
        arr_min = a
    batches = arr_min
    return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  # recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  # ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  # recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 }
  # ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }

  # recipe = { 'milk': 2 }
  # ingredients =  { 'milk': 200}
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients =  { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))