from flask import Flask
from docker import Client
app = Flask(__name__)

@app.route('/<input>')
def process(input):
    cli = Client(base_url='unix://var/run/docker.sock')
    container = cli.create_container(image='gap', environment=["ARRAY=" + input])
    cli.start(container['Id'])
    cli.wait(container['Id'])
    output = cli.logs(container['Id'], tail=1)
    cli.remove_container(container['Id'])
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
