from chalice import Chalice
import random
import boto3

app = Chalice(app_name='FavUncleJokes')
dynamo = boto3.resource("dynamodb")
dynamo.Table("favunclejokes_myfirstjokes")
my_first_table = dynamo.Table("favunclejokes_myfirstjokes")
jokes = []
for joke in my_first_table.scan()["Items"]:
    jokes.append(joke["text"])


@app.route('/')
def uncle_jokes():
    index = random.randint(0, len(jokes) - 1)
    return jokes[index]


@app.route('/{key_word}')
def find_jokes(key_word):
    for joke in jokes:
        if key_word.lower() in joke.lower():
            return joke
    else:
        return "No jokes with this word. Wanna add one?"


# The view function above will return a random joke
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
