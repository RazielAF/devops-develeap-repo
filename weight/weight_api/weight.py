from pickle import NONE
from flask import Flask, redirect, url_for, render_template, request, jsonify
import db_utils as dbutils
import utils as utils
from datetime import datetime
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def api_weight():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        direction = request.form.get("direction")
        truck = request.form.get("truck")
        containers_id = request.form.get("containers_id")
        truck_weight = request.form.get("truck_weight")
        unit = request.form.get("unit")
        force = request.form.get("force")
        produce = request.form.get("produce")

        dbutils.post_weight(
            direction, truck, containers_id, truck_weight, unit, force, produce
        )
        # dbutils.post_containers(containers_id)

        return f"direction : {direction} truck = {truck}, containers_id = {containers_id}, truck_weight = {truck_weight} unit = {unit}, force = {force}, produce = {produce};"


@app.route("/getweightparams", methods=["GET", "POST"])
def get_params_weight():
    if request.method == "GET":
        frm = (
            datetime.now()
            .replace(hour=0, minute=0, second=1, microsecond=0)
            .strftime("%Y%m%d%H%M%S")
        )
        to = datetime.now().strftime("%Y%m%d%H%M%S")
        return render_template("get_weight.html", frm=frm, to=to)
    else:
        filter = request.form.get("filter")
        frm = request.form.get("from")
        to = request.form.get("to")
        return redirect(
            url_for("get_weight", frm=frm, to=to, filter=filter, **request.args)
        )


@app.route("/weight", methods=["GET"])
def get_weight():
    if request.method == "GET":
        try:
            args = request.args
            t1 = args.get(
                "frm",
                default=datetime.combine(
                    datetime.today().replace(hour=0, minute=0, second=1, microsecond=0),
                    datetime.min.time(),
                ),
            )
            t2 = args.get("to", default=datetime.now())
            frm = datetime.strptime(t1, "%Y%m%d%H%M%S")
            to = datetime.strptime(t2, "%Y%m%d%H%M%S")
            filter = args.get("filter")
        except:
            frm = (
                datetime.now()
                .replace(hour=0, minute=0, second=1, microsecond=0)
                .strftime("%Y%m%d%H%M%S")
            )
            to = datetime.now().strftime("%Y%m%d%H%M%S")
            filter = "'in', 'out', 'na'"
        return json.dumps(dbutils.get_weight(frm, to, filter))


@app.route("/health", methods=["GET"])
def health():
    if request.method == "GET":
        try:
            dbutils.health_db()
            output = "Database is ok"
            status = 200
        except Exception as e:
            output = str(e)
            status = 500
        return output, status


@app.route("/session/", methods=["GET", "POST"])
def post_session():
    if request.method == "POST":
        session_id = request.form.get("sesid")
        if request.form.get("get_json") == "get json":
            post_session.global_type = "get json"
            return redirect(url_for("get_session", sid=session_id))
        elif request.form.get("show_table") == "show table":
            post_session.global_type = "show table"
            return redirect(url_for("get_session", sid=session_id))
    else:
        return render_template("session_post.html")


@app.route("/session/<sid>", methods=["GET"])
def get_session(sid):
    if request.method == "GET":
        try:
            dbutils.session_db(sid)
            status = 200
            if post_session.global_type == "get json":
                return utils.get_session_json(dbutils.session_db.output)
            elif post_session.global_type == "show table":
                return (
                    render_template("session.html", data=dbutils.session_db.output),
                    status,
                )
        except Exception as e:
            output = str(e)
            status = 404
            return render_template("page404.html", show=output), status


@app.route("/unknown/", methods=["GET"])
def get_unknown_containers():
    if request.method == "GET":
        try:
            dbutils.unknown_containers_db()
            status = 200
            error = "no"
            return dbutils.unknown_containers_db.list1
            # return render_template("unknown_container.html", err = error, data = dbutils.unknown_containers_db.list1), status
        except Exception as e:
            status = 404
            error = "yes"
            return (
                render_template("unknown_container.html", err=error, show=str(e)),
                status,
            )


@app.route("/batch_weight", methods=["GET", "POST"])
def batch_weight():
    if request.method == "GET":
        return render_template("batch_weight.html")
    if request.method == "POST":
        batch_file = request.form.get("batch_file")
        try:
            utils.upload_in_data(batch_file)
        except:
            return "provided file doesn't exist!"

        return "success"


@app.route("/item/", methods=["GET", "POST"])
def post_itemid():
    if request.method == "GET":
        frm = datetime.combine(
            datetime.today().replace(day=1), datetime.min.time()
        ).strftime("%Y%m%d%H%M%S")
        to = datetime.now().strftime("%Y%m%d%H%M%S")
        return render_template("item.html", frm=frm, to=to)
    else:
        itemid = request.form.get("itemid")
        frm = request.form.get("from")
        to = request.form.get("to")
        return redirect(url_for("get_item", id=itemid, frm=frm, to=to))


@app.route("/item/<id>", methods=["GET"])
def get_item(id):
    # item = get_item_db(id)
    args = request.args
    t1 = args.get(
        "frm",
        default=datetime.combine(datetime.today().replace(day=1), datetime.min.time()),
    )
    t2 = args.get("to", default=datetime.now())
    frm = datetime.strptime(t1, "%Y%m%d%H%M%S")
    to = datetime.strptime(t2, "%Y%m%d%H%M%S")
    weight_item_truck = dbutils.get_weight_item(id, t1, t2)
    return json.dumps(weight_item_truck)
    # except:
    # return render_template("page404.html")


if __name__ == "__main__":
    app.run(debug=True)
