import eel
import datetime as dt
import json
import subprocess
eel.init('web')

@eel.expose
def getTime():
    now = str(dt.datetime.now())
    #return json.dumps({'now':now})
    return now
#eel.js_random()(print)

def testThread():
    #below should be replaced by an electron app call if necessary.
    #maybe have a json file and regular checks from the javascript side to update values.
    subprocess.call(['touch','other.html'])

eel.spawn(testThread)
eel.start('main.html')
random_number_from_javascript=eel.js_random()()
print(random_number_from_javascript)
eel.say_hello_js('javascript')
