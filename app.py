from flask import Flask, render_template
import json
from data_model import DB, User, Tweet


def create_app():
    """create the app and various pages in it"""
    app = Flask(__name__)

    # make a database to store all the data of the User and the Tweets etc
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # initialize the application
    DB.init_app(app)

    # navigation of the page to be declared here
    @app.route('/')
    def landing():
        # Sqlalchemy drop all the tables
        DB.drop_all()
        DB.create_all()
        app_user = User(id=1, name='User1')
        DB.session.add(app_user)
        app_user = User(id=2, name='User2')
        DB.session.add(app_user)
        app_user = User(id=3, name='User3')
        DB.session.add(app_user)
        app_user = User(id=4, name='User4')
        DB.session.add(app_user)
        app_user = User(id=5, name='User55')
        DB.session.add(app_user)
        DB.session.commit()
        with open(
                '/Users/rob/G_Drive_sing.parvi/Colab_Notebooks/Unit-3-Sprint-3-Productization-and-Cloud/module1-web-application-development-with-flask/assignment3.3.1/templates/landing.json') as f:
            args = json.load(f)
        return render_template('base.html', **args)

    @app.route('/products')
    def products():
        new_tweet = Tweet(id=1, text='User1_tweet', user_id=1)
        DB.session.add(new_tweet)
        new_tweet = Tweet(id=2, text='User2_tweet', user_id=2)
        DB.session.add(new_tweet)
        new_tweet = Tweet(id=3, text='User3_tweet', user_id=3)
        DB.session.add(new_tweet)
        new_tweet = Tweet(id=4, text='User4_tweet', user_id=4)
        DB.session.add(new_tweet)
        new_tweet = Tweet(id=5, text='User5_tweet', user_id=5)
        DB.session.add(new_tweet)
        DB.session.commit()
        return render_template('base.html', title='Products', body='products in the body')

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8888)
