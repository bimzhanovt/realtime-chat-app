# Real-Time Chat Application
This is a simple chat application that allows users to chat with each other in real-time.
The application is built using Flask-SocketIO, a Flask extension that adds support for WebSockets, and SQLite.

## Usage
Clone this repository and run following commands:

```
$ python3 -m venv venv          # Creates a virtual environment
$ source venv/bin/activate      # Activates the virtual environment
$ pip install -e .              # Installs the dependencies
$ python sqlite.py              # Initializes the database
$ flask --app realtime-chat run # Runs the application
```

## License
This project is licensed under the GNU General Public License v3.0.
See the LICENSE file for details.
