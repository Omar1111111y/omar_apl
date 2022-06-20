from flask import *
print('<br>Omarrrrr')
m_my = Flask(__name__)
bb= [{"name":"clear","id":10027,"pp":"Omar====="}]

@m_my.route('/')
def ih():
        return jsonify(bb)
m_my.run()

