from flask import Flask
from docker import Client
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/<input>')
def process(input):
    cli = Client(base_url='unix://var/run/docker.sock')
    container = cli.create_container(image='rwlaub/gap', environment=["ARRAY=" + input])
    cli.start(container['Id'])
    cli.wait(container['Id'])
    output = cli.logs(container['Id'], tail=1)
    cli.remove_container(container['Id'])
    return output

if __name__ == '__main__':
    manager.run()
