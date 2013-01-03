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
You can turn off pretty print
```
d.prettify = False # or when you create it d = Div(prettify=False)

# outputs <div><p><a href="#"> google.com</a></p></div>
```
You can set html attributes like so
```
d.attr.id = 'wrapper'
d.attr.className = 'themainclass'
```
Result
```
<div id="wrapper" class="themainclass">
</div>
```
You can set custom attributes to dom elements.

``` 
d = Div()
d.add_attr('data-foo')
# its now accessible as an attribute via some magics
d.attr.data_foo = 'bar'
print d
# outuputs
<div data-foo="bar">
</div>
```
Some elements have helper methods built in.
```
ul = Ul()
for i in ['hi', 'there']:
    ul.add_li(inner_text=i) # this is the helper
#outputs
<ul>
   <li>
    hi
   </li>
   <li>
    there
   </li>
</ul>
```

```
tbl = Table()
thead = tbl.add_header()
row = thead.add_row()
row.add_col(inner_text='Beans', colspan='2')
row.add_col(inner_text='Rice')
tbody = tbl.add_body()
tr = tbody.add_row()
tr.add_col(inner_text='pinto', className='foo')
tr.add_col(inner_text='jasmine', className='foo')
```
Outputs
```
<table>
    <thead>
      <tr>
        <th colspan="2">Beans</th>

        <th>Rice</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td class="foo">pinto</td>

        <td class="foo">jasmine</td>
      </tr>
    </tbody>
  </table>
```


## Disclaimer
I based html tags and attributes off of the html5 spec and while I've automated some of it, adding attributes is tedious.
All tags have GLOBAL ATTRIBUTES applied http://www.w3.org/html/wiki/Attributes/_Global
That being said, not all element's attributes are complete.

