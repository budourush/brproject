from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from cgi import FieldStorage

# load html file
with open('index.html', mode='r', encoding="utf-8") as f:
    index = f.read()

with open('next.html', mode='r', encoding="utf-8") as f:
    next = f.read()

routes = []


def route(path, method):
    routes.append((path, method))


# add route setting
route('/', 'index')
route('/index', 'index')

# data
data = [
    ['それは人間のペットですか', 1, 2],
    ['それはニャーと鳴きますか', 'ネコ', 'イヌ'],
    ['それは食べるとおいしいですが', 'うし', 'ライオン']
]


class HelloServerHandler(BaseHTTPRequestHandler):
    # GET Method
    def do_GET(self):
        global routes
        a = 1
        print(type(a))
        _url = urlparse(self.path)
        for r in routes:
            if (r[0] == _url.path):
                eval('self.' + r[1] + '()')
                break
        else:
            self.error()

    # index action
    def index(self):
        self.send_response(200)
        self.end_headers()
        html = index.format(
            title='Animal',
            message='質問に答えてね',
            last=-1,
            animal='',
            yes=0,
            no=0
        )
        self.wfile.write(html.encode('UTF-8'))
        return

    # error action
    def error(self):
        global routes
        self.send_error(404, "CANNOT ACCESS!!")
        return

    # POST method
    def do_POST(self):
        _url = urlparse(self.path)
        if (_url.path == '/'):
            self.quiz()
        elif (_url.path == '/end'):
            self.end()
        return

    # quiz action
    def quiz(self):
        form = FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        try:
            answer = int(form['answer'].value)
            if (answer == -1):
                html = index.format(
                    title='Animal',
                    message='やったー',
                    last=-1,
                    animal='',
                    yes=0,
                    no=0
                )
            elif (answer == -2):
                html = index.format(
                    title='Animal',
                    message='うーん、答えを教えて',
                    last=form['last'].value,
                    animal=form['animal'].value
                )
            else:
                html = index.format(
                    title='Animal',
                    message=data[answer][0],
                    last=answer,
                    animal=form['answer'].value,
                    yes=data[answer][1],
                    no=data[answer][2],
                )
        except:
            html = index.format(
                title='Animal',
                message='それは、' + form['answer'].value + 'ですか。',
                last=form['last'].value,
                animal=form['answer'].value,
                yes=-1,
                no=-2,
            )
        self.send_response(200)
        self.end_headers()
        self.wfile.write(html.encode('UTF-8'))
        return

    # end action
    def end(self):
        form = FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        animalname = form['animalname'].value
        question = form['question'].value
        last = int(form['last'].value)
        animal = form['animal'].value
        newdata = form['newdata'].value
        n = len(data)
        if (data[last][1] == animal):
            data[last][1] = n
        elif (data[last][2] == animal):
            data[last][2] = n

        data.append(newdata)

        html = index.format(
            title='Animal',
            message='なるほどわかりました',
            last=-1,
            animal='',
            yes=0,
            no=0,
        )
        self.send_response(200)
        self.end_headers()
        self.wfile.write(html.encode('UTF-8'))
        return

    # next action
    def next(self):
        _url = urlparse(self.path)
        query = parse_qs(_url.query)
        id = query['id'][0]
        password = query['pass'][0]
        msg = 'id=' + id + ', password=' + password
        self.send_response(200)
        self.end_headers()
        # html = next.format(
        #     message=msg,
        #     data=query
        # )
        html = next.format(
            message='header data.',
            data=self.headers
        )
        self.wfile.write(html.encode('UTF-8'))
        return

    def xml(self):
        xml = '''<?xml version="1.0" encoding="Shift_JIS"?>
        <data>
            <person>
                <name>Taro</name>
                <mail>taro@yamada.com</mail>
                <age>39</age>
            </person>
            <massage>Hello Python</massage>
        </data>
        '''
        self.send_response(200)
        self.send_header('Content-Type', 'application/xml; charset=Shift_JIS')
        self.end_headers()
        self.wfile.write(xml.encode('UTF-8'))


server = HTTPServer(('', 8000), HelloServerHandler)
server.serve_forever()
