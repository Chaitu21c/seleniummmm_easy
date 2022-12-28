import configparser


def read_date(section,keys):
    data=configparser.ConfigParser()
    data.read("..\CONFIG\config.cfg")
    data.get(section,keys)
    return data.get(section,keys)


