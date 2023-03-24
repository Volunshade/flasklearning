from flaskblog import app, db, Post, User

with app.app_context():
    db.create_all()

    user_1 = User(username="Tom",
                  email="tom@test.com",
                  password="testing123")
    db.session.add(user_1)
    user_2 = User(username="Raina",
                  email="raina@test.com",
                  password="testing123")
    db.session.add(user_2)
    db.session.commit()

    print(User.query.all())
    print(User.query.first())
    print(User.query.filter_by(username="Tom").all())
    print(User.query.filter_by(username="Tom").first())

    test_user_1 = User.query.filter_by(username="Tom").first()
    print(test_user_1.id, test_user_1)

    tom = User.query.get(1)
    raina = User.query.get(2)
    print(raina)

    post_1 = Post(title="Blog 1", content="First blog post!", user_id=tom.id)
    post_2 = Post(title="Blog 2", content="Second blog post!", user_id=tom.id)
    post_3 = Post(title="Blog 3", content="Third blog post!", user_id=raina.id)
    db.session.add(post_1)
    db.session.add(post_2)
    db.session.add(post_3)
    db.session.commit()

    test_post = Post.query.first()
    print(test_post)

    test_user_2 = User.query.get(1)
    print(test_user_2.posts)
    print(test_user_2.posts[0].title)

    for post in test_user_2.posts:
        print(post)

    db.drop_all()