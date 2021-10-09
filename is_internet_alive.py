import requests

# Web page (non-SSL) to get
url = "https://www.google.hr"
response = None
net = False

# Perform HTTP GET request on a non-SSL web
try:
    response = requests.get(url)
    net = True
    # Display the contents of the page
    #print(response.text)
except:
    pass

if net == True:
    print("Internet ok")
else:
    print("No internet")