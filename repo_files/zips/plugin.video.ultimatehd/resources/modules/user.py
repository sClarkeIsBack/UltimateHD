import base64 as b
import xbmcaddon
id   = b.b64decode('cGx1Z2luLnZpZGVvLnVsdGltYXRlaGQ=')

name = b.b64decode('VWx0aW1hdGUgSEQ=')

port = b.b64decode('ODA=')

def host():
	if xbmcaddon.Addon().getSetting('direct') == 'true':
		url = b.b64decode('aHR0cDovL2FkczJtb3JlLmNvbQ==')
	else:
		url = b.b64decode('aHR0cDovL2xvYWQtYmFsYW5jZS5pbmZv')
	return url