import os,xbmc,xbmcgui,downloader,user,tools

fanart       = xbmc.translatePath(os.path.join('special://home/addons/' + user.id , 'fanart.jpg'))

def get():
	r = tools.OPEN_URL('https://archive.org/download/samemilyonline_gmail_Apps/apps.xml')
	all = tools.regex_get_all(r,'<apk>','</apk>')
	for a in all:
		name = tools.regex_from_to(a,'<title>','</title>')
		url  = tools.regex_from_to(a,'<url>','</url>')
		icon = tools.regex_from_to(a,'<icon>','</icon>')
		if icon == "":
			icon = xbmc.translatePath(os.path.join('special://home/addons/' + user.id, 'icon.png'))
		tools.addDir(name,url,18,icon,fanart,'')

def install(name,url):
	if xbmc.getCondVisibility('system.platform.android'):
		path = xbmc.translatePath(os.path.join('/storage/emulated/0/Download',''))
		dp = xbmcgui.DialogProgress()
		dp.create(user.name,"","",'Downloading:' + name)
		lib=os.path.join(path, 'app.apk')
		downloader.download(url, lib, dp)
		xbmcgui.Dialog().ok(user.name, "[COLOR white]Launching the installer[/COLOR]" , "[COLOR white]You will now be asked to install[/COLOR] [B][COLOR lime]%s[/COLOR][/B]"%name)
		xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + lib + '")' )
	else:
		xbmcgui.Dialog().ok("[COLOR white]Non Android Device[/COLOR]" ,"[COLOR white]This App Installer is only compatible with Android Devices[/COLOR]"," ")