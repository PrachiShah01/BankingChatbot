import json
import time
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def personalCurrentAccount(intent_request):
    intent = intent_request['currentIntent']['name']
    slots = intent_request['currentIntent']['slots']
    Inquiry = slots['currentaccounttype']
    
    if(Inquiry == 'personal'):
        Result="You need to contact nearby branch with PAN card and ADHAR card."
    elif(Inquiry == 'proprietory'):
        Result="You need to contact nearby branch with Registration Certificate of firm and letter issued by UIDAI containing details of name, address and ADHAR."
        
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
    if intent_name == 'currentaccount':
        return personalCurrentAccount(intent_request)
    else:
        raise Exception('Intent with name ' + intent_name + ' not supported')


# --- Main handler ---

def lambda_handler(event, context):
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)