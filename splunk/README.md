# JIRA Alert Add-on

## Introduction

This add-on allows Splunk to create Jive Activity with External Objects using Simple Stream Integrations.

This add-on was produced as part of the
[Developer Guidance](http://dev.splunk.com/goto/alerting) project. Read our
guide to learn more about creating custom actions that can be performed when an
alert triggers.

## Installation

Before installing this app, you must install the corresponding Splunk + Jive Simple Stream Integration Add-On Your Jive Instance (and/or your own custom SSI handler).  

Once the app is installed (through [Splunkbase](https://splunkbase.splunk.com),
`Install app from file`, or by copying this directory to the etc/apps/ directory
of your Splunk installation), you are good to go.

To add a Jive action to an alert, go to the `Alerts` tab in the `Search` app and
find the alert for which you want to add Jive activity.  Click `Edit`, and select
`Edit Actions`. Click `+ Add Actions` and select Jive.  Specify the Jive Stream
Endpoint URL and then save.  Splunk will now start creating activity in your Jive instance.

## Case Study
For a case study showcasing the application of this custom alert action, see the [Splunk Reference App - PAS](https://github.com/splunk/splunk-ref-pas-code) and the accompanying [Splunk Developer Guidance](http://dev.splunk.com/goto/devguide)

## License
The Splunk Add-on for Jive Simple Stream Alerts is licensed under the Apache License 2.0. Details can be found in the [LICENSE page](http://www.apache.org/licenses/LICENSE-2.0).
