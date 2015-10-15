import splunk
import splunk.admin as admin
from jive_helpers import *

class JiveAlertsInstallHandler(admin.MConfigHandler):
    def __init__(self, *args):
        admin.MConfigHandler.__init__(self, *args)
        self.shouldAutoList = False

    def setup(self):
        self.supportedArgs.addOptArg('*')

    def handleList(self, confInfo):
        jive_settings = get_jive_settings(splunk.getLocalServerInfo(), self.getSessionKey())
        item = confInfo['jive']
        item['jive_url'] = jive_settings.get('jive_url', 'https://xxxx.jiveon.com/')

    def handleEdit(self, confInfo):
        if self.callerArgs.id == 'jive':
            jive_settings = get_jive_settings(splunk.getLocalServerInfo(), self.getSessionKey())
            if 'jive_url' in self.callerArgs:
                jive_settings['jive_url'] = self.callerArgs['jive_url'][0]
            update_jive_settings(jive_settings, splunk.getLocalServerInfo(), self.getSessionKey())

admin.init(JiveAlertsInstallHandler, admin.CONTEXT_APP_ONLY)
