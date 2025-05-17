import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/members', methods=["GET"])
def get_all_users_data():
    return "<h5>All records are being displayed</h5>"


@app.route('/members/<string:member_id>', methods=["GET"])
def get_selected_user_data(member_id):
    return "<h5>Member {} details being displayed</h5>".format(member_id)


@app.route('/members', methods=["POST"])
def adding_new_user_data():
    return "<h5>Adding the new user</h5>"


@app.route('/members/<int:member_id>', methods=["PUT", "PATCH"])
def editing_user_data(member_id):
    return "<h5> zyx user : {} data</h5>".format(member_id)


@app.route('/members/<int:member_id>', methods=["DELETE"])
def deleting_user(member_id):
    return "<h5>Deleting user :{}</h5>".format(member_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
