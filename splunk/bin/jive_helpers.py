import sys
import requests
import json

def splunkd_auth_header(session_key):
    return {'Authorization': 'Splunk ' + session_key}

def get_jive_settings(server_uri, session_key):
    result = dict()
    for k,v in get_jive_action_config(server_uri, session_key).items():
        if k.startswith('param.'):
            result[k[len('param.'):]] = v
    return result

def update_jive_settings(jive_settings, server_uri, session_key):
    r = requests.post(
        url=server_uri+'/servicesNS/nobody/jive-splunk-ssi-alerts/alerts/alert_actions/jive?output_mode=json',
        data={
            'param.jive_url': jive_settings.get('jive_url'),
        },
        headers=splunkd_auth_header(session_key),
        verify=False).json()

def get_jive_action_config(server_uri, session_key):
    url = server_uri + '/servicesNS/nobody/jive-splunk-ssi-alerts/alerts/alert_actions/jive?output_mode=json'
    result = requests.get(url=url, headers=splunkd_auth_header(session_key), verify=False)
    return json.loads(result.text)['entry'][0]['content']

def update_jive_dialog(content, server_uri, session_key):
    uri = server_uri + '/servicesNS/nobody/jive-splunk-ssi-alerts/data/ui/alerts/jive'
    requests.post(url=uri, data={'eai:data': content}, headers=splunkd_auth_header(session_key), verify=False)
