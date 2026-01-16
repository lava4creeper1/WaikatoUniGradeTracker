import requests

# Function to extract html from passed url
def getHTML(url):

    # try a get, catching invalid URLs
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        raise Exception(f"error reaching url {url}: Invalid URL")

    # check for status code not being 200 OK
    if r.status_code != 200:
        raise Exception(f"error reaching url {url}: response code <{r.status_code}>")
    
    # Split text on \r\n character
    html = (r.text).split(r"\r\n")

    # Remove first line of html (either DOCTYPE html or json header)
    html.pop(0)

    return html

if __name__ == "__main__":
    url = "https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29"

    # Get html of ENGEN101-24A as a default value for testing
    getHTML(url)