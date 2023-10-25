__author__ = "Rainer Schmitz <rainer.ch.franz@gmail.com>"
__copyright__ = "Rainer Schmitz <rainer.ch.franz@gmail.com>"
__version__ = "1.0.0"


import datetime
import configparser

import win32api
import win32clipboard

import terminaltables



def generate_docToDO():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Annahme: Die config-Datei existiert und hat einen Abschnitt namens [Counter]
    projektid = config.get('PerSet', 'projektid')
    developerid = config.get('PerSet', 'developerid')
    counter = config.getint('ToDOs', 'counter')
    counter += 1
    doctype = config.get('ToDOs', 'doctype')

    config.set('ToDOs', 'counter', str(counter))

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    timestamp = datetime.datetime.now().strftime('%Y%m%d-') + str(counter).zfill(5)
    respond = doctype + " " + projektid + "-" + timestamp + developerid

    return respond


def generate_docBugDoc():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Annahme: Die config-Datei existiert und hat einen Abschnitt namens [Counter]
    projektid = config.get('PerSet', 'projektid')
    developerid = config.get('PerSet', 'developerid')
    counter = config.getint('BugDoc', 'counter')
    counter += 1
    doctype = config.get('BugDoc', 'doctype')

    config.set('BugDoc', 'counter', str(counter))

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    timestamp = datetime.datetime.now().strftime('%Y%m%d-') + str(counter).zfill(5)
    respond = doctype + " " + projektid + "-" + timestamp + developerid

    return respond


def generate_docCOM():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Annahme: Die config-Datei existiert und hat einen Abschnitt namens [Counter]
    projektid = config.get('PerSet', 'projektid')
    developerid = config.get('PerSet', 'developerid')
    counter = config.getint('DocCOM', 'counter')
    counter += 1
    doctype = config.get('DocCOM', 'doctype')

    config.set('DocCOM', 'counter', str(counter))

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    timestamp = datetime.datetime.now().strftime('%Y%m%d-') + str(counter).zfill(5)
    respond = doctype + " " + projektid + "-" + timestamp + developerid

    return respond





flag = "1"
while flag != "0":

    flag = input("Was für ein Comment?: ")
    if flag == "TD":
        doctype = generate_docToDO()
        doctype_toSTR = (str(doctype))

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(doctype_toSTR)
        win32clipboard.CloseClipboard()

        print(f'{doctype_toSTR} |  ToDO: Comment Generiert und in die Zwischenablage Kopiert!')
    elif flag == "BD":
        doctype = generate_docBugDoc()
        doctype_toSTR = (str(doctype))

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(doctype_toSTR)
        win32clipboard.CloseClipboard()

        print(f'{doctype_toSTR} |  BugDoc: Comment Generiert und in die Zwischenablage Kopiert!')

    elif flag == "DC":
        doctype = generate_docCOM()
        doctype_toSTR = (str(doctype))

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(doctype_toSTR)
        win32clipboard.CloseClipboard()

        print(f'{doctype_toSTR} |  DocCOM: Comment Generiert und in die Zwischenablage Kopiert!')

    elif flag == "-h":
        print('Usage: set the counter and IDs over the config.ini')
        print('exit = 0')
        data = [["Arg", "Gen, projektid-Date-counter-developerid"],
                ["TD", "# ToDo: 037-231023-000001-7001"],
                ["BD", "# BugDoc: 037-231023-000004-7001"],
                ["DC", "# DocCOM: 037-231023-000005-7001"]]

        table = terminaltables.AsciiTable(data)
        print(table.table, '\n')

    else:
        data = [["Arg", "Gen, projektid-Date-counter-developerid"],
                ["TD", "# ToDo: 037-231023-000001-7001"],
                ["BD", "# BugDoc: 037-231023-000004-7001"],
                ["DC", "# DocCOM: 037-231023-000005-7001"]]

        table = terminaltables.AsciiTable(data)
        table = terminaltables.AsciiTable(data, title="Doctype not found!")

        print(table.table, '\n')


