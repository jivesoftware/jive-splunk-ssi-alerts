import sys
import json
import requests

# creates outbound message from alert payload contents
# and attempts to send to the specified endpoint
def send_message(payload):
    config = payload.get('configuration')

    # Get the Tile Endpoint URL
    jive_url = config.get('jive_url')

    # create outbound JSON message body
    body = json.dumps({
       "app"    :   payload.get("app"),
       "owner"  :   payload.get("owner"),
       "results_file"   :   payload.get("results_file"),
       "results_link"   :   payload.get("results_link"),
       "server_host"    :   payload.get("server_host"),
       "server_uri"     :   payload.get("server_uri"),
       "session_key"    :   payload.get("session_key"),
       "sid"    :   payload.get("sid"),
       "search_name"    :   payload.get("search_name"),
       "result" :   payload.get("result"),
    })

    # create outbound request object
    try:
        headers = {"Content-Type": "application/json"}
        result = requests.post(url=jive_url, data=body, headers=headers)
        #TODO:  CHANGE THIS TO result.statuscode or result.code
        print >>sys.stderr, "INFO Jive HTTP Response [%s] - [%s]" % (result.text, result.text)
    except Exception, e:
        print >> sys.stderr, "ERROR Error sending message: %s" % e
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        try:
            # retrieving message payload from splunk
            raw_payload = sys.stdin.read()
            payload = json.loads(raw_payload)
            send_message(payload)
        except Exception, e:
            print >> sys.stderr, "ERROR Unexpected error: %s" % e
            sys.exit(3)
    else:
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
        sys.exit(1)
