from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import pyshorteners
def Start():
    put_text('تطبيق اختصار روابط').style('text-align:center; font-size:20px; color:green;')
    put_html('<center><img src="http://cu-t.link/content/auto_site_logo.png"></center>')
    put_html('<hr>')
    name=input('اختصار الروابط',
            type='text',
            placeholder='ادخل رابط الذي تريد اختصاره',
            help_text='url with : https / http'
    )
    def Short():
        sh=pyshorteners.Shortener()
        put_text(sh.tinyurl.short(name)).style('float:right; margin-right:300px; font-size:20px;')
    put_button('اختصار الرابط الان' , onclick=Short).style('float:right; margin-right:350px;')
    
start_server(Start,port=3335,debug=True)