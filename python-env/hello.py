from flask import Flask
from docker import Client
from flask.ext.script import Manager

app = Flask(__name__)

# manager allows for threaded option
manager = Manager(app)

@app.route('/<input>')
def process(input):

    # defines where python looks for the docker server
    cli = Client(base_url='unix://var/run/docker.sock')

    # launching a new gap container and giving it the environment varible <input>
    container = cli.create_container(image='rwlaub/gap', environment=["ARRAY=" + input])
    cli.start(container['Id'])

    # waiting for gap to finish calculation
    cli.wait(container['Id'])

    # reading gap output from logs
    output = cli.logs(container['Id'], tail=1)

    # cleanup and output
    cli.remove_container(container['Id'])
    return output

if __name__ == '__main__':
    manager.run()
