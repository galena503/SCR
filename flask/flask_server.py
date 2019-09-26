from flask import Flask, jsonify, request, render_template
from ability.twitter_api.sq_twitter_DB import Sq_tw
from ability.twitter_api.g_user_lookup_class import G_tw_user_tw
from manipulator.tools import Tools
from flask_controller import Flask_controller

app = Flask(__name__)
tls = Tools()
sfc = Flask_controller()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/0/', methods=['GET'])
def api_0():
    return jsonify(tls.get_tasks('0'))

@app.route('/api/0/change', methods=['POST'])
def api_0_change():
    sfc.timer_change( request.json )
    return jsonify(tls.get_tasks('0'))

@app.route('/test/')
def test():
    sq_tw = Sq_tw()
    return sq_tw.mysql_select_sv_users('description','1094616097725140993')

@app.route('/test/<screen_name>')
def test_sn(screen_name=None):
    g_tw_user_tw = G_tw_user_tw()
    return str(g_tw_user_tw.get(screen_name = screen_name)) + '<br>key追加完了'


if __name__ == "__main__":
    app.run(debug=True)