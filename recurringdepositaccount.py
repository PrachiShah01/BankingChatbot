import json
import time
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def recurringDepositAccount(intent_request):
    intent = intent_request['currentIntent']['name']
    slots = intent_request['currentIntent']['slots']
    Inquiry = slots['document']
    
    if(Inquiry == 'document'):
        Result="You need to contact nearby branch with CIF number and cheque of your existing savings account"
        
    return {
                "dialogAction": {
                'type': 'Close',
                'fulfillmentState': 'Fulfilled',
                    'message': {
                        'contentType': 'PlainText',
                        'content': Result,
                    }
                }
            }
    
     
# --- Intents ---

def dispatch(intent_request):
    logger.debug(
        'dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'recurringdepositaccount':
        return recurringDepositAccount(intent_request)
    else:
        raise Exception('Intent with name ' + intent_name + ' not supported')


# --- Main handler ---

def lambda_handler(event, context):
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)