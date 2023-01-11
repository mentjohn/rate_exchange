#Import the required dependencies
import requests
from key import api_key
from key import to_curr


#Ask user to input currencies for conversion and the amount
def get_user_input():
    curr_from = input("Please enter the currency from which you would like to convert: ").upper()
    # curr_to = input('Please enter the currency to which you would like to convert: ').upper()
    print("The target currency is "+ to_curr +" by default")
    amount = int(input("Please the amount you would like to convert: "))
    return curr_from, to_curr, amount


#Get converted amount
def get_converted_amount(curr_from, to_curr, amount):
    #Create a URL for pair converstion
    url = 'https://v6.exchangerate-api.com/v6/{}/pair/{}/{}/{}'.format(api_key,curr_from,to_curr,amount)
    #Parse the result as JSON
    data = requests.get(url).json()
    #Extract the converted amount
    converted_amount = data['conversion_result']
    
    return converted_amount


if __name__ == '__main__':
    curr_from, to_curr, amount =  get_user_input()
    converted_amount = get_converted_amount(curr_from, to_curr, amount)
    print(f'{amount} {curr_from} = {converted_amount} {to_curr}')
