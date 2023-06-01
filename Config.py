def Config():

    #You can add more if you want


    #todo:song player
    if "play song" in query.lower():
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

    #todo:open applications
    elif "open chrome" in query.lower():
        os.system(f"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #todo:open websites
    elif "open website" in query.lower():
        webbrowser.open(f'https://www.{query}.com')

    #todo:play videos
    elif "play video" in query.lower():
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

    #time
    elif "the time" in query:
        hour = datetime.datetime.now().strftime("%H")
        min = datetime.datetime.now().strftime("%M")
        toung(f"Sir time is {hour} bajke {min} minutes")

    #todo:some more features to add
    #weather
    #music player
    #animation
    #email writor
    #instagram
    #add more apps
    #add more sites

    '''***************  sky is the limit  *****************'''