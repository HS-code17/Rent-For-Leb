import requests

response = requests.get('https://www.lebaneselira.org/?ref=w3use.com')

if response:
    print('Request is successful')
else:
    print('Request returned an error.')

usd_to_lbp= '<td class="s30" dir="ltr">13,000</td>'

# Get the data first
def get_data():
    # add this to the end of the url
    # https://docs.google.com/spreadsheets/d/e/2PACX-1vQKxp7P4c5bbgJf403C4r51yQDeDljC6-ETLLBPYEXX9q64iGSRo0PpPEtY4W68qOYEmFTiEfVKDkz3/edit?output=csv&gid=$%7Bgid%7D
    # ?output=csv&gid=${gid}

    # extract the high number and other numbers

    # make sure it works and can be updated

    

# convert it to the right

