from flask import Flask

app = Flask(__name__)

def add_tag(tag: str):
    def decorator(func):
        def wrapper():
            return f'<{tag}>{func()}</{tag}>'
        return wrapper
    return decorator


@app.route("/")
def hello_world():
    return """<iframe src="https://giphy.com/embed/mlvseq9yvZhba" 
                    width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen>
              </iframe>"""
    # return "<h1 style='text-align: center'>Hello, World!</h1>"

@app.route("/bye")
@add_tag('em')
@add_tag('b')
@add_tag('u')
def say_bye():
    return 'Good bye'

@app.route("/username/<string:name>/<int:age>")
def greet(name, age):
    return f"Hello there {name}, you are {age} years old!"


if __name__ == '__main__':
    # app.run()
    # app.run(host="0.0.0.0", port=5100)
    app.run(debug=True)
