# pylint: disable=C0303, C0114, C0116, W1508, E1101, C0301, C0103, W0612, W0621, R0914

import json
import os
import flask
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    login_required,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
import tmdb_api
import wikipedia_api
import get_audio
import get_background

app = flask.Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
if app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgres://"):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config[
        "SQLALCHEMY_DATABASE_URI"
    ].replace("postgres://", "postgresql://")

# autocommit was need to fix "QueuePool limit of size 5 overflow 10 reached"
db = SQLAlchemy(app, session_options={"autocommit": True})

bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)


@bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if flask.request.method == "GET":
        return flask.render_template("index.html")
    if flask.request.method == "POST":
        data = Comments.query.filter_by(username=current_user.username).all()
        # i don't think you can send over data as is or it'll give an error
        # which is why i turned them all into a list
        movie_list = []
        rating_list = []
        comment_list = []
        for x in data:
            movie_list.append(x.movie_title)
            rating_list.append(x.rating)
            comment_list.append(x.comment)
    return flask.jsonify(movie_list, rating_list, comment_list)


@app.route("/save_changes", methods=["POST"])
def save_changes():
    if flask.request.method == "POST":
        jsonData = json.loads(flask.request.data)
        deleted_movies = jsonData["deletedMovies"]
        deleted_ratings = jsonData["deletedRatings"]
        deleted_comments = jsonData["deletedComments"]
        edited_rating = jsonData["edited_rating"]
        edited_comment = jsonData["edited_comment"]
        # this section was to bulk delete reviews
        combinedList = zip(deleted_movies, deleted_ratings, deleted_comments)
        for x in combinedList:
            contains_data = Comments.query.filter_by(
                username=current_user.username,
                movie_title=x[0],
                rating=x[1],
                comment=x[2],
            ).first()
            if contains_data is not None:
                db.session.begin()
                Comments.query.filter_by(
                    username=current_user.username,
                    movie_title=x[0],
                    rating=x[1],
                    comment=x[2],
                ).delete()
                db.session.commit()
        comment_id = []
        for x in Comments.query.filter_by(username=current_user.username):
            comment_id.append(x.id)
        index = 0
        db.session.begin()
        for i in comment_id:
            if(edited_rating[index] == ""):
                pass
            else:
                update = Comments.query.filter_by(id=i).update(
                    {Comments.rating: edited_rating[index]}
                )
            index = index + 1
        index = 0
        for i in comment_id:
            if(edited_comment[index] == ""):
                pass
            else:
                update = Comments.query.filter_by(id=i).update(
                {Comments.comment: edited_comment[index]}
            )
            index = index + 1
        db.session.commit()
    return flask.redirect(flask.url_for("bp.profile"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # function will check if the method is either get or post and act accordingly
    if flask.request.method == "GET":
        return flask.render_template("signup.html")
    if flask.request.method == "POST":
        db.session.begin()
        data = flask.request.form["username"]
        contains_data = Users.query.filter_by(username=data).first()
        # if the user enters a username and it is not already in the database, it will be added.
        if contains_data is None:
            insert_data = Users(data)
            db.session.add(insert_data)
            db.session.commit()
            # once added to the database, it will automatially redirect to the login page
            return flask.redirect(flask.url_for("login"))
        flask.flash("Username already exist / is incorrect. Please login instead.")
    return flask.render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # function will check if the method is either get or post and act accordingly
    if flask.request.method == "GET":
        return flask.render_template("login.html")
    if flask.request.method == "POST":
        db.session.begin()
        data = flask.request.form["username"]
        contains_data = Users.query.filter_by(username=data).first()
        # if the user enters a username and it is in the database, the user will be logged in.
        if contains_data is not None:
            login_user(contains_data)
            # once logged in, it will automatially redirect to the index page
            return flask.redirect(flask.url_for("index"))
        flask.flash("Username does not exist / is incorrect. Please signup instead.")
    return flask.render_template("login.html")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    # when the user clicks on the logout button this section will be called and log the user out
    # their session will end and their cookies will be cleared
    # please remember to logout when you're done!!!
    logout_user()
    return flask.redirect(flask.url_for("signup"))


@app.route("/", methods=["GET", "POST"])
def index():
    # this will check if the current user is authenticated
    if current_user.is_authenticated:
        # this function is being called to retrieve the movie data
        (
            movie_title,
            movie_tagline,
            movie_genres,
            movie_poster_file,
        ) = tmdb_api.generate_movie_info(tmdb_api.os.getenv("TMDB_KEY"))

        movie_poster_url = tmdb_api.generate_movie_poster(
            tmdb_api.os.getenv("TMDB_KEY"), movie_poster_file
        )

        # this methid is being called to retrieve the wikipedia page URL
        wiki_url = wikipedia_api.get_wiki_page(movie_title)
        wiki_url = wiki_url[len(wiki_url) - 1]

        # these two methods are simply retriving audio and background data for styling based
        # on the current movie being displayed which is why movie_title is being passed in
        audio, audio_title, audio_artist = get_audio.get_audio_file(movie_title)
        background = get_background.get_background_file(movie_title)
        if flask.request.method == "GET":
            # this section will render out an HTML page with variables being passed.
            return flask.render_template(
                "main.html",
                # the HTML page can use all these data being passed in
                movie_title=movie_title,
                movie_tagline=movie_tagline,
                movie_genres=movie_genres,
                movie_poster=movie_poster_url,
                wiki_page=wiki_url,
                audio=audio,
                audio_title=audio_title,
                audio_artist=audio_artist,
                background=background,
                user=current_user.username,
                # we are querying the database to find all movie_title that matches the movie_title
                # column within the Comments table of our database
                comments=Comments.query.filter_by(movie_title=movie_title).all(),
            )
        if flask.request.method == "POST":
            # this section will retrieve the data being submitted from data and add them into the database
            db.session.begin()
            comment = Comments(
                flask.request.form["movie_title"],
                current_user.username,
                flask.request.form["rating"],
                flask.request.form["comment"],
            )
            db.session.add(comment)
            db.session.commit()
            return flask.redirect(flask.request.url)
    # if the current_user is not authincated (not logged in) it will redirect to the signup page
    return flask.redirect(flask.url_for("signup"))


app.register_blueprint(bp)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


if __name__ == "__main__":
    db.create_all()
    from models import Users, Comments

    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
    )
