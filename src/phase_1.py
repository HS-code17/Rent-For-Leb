import urllib.request
def validate_url(base_url):
    try:
        code_1= urllib.request.urlopen(base_url).getcode()
        print(code_1)
        return code_1
    except Exception as e:
        print(e)

# if __name__=="__main__":
#     validate_url("https://stackoverflow.com/")