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


@app.get("/yodabotv2/{query}")
def ask_yodabot(query: str):

    str_respone = ''

    if(query.upper() in 'Can I Get a Personal Loan if my Salary is $40,000?'.upper()):
        print(1)
        str_respone='Personal loans can help you take the reins of your financial future. Whether you qualify for a personal loan depends on several factors, one of which can be your income. Loan size, term length, credit history, expenses, other financial obligations and the availability of collateral can also be relevant. Each lender has their own system, which may itself be flexible. Please continue reading at https://www.onemainfinancial.com/resources/loan-basics/40000-salary-personal-loan'
    
    elif(query.upper() in 'How Do Personal Loans Affect My Taxes?'.upper()):
        print(2)
        str_respone='If you have a personal loan, or are considering getting one, you might have questions about your taxes. After all, other loans like mortgages, business loans and student loans can have an impact come tax time. What are the personal loan tax implications, and should you worry? Please continue reading at https://www.onemainfinancial.com/resources/loan-basics/how-do-personal-loans-affect-my-taxes'    
    
    elif(query.upper() in 'How Much Does the Average Wedding Cost?'.upper()):
        print(3)
        str_respone='In 2021, American couples spent an average of $28,000 on their weddings, so it\'s safe to say the average cost of a wedding in 2022 will be a little higher because of inflation. That number includes the ceremony and reception, while the cost of engagement rings bumped up the total to $34,000.1 Please continue reading at https://www.onemainfinancial.com/resources/everyday-living/average-wedding-cost'
    
    elif(query.upper() in 'Career Advice for New Graduates'.upper()):
        print(4)
        str_respone='t’s an exciting time, but it also can be a daunting one. Where do you start? How can you stand out in a crowded job market? And how can you highlight your work experience if you don’t have much in the first place? \n From resumes and networking to locking down your social media accounts, OneMain senior recruiter Davida Black is here to address.. Please continue reading at https://www.onemainfinancial.com/resources/everyday-living/career-advice-for-new-graduates'
    
    elif(query.upper() in 'How Do Late Payments Affect Your Credit Score?'.upper()):
        print(5)
        str_respone='Payment history is the most important factor in two of the most common credit scoring models: FICO Score and VantageScore.1 This means one late loan or credit payment could potentially make your score go down. And depending on how long your payment remains unpaid (60 days, 90 days, 120 days, etc.), your score might continue to drop. If your account is ultimately charged off by the lender as bad debt and sent to collections, that can be reported too... Please continue reading at https://www.onemainfinancial.com/resources/credit/how-do-late-payments-affect-your-credit-score'    
    
    elif(query.upper() in 'What Happens if You Pay off a Personal Loan Early'.upper()):
        print(5)
        str_respone='If you’ve found yourself with extra money and wanted to put it towards paying down debt, you might be wondering if you can pay off a personal loan early. The short answer is yes... Please continue reading at https://www.onemainfinancial.com/resources/loan-basics/should-you-pay-off-a-personal-loan-early'
       
    else:
        print(7)
        str_respone='If you have a personal loan, or are considering getting one, you might have questions about your taxes. After all, other loans like mortgages, business loans and student loans can have an impact come tax time. What are the personal loan tax implications, and should you worry? Please continue reading at https://www.onemainfinancial.com/resources/loan-basics/how-do-personal-loans-affect-my-taxes'



    # yodabot_response  = yoda_bot.get_response(query)

    # yodabot_response

    # print("type = " + str(type(yodabot_response)))

    # print(yodabot_response)

    return {str_respone}

    #return {"Hellow form Bot"}
