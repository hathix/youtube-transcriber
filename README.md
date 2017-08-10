# YouTube Transcriber

Need to transcribe a YouTube video? Turns out that YouTube already makes pretty good automated captions. With this script, you can grab those captions - so that you've effectively automatically transcribed the YouTube video!


## Getting started

First, fire up the Jupyter notebook.

Next you need to get the URL of a `timedtext` file from your YouTube video. This file basically  Go to the YouTube URL, open your Developer Console, go to the Network Tab, refresh the page. Then toggle on the closed captions. Wait for a bit then filter for `timedtext` in the dev tools search bar. Copy and paste the URL you see there.

![demonstration](img/timedtext-network-tab.png)

## Example

Consider [this example video](https://www.youtube.com/watch?v=0Ydp6bR5HXw). Its `timedtext` looks like:

```xml
<timedtext format="3">
    <body>
    <p t="2810" d="7450">
When you grow up you, tend to get told that the world is the way it is and your life is
</p>
    <p t="10260" d="5299">
just to live your life inside the world, try not to bash into the walls too much, try to
</p>
    <p t="15559" d="6351">have a nice family, have fun, save a little money.</p>
    <p t="21910" d="3199">That’s a very limited life.</p>
    <p t="25109" d="4711">
Life can be much broader, once you discover one simple fact, and that is that everything
</p>
    <p t="29820" d="6460">
around you that you call life was made up by people that were no smarter than you.
</p>
    <p t="36280" d="5110">
And you can change it, you can influence it, you can build your own things that other people
</p>
    <p t="41390" d="1610">can use.</p>
    <p t="43000" d="4270">
And the minute that you understand that you can poke life and actually something will,
</p>
    <p t="47270" d="4241">
you know if you push in, something will pop out the other side, that you can change it,
</p>
    <p t="51511" d="1999">you can mold it.</p>
    <p t="53510" d="2880">That’s maybe the most important thing.</p>
    <p t="56390" d="9350">
It’s to shake off this erroneous notion that life is there and you’re just gonna
</p>
    <p t="65740" d="7239">
live in it, versus embrace it, change it, improve it, make your mark upon it.
</p>
    <p t="72979" d="5390">
I think that’s very important and however you learn that, once you learn it, you’ll
</p>
    <p t="78369" d="5591">
want to change life and make it better, cause it’s kind of messed up, in a lot of ways.
</p>
    <p t="83960" d="1819">
Once you learn that, you’ll never be the same again.”
</p>
    </body>
</timedtext>
```

## TODOs

This doesn't currently work with [this video](https://www.youtube.com/watch?v=0Ydp6bR5HXw) b/c the format is different:

```xml
<timedtext format="3">
<body>
<p t="2810" d="7450">
When you grow up you, tend to get told that the world is the way it is and your life is
</p>
<p t="10260" d="5299">
just to live your life inside the world, try not to bash into the walls too much, try to
</p>
<p t="15559" d="6351">have a nice family, have fun, save a little money.</p>
<p t="21910" d="3199">That’s a very limited life.</p>
<p t="25109" d="4711">
Life can be much broader, once you discover one simple fact, and that is that everything
</p>
<p t="29820" d="6460">
around you that you call life was made up by people that were no smarter than you.
</p>
<p t="36280" d="5110">
And you can change it, you can influence it, you can build your own things that other people
</p>
<p t="41390" d="1610">can use.</p>
<p t="43000" d="4270">
And the minute that you understand that you can poke life and actually something will,
</p>
<p t="47270" d="4241">
```
