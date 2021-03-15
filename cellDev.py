# -*- coding: utf-8 -*-

import time
import json
import requests


def checkCapacity(contents,knapsack_cap):
    """ contents is expected as a dictionaryof the form {item_id:(volume,value), ...} """
    """ This function returns True if the knapsack is within capacity; False if the knapsack is overloaded """
    load = 0
    if isinstance(contents,dict):
        for this_key in contents.keys():
            load = load + contents[this_key][0]
        if load <= knapsack_cap:
            return True
        else:
            return False
    else:
        print("function checkCapacity() requires a dictionary")

def knapsack_value(items):
    value = 0.0
    if isinstance(items,dict):
        for this_key in items.keys():
            value = value + items[this_key][1]
        return(value)
    else:
        print("function cell_tower_value() requires a dictionary")

def getData():
    search_url = 'https://jrbrad.people.wm.edu/deleteme/knapsack.json'
    response = requests.get(search_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
    x = response.json()
    
    '''
    f = open('knapsack.json','r')
    x = json.load(f)
    f.close()
    '''
    for i in range(len(x)):
        myData = x[i]['data']
        x[i]['data'] = {}
        for j in range(len(myData)):
            x[i]['data'][j] = tuple(myData[j])
    return x

def cell_algo(towers,budget):
    """ You write this function which is your heuristic knapsack algorithm
    
        You may indicate one or more items to put into the backpack within a list data structure
        by returning a list of values corresponding to the dictionary keys for the inserted items
    
        If you are finished loading the knapsack, then return any string value  """
        
    """ Compute existing load in knapsack """
    my_user_name = "no_name"   # replace string with your username
    my_nickname = 'nickname'   # if you chose, enter a nickname to appear instead of your username
    towers_to_pick = []        # use this list for the indices of the towers you select
    investment = 0.0           # use this variable, if you wish, to keep track of how much of the budget is already used
    tot_calls_added = 0.0      # use this variable, if you wish, to accumulate total calls added given towers that are selected
        
    ''' Start your code below this comment '''
    ids = list(towers.keys())
    towers_to_pick.append(ids[0])
    ''' Finish coding before this comment '''
    
    return my_user_name, towers_to_pick, my_nickname
        

""" Main code """
""" Get data and define problem ids """
probData = getData()
problems = range(len(probData))
silent_mode = False    # use this variable to turn on/off appropriate messaging depending on student or instructor use
""" Error Messages """
error_bad_list_key = """ 
A list was received from the cell_tower() function for the cell tower ID numbers to be selected.  However, that list contained an ID that was not a key in the dictionary of towers   This could be either because the element was non-numeric, it cell tower was already selected, or it was a numeric value that didn't match with any of the dictionary keys. 
"""
error_response_not_list = """
cell_tower() returned a response for towers to be selected that was not a list.  Scoring will be terminated   """

for problem_id in problems:
    in_knapsack = {}
    knapsack_cap = probData[problem_id]['cap']
    items = probData[problem_id]['data']
    errors = False
    response = None
    
    startTime = time.time()
    team_num, response, nickname = cell_algo(items,knapsack_cap)
    execTime = time.time() - startTime
    if isinstance(response,list):
        for this_key in response:
            if this_key in items.keys():
                in_knapsack[this_key] = items[this_key]
                del items[this_key]
            else:
                errors = True
                if silent_mode:
                    status = "bad_list_key"
                else:
                    print("P"+str(problem_id)+"bad_key_")
                #finished = True
    else:
        if silent_mode:
            status = "P"+str(problem_id)+"_not_list_"
        else:
            print(error_response_not_list)
                
    if errors == False:
        if silent_mode:
            status = "P"+str(problem_id)+"knap_load_"
        else:
            print("Cell towers selected for Problem ", str(problem_id)," ....", '    Execution time: ', execTime, ' seconds')
        knapsack_ok = checkCapacity(in_knapsack,knapsack_cap)
        knapsack_result = knapsack_value(in_knapsack)
        if silent_mode:
            print(status+"; Cell towers selected are within budget: "+knapsack_ok)
        else:
            print("Cell towers selected are within budget.")
            print("Cell tower objective function : ", knapsack_value(in_knapsack), '\n')