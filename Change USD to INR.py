import math

def calculate_total_amount():
  """
  Calculates the total amount to be paid, including the exchange rate and processing fee.

  Args:
    amount: The amount in USD.
    exchange_rate: The exchange rate between USD and INR.
    processing_fee: The processing fee charged by the bank.

  Returns:
    The total amount to be paid.
  """
  amount = float(input('Enter the Amount in USD: '))
  exchange_rate = float(input('Enter the Exchange Rate: '))
  processing_fee = float(input('Enter the Processing Fee: '))
  processing_fee = amount * processing_fee / 100
  processing_fee = processing_fee * exchange_rate

  total_amount_in_inr = amount * exchange_rate
  total_amount = total_amount_in_inr + processing_fee

  total_pay = f"The total amount to be paid is: {math.ceil(total_amount)}."


  return total_pay

  
  
print(calculate_total_amount())
