# Plugins specializations with common methods useful for their own type

class DiscoveryPluginMixin:
    def queue_url(self, url):
	if not parse_url(url).isbllist:
	    BasePlugin.queue_url(self, url)
	    return True
	return False



