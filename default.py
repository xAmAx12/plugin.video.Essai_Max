import xbmcaddon, util

addon = xbmcaddon.Addon('plugin.video.Essai_Max')

util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 
               'http://78.129.30.42:8001/1:0:1:1C7:26AC:13F:820000:0:0:0:')

