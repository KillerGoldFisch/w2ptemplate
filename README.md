# w2ptemplate

This Package is based on the Template Engine from the Web2Py free open source full-stack framework for rapid development of fast, scalable, secure and portable database-driven web-based applications.

It is written and programmable in Python. LGPLv3 License

Learn more at http://web2py.com or https://github.com/web2py/web2py

## Usage

```python
>>>from w2ptemplate import render
>>> render()
'hello world'
>>> render(content='abc')
'abc'
>>> render(content='abc\'')
"abc'"
>>> render(content='a"\'bc')
'a"\\'bc'
>>> render(content='a\\nbc')
'a\\nbc'
>>> render(content='a"bcd"e')
'a"bcd"e'
>>> render(content="'''a\\nc'''")
"'''a\\nc'''"
>>> render(content="'''a\\'c'''")
"'''a\'c'''"
>>> render(content='{{for i in range(a):}}{{=i}}<br />{{pass}}', context=dict(a=5))
'0<br />1<br />2<br />3<br />4<br />'
>>> render(content='{%for i in range(a):%}{%=i%}<br />{%pass%}', context=dict(a=5),delimiters=('{%','%}'))
'0<br />1<br />2<br />3<br />4<br />'
>>> render(content="{{='''hello\\nworld'''}}")
'hello\\nworld'
>>> render(content='{{for i in range(3):\\n=i\\npass}}')
'012'
```

For the Syntax inside the template please read the "Basic-syntax"-Section here: http://web2py.com/books/default/chapter/29/05/the-views#Basic-syntax

## The `render`-function

```python
def render(content="hello world",
           stream=None,
           filename=None,
           path=None,
           context={},
           lexers={},
           delimiters=('{{', '}}'),
           writer='response.write'
           ):
```

## Installation

using pip
```
pip install w2ptemplate
```
or manually
```
git clone https://github.com/KillerGoldFisch/w2ptemplate
cd w2ptemplate
python setup.py install
```
