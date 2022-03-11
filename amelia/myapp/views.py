from ast import Index
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.

holos = [
    {'id':1, 'idol': 'Amelia Watson', 'body':'Ame Is...,', 'img':'https://walfiegif.files.wordpress.com/2022/01/out-transparent-2.gif?w=340&h=415&zoom=2', 'color':'gold'},
    {'id':2, 'idol': 'Takanasi Kiara', 'body':'Kiara Is...', 'img':'https://walfiegif.files.wordpress.com/2021/07/out-transparent-2.gif?w=340&h=395&zoom=2', 'color':'orange'},
    {'id':3, 'idol': 'Gawr Gura', 'body':'Gura Is...','img':'https://walfiegif.files.wordpress.com/2020/12/out-transparent-4.gif?w=560&h=9999', 'color':'skyblue'},
    {'id':4, 'idol': 'Mori Kalliope', 'body':'kalli Is...','img':'https://walfiegif.files.wordpress.com/2021/05/out-transparent-16.gif?w=560&h=9999', 'color':'pink'},
]


def main_home(articletag, id=None):
    global holos
    ol = ''
    contentUI= ''
    if id != None:
        contentUI = '''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value="{id}">
                    <input type="submit" value="delete">
                </form>
            </li>
        '''
    for holo in holos:
        ol +=f'<li><a href="/read/{holo["id"]}/">{holo["idol"]}</a></li>'

    templates = f'''
    <!DOCTYPE html>
    <html lang="ko">
    <body style="font-size: 20px;">
        <h1><a style="text-decoration-line: none; "href="/">Welcome HoloLive</a></h1>
        <ul style="font-size: 40px; margin-left: 20px;">
            {ol}
        </ul>
        <h1>menu</h1>
        <ul style="font-size: 40px; margin-left: 20px; list-style: none;">
            <li><a href="/create">create</a></li>
            {contentUI}
        </ul>
        {articletag}
    </body>
    </html>
    '''
    return HttpResponse(templates)

def hololive_En(name, color, img, body):
    article = f'''
    <h1 style="margin-top: 20px; color:{color}; text-align:center">{name} World!!</h1>
    <div style="width:100%; text-align:center;">
        <img style="width: 10%;"src="{img}">
    </div>
    <h2 style="margin-top: 20px; color:{color}; text-align:center">{body}</h2>
    '''
    return article

def index(request):
    article = f'''
        <h1>Welcom</h1>
        I'm yours
    '''
    return main_home(article)

def read(request, id):
    global holos
    article = f''
    for holo in holos:
        if int(id) == int(holo["id"]):
            article = hololive_En(holo["idol"], holo["color"], holo["img"], holo["body"])
    return main_home(article, id)

@csrf_exempt
def create(request):
    # request
    # print('request.method', request.method)
    if request.method == 'GET':
        article = f'''
            <form action="/create/" method="post">
                <p><input type="text" name="idol" placeholder="title"></p>
                <p><input type="text" name="img" placeholder="img_link"></p>
                <div>
                    <input type="color" name="color" id="color" value="#87CEEB">
                    <label style="cursor:pointer;" for="color">holos color</label>
                </div>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(main_home(article))
    
    elif request.method == 'POST':
        idol = request.POST['idol']
        body = request.POST['body']
        img = request.POST['img']
        color = request.POST['color']
        try:
            id = holos[-1]["id"]+1
        except IndexError:
            id = 0

        newTopic = {"id": id, 'idol':idol, 'body':body, 'img':img, 'color':color}
        holos.append(newTopic)
        
        print(request.POST)
        url = f'/read/{id}'
        return redirect(url)
    
    
@csrf_exempt
def delete(request):
    global holos
    if request.method == 'POST':
        id = request.POST['id']

        for holo in holos:
            if holo['id'] == int(id):
                print(holo)
                holos.remove(holo)
        print('id', id)
        return redirect('/')