import requests
from constants import GOOGLE_API_TOKEN, GOOGLE_URL, DISCORD_BOT_GOOGLE_KEYWORD, \
    DISCORD_BOT_RECENT_KEYWORD
from utils import get_top_five_link
from db_connection import inser_to_db, search_from_db
import logging

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


# Function to call google api, three params is mandatory for calling google api
def get_result_from_search(searchquery):
    try:
        if searchquery:
            url = GOOGLE_URL
            params_dict = (('q', searchquery), ('key', GOOGLE_API_TOKEN),
                           ('cx', '009019762040196071011:mpuvahqhakm'))
            print(url)
            res = requests.get(url, params=params_dict,
                               headers={"Accept": "application/json"},
                               timeout=100)
            if res.status_code in (200, 201):
                logging.info('Response Received from Google')
                # checking  count of total results from google search
                total_results = int(res.json()['searchInformation']['totalResults'])
                # if count is greater than zero
                if total_results > 0:
                    response = res.json()['items']
                    print(get_top_five_link(response))
                    results_to_send = get_top_five_link(response)
                    return results_to_send
                else:
                    return 'No results Found'



    except Exception as e:
        logger.error('some error in calling google api')
        logger.error(e)
        return 'we will get back soon'


# bot reply here splitting on basis of space
def get_bot_reply(query, user):
    # split on basis of space ,only first space
    inital_word = query.split(' ', 1)

    # if #google keyword is in the query then calling google api
    if inital_word[0] == DISCORD_BOT_GOOGLE_KEYWORD:
        # here checking if there is word after the space or not
        if (len(inital_word) == 2):
            query_to_search = inital_word[1].strip()
            if (query_to_search):
                x = get_result_from_search(query_to_search)
                inser_to_db(query_to_search, user)
                return x

        return 'hey! there, Nothing to Search'
    if inital_word[0] == DISCORD_BOT_RECENT_KEYWORD:
        if (len(inital_word) == 2):
            x = search_from_db(inital_word[1], user)
            return x
    # replying in case of other query
    return 'HEY! PLEASE BE SAFE AND STAY AT HOME'
