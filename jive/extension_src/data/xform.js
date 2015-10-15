function transform(body, headers, options, callback)   {

/*
 * TO DO: Parse 'body' arg based on incoming event from 3rd party system.
 * TO DO: Replace the sample code below with your own transformation code.
 */

 /*** TEMPORARY WORKAROUND NEEDED FOR REFERENCING STRUCTURES IN body, headers, options RATHER THAN INDIVIDUALLY TRAVERSING EACH KEY ***/
 function clone(obj) {  if (null == obj || "object" != typeof obj) return obj;  var copy = {};  for (var attr in obj) {   copy[attr] = clone(obj[attr]);   }  return copy;  }
 body = clone(body);
 headers = clone(headers);
 options = clone(options);
 /*** END TEMPORARY WORK AROUND ****/

// Build activity object.
var activityInfo = { actor: {}, object:{}, jive:{} };

// Optional name of actor for this activity. Remove if n/a.
// activityInfo.actor.name = "Jane Doe";

// Optional email of actor for activity. Remove if n/a.
// activityInfo.actor.email = "janedoe@example.com";

// Optional URL for this activity. Remove if n/a.
activityInfo.object.url = body["results_link"];

// Required URL to the image for this activity.
activityInfo.object.image = "https://ryanrutan.ngrok.io/osapp/splunk-alerts/images/icon128.png";

// Required title of the activity.
activityInfo.object.title = body["owner"] + "@" + body["server_host"] + " - " + body["search_name"] + "[" + body["result"]["_indextime"] + "]";

// Optional HTML description of activity. Remove if n/a.
activityInfo.object.description = "Test"; //["+body["result"]["_raw"]+"]";

// Optional ... Removes the Go To Item Link in the Activity Stream Link (User will use the tile)
//activityInfo.object.hideGoToItem = true;

activityInfo.jive.app = {
  'appUUID': "fe922499-bda6-4aaf-8e47-6bf6c3e41f05",
  'view': "ext-object",
  'context': {
    'timestamp': new Date().toISOString(),
    'body': body,
    'headers': headers,
    'options': options
  }
}

/*
 * Call the callback function with our transformed activity information
 */

callback({ "activity" : activityInfo });

}
