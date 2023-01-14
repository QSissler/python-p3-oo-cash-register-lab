#!/usr/bin/env python3
import ipdb

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item_cost = 0

  def add_item(self, item_name, price, quantity=1):
    self.total += (price * quantity)
    for i in range(quantity):
      self.items.append(item_name)
    self.last_item_cost = (price * quantity)
  
  def apply_discount(self, discount=20):
    discount_amount = int(self.total * (discount/100))
    self.total -= discount_amount
    if discount_amount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${self.total}.")

  def items(self):
    return self.items

  def void_last_transaction(self):
    self.total -= self.last_item_cost
    