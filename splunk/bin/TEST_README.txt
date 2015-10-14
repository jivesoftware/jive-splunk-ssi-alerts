Prerequisites:
    * The jive_alerts add-on has been installed to $SPLUNK_HOME/etc/apps

I. Ad-hoc Search Language Invocation
    In a SplunkWeb Search Dashboard, enter the following:
        | sendalert jive param.jive_url="SET_JIVE_TILE_URL"

    Expected Result:
        A new Jive Activity entry will have been created in the specified Jive instance and place related to the Tile URL.
