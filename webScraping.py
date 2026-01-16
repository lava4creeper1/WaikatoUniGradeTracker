import requests

def getHTML(url):
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        raise Exception(f"error reaching url {url}: Invalid URL")

    if r.status_code != 200:
        raise Exception(f"error reaching url {url}: response code <{r.status_code}>")
    
    html = (r.text).split(r"\r\n")
    html.pop(0)

    return html

if __name__ == "__main__":
    url = "https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29"

    getHTML(url)