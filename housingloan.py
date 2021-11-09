import json
import time
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def housingLoan(intent_request):
    intent = intent_request['currentIntent']['name']
    slots = intent_request['currentIntent']['slots']
    Inquiry = slots['loancontent']
    
    if(Inquiry == 'avialloan'):
        Result="For housing loan visit this website: https://homeloans.sbi/products/view/regular-home-loan"
        
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
    if intent_name == 'housingloan':
        return housingLoan(intent_request)
    else:
        raise Exception('Intent with name ' + intent_name + ' not supported')


# --- Main handler ---

def lambda_handler(event, context):
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)