
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file, f_items, f_users, f_bids, f_categories):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        formatted_items = []
        formatted_users = []
        formatted_bids = []
        formatted_categories = []
        count = 0
        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            # ITEMS
            buy_price = item['Buy_Price'] if 'Buy_Price' in item else 'NULL'
            description = '"{0}"'.format(item['Description'].strip().replace('\"', '\"\"')) if item['Description'] else 'NULL'
            item_attributes = [
                item['ItemID'],
                item['Seller']['UserID'],
                '"{0}"'.format(item['Name'].strip().replace('\"', '\"\"')),
                transformDollar(item['Currently']),
                buy_price,
                transformDttm(item['Started']),
                transformDttm(item['Ends']),
                transformDollar(item['First_Bid']),
                item['Number_of_Bids'],
                description
            ]
            formatted_items.append("|".join(item_attributes))

            # USERS
            user_attributes = [
                item['Seller']['UserID'],
                item['Seller']['Rating'],
                item['Location'],
                item['Country']
            ]
            formatted_users.append("|".join(user_attributes))

            # BIDS
            if item['Bids']:
                for bid in item['Bids']:
                    # print(bid)
                    bids_attributes = [
                        bid['Bid']['Bidder']['UserID'],
                        item['ItemID'],
                        transformDttm(bid['Bid']['Time']),
                        transformDollar(bid['Bid']['Amount'])
                    ]
                    formatted_bids.append("|".join(bids_attributes))


            # CATEGORIES
            if item['Category']:
                for category in item['Category']:
                    category_attributes = [
                        category,
                        item['ItemID']
                    ]
                    formatted_categories.append("|".join(category_attributes))

        f_items.write("\n".join(formatted_items))
        f_users.write("\n".join(formatted_users))
        f_bids.write("\n".join(formatted_bids))
        f_categories.write("\n".join(formatted_categories))



"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)

    # open files
    f_items = open("item.dat","w")
    f_users = open("users.dat","w")
    f_bids = open("bids.dat","w")
    f_categories = open("categories.dat","w")

    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f,f_items, f_users, f_bids, f_categories)
            # print "Success parsing " + f

    f_items.close()
    f_users.close()
    f_bids.close()
    f_categories.close()


if __name__ == '__main__':
    main(sys.argv)
