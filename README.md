# TimedText Parser

Parse text out of YouTube's auto-generated captions. A great way of transcribing YouTube videos automatically.

*Note: this only works with some videos. Under development.*

## Getting started

First, fire up the Jupyter notebook.

Next you need to get a TimedText URL from your YouTube video. Go to the YouTube URL, open your Developer Console, go to the Network Tab, refresh the page. Then toggle on the closed captions. Wait for a bit then filter for `timedtext` in the dev tools search bar. Copy and paste the URL you see there.

![demonstration](img/timedtext-network-tab.png)
