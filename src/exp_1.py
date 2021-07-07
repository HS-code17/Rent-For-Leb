import urllib.request
# is this site available?
# as well as gives out some metadata that are specific
# to the site itself.
# maybe take input from command line
# import sys
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# in the future add a robots txt check up
# we could have multiple urls;
# so maybe create a little choice thing
def validate_url():
    code_1 = ""
    user_tries = []
    while code_1 != "200":
        user_input = input("Enter url: ")
        print("Url entered is:",user_input)
        user_tries.append(user_input)
        if len(user_tries)<5:
            print("Number of trials:", len(user_tries))
            number_of_tries = 5 - int(len(user_tries))
            print("Number of trials left:",number_of_tries )
            try:
                code_1= urllib.request.urlopen(user_input).getcode()
                url_success = user_input
                url_success_code = str(code_1)
                print("This site is functional. Code:",url_success_code,"Succesful url is: ", url_success)
                break
            except:
                print("This site is not working")
        else:
            print("You exceeded your number of trials")
            break    
    # print("This site is functional. Code:",code_1)
    try:
        return url_success,url_success_code
    except:
        print("All the urls you entered are invalid:", user_tries)