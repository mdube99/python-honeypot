from configparser import ConfigParser

# TODO: rename option

def getOptions(category, option):
    options = ConfigParser()
    options.read('options.ini')
    wantedData = options.get(category, option)
    return wantedData 
