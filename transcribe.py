import urllib2
import xml.etree.ElementTree as ET


def get_transcript(timedtext_url):
    # grab the XML file at that URL
    handle = urllib2.urlopen(timedtext_url)
    contents = handle.read()

    # parse XML
    root = ET.fromstring(contents)
    # root = tree.getroot()

    running_words = []
    body = root.find("body")
    for p in body.findall("p"):
        if p.text is None or p.text == "\n":
            # nothing here, go to the <s> inside
            words = [clean_text(s.text) for s in p.findall("s")]
        else:
            # p.text is an actual word/string!
            words = [clean_text(p.text)]
        running_words.extend(words)

    final_text = " ".join(running_words)

    return final_text


def clean_text(text):
    return text.strip().replace("\n", " ")
