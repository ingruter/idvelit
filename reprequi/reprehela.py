def get_price(price, decimal):
  """
  Return the price with the decimal places removed.

  Args:
    price: The price as a string.
    decimal: The number of decimal places to remove.

  Returns:
    The price with the decimal places removed.
  """

  return price / int("".join((["1"]+ ["0"]*decimal)))
