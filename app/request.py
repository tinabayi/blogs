

import urllib.request,json
from .models import Quote

# Quote = quote.Quote

base_url= None
def configure_request(app):
# Getting QUOTE_API_BASE_URL
   base_url = app.config['QUOTE_BASE_URL']





def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
   
    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

    #     if get_quote_response[]:
    #         quote_results_list = get_quote_response[]
    #         quote_results = process_results(quote_results_list)


    # return quote_results

    # def process_results(quote_list):
    # '''
    # Function  that processes the quote result and transform them to a list of Objects

    # Args:
    #     movie_list: A list of dictionaries that contain quote details

    # Returns :
    #     movie_results: A list of quote objects
    # '''
    # quote_results = []
    # for quote_item in quote_list:
        author=quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        permalink= quote_item.get('permalink')
       
        if id:
            quote_object = Quote(author,id,quote,permalink)
            # quote_results.append(quote_object)

    return quote_object