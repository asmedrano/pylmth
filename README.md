# Write python, render html
## Why?
* I get obsessed.
* Actually, I started this to ease testing some rather nasty templatetags in Django. Logic in our templates got a bit ridiculous so im hoping this will ease our pain a bit.

## Usage
```
from pylmth.dom import *

# all html elements (based on html5 spec) are represented similarly. 
# For Example lets use a div
d = Div()

# p tags are P, ul tags are Ul etc.
p = P()

# tags have methods to set inner_text and inner_html much like plain js.
p.inner_text = 'Hello World!'
p.inner_html = '<a href="#"> google.com</a>'

# append elements to others using append_child()
d.append_child(p)

# Dom element str reps give you the rendered tag.
print d
```
```
<div>
 <p>
  Hello World!
  <a href="#">
   google.com
  </a>
 </p>
</div>
```
```
# you can turn off pretty print
d.prettify = False # or when you create it d = Div(prettify=False)

# outputs <div><p><a href="#"> google.com</a></p></div>

# you can set html attributes like so
d.attr.id = 'wrapper'
d.attr.className = 'themainclass'

print d
```
```
<div id="wrapper" class="themainclass">
</div>
```

## Disclaimer
I dont know how much overhead this will add to rendering templates in something like Django. That's yet to be determined. Also, I based html tags and attributes off of the html5 spec and while i've automated some of it, adding attributes is tedious. That being said, not all element's attributes are complete.

