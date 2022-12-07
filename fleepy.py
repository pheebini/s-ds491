import requests
def foo(url_dataframe):
    url_test = url_dataframe["URL"]
    ticker_test = url_dataframe["Ticker"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url_test, headers=headers)
    content = response.content.decode("utf-8")

    filename = f"/Users/phoebeliu/Documents/SDS_Senior_Project/YahooFinance_HTMLs/{ticker_test}.html"  # folder
    print(filename)
    with open(filename, 'w') as f:
        f.write(content)
