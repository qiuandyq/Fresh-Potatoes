import api_get as api


#test the search function
#prints True if the result is connected to the search word
def movie_search_test(search_word):
    search_results = api.search_movie_id(search_word)
    count = 0
    result_check = []
    for i in search_results['results']:
        if search_word in i['title']:
            result_check.append('True')
        else:
            result_check[count]('False')

    for i in result_check:
        if i != 'True':
            return "Error: One or more results did not match the search word"
    return "Passed: All results match the search word"
            
#test the search function
#prints True if the result is connected to the search word
def tv_search_test(search_word):
    search_results = api.search_tv_id(search_word)
    count = 0
    result_check = []
    for i in search_results['results']:
        if search_word in i['title']:
            result_check.append('True')
        else:
            result_check[count]('False')

    for i in result_check:
        if i != 'True':
            return "Error: One or more results did not match the search word"
    return "Passed: All results match the search word"


#Call the test functions
print(movie_search_test('Marvel'))
print(tv_search_test('Marvel'))
test_id = api.search_movie_id("Marvel")['results'][1]['id']
