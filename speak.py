import webbrowser

def open_url(url):
    """
    Open the specified URL in the default web browser.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    webbrowser.open(url)