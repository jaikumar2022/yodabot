from typing import Union
from fastapi import FastAPI

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# adding language for compatibility with spacy 3.0
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


app = FastAPI()

yoda_bot = ChatBot(name='yodabot', read_only=True, tagger_language=ENGSM, logic_adapters=['chatterbot.logic.BestMatch'])


personal_loan = ['Personal Loan',
              'Personal loans can help you take the reins of your financial future. Whether you qualify for a personal loan depends on several factors, one of which can be your income. Loan size, term length, credit history, expenses, other financial obligations and the availability of collateral can also be relevant. Each lender has their own system, which may itself be flexible. Please continue reading at https://www.onemainfinancial.com/resources/loan-basics/40000-salary-personal-loan']

taxes = ['How Do Personal Loans Affect My Taxes?',
              'If you have a personal loan, or are considering getting one, you might have questions about your taxes. After all, other loans like mortgages, business loans and student loans can have an impact come tax time. What are the personal loan tax implications, and should you worry? Please continue reading at https://www.onemainfinancial.com/resources/loan-basics/how-do-personal-loans-affect-my-taxes'
              ]

# math_talk_1 = ['pythagorean theorem',
#                'a squared plus b squared equals c squared.']
# math_talk_2 = ['law of cosines',
#                'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']


list_trainer = ListTrainer(yoda_bot)

# for item in (personal_loan, taxes):
#     list_trainer.train(item)


print("In fast api")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/yodabot/{query}")
def ask_yodabot(query: str):

    yodabot_response  = yoda_bot.get_response(query)

    yodabot_response

    print("type = " + str(type(yodabot_response)))

    print(yodabot_response)

    return {str(yodabot_response)}

    #return {"Hellow form Bot"}
