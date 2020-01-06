import unittest
from datetime import timedelta, datetime

from app import app, db
from app.models import User, Post


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username="foo")
        u.set_password("bar")
        self.assertFalse(u.check_password("baz"))
        self.assertTrue(u.check_password("bar"))

    def test_followed(self):
        u1 = User(username="foo")
        u2 = User(username="bar")

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u2.followed.all(), [])

    def test_is_following(self):
        u1 = User(username="foo")
        u2 = User(username="bar")

        db.session.add(u1)
        db.session.add(u2)
        u1.follow(u2)
        db.session.commit()

        self.assertTrue(u1.is_following(u2))

    def test_follow(self):
        u1 = User(username="foo")
        u2 = User(username="bar")

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followed.count(), 0)

        u1.follow(u2)
        db.session.commit()

        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, u1.username)

    def test_unfollow(self):
        u1 = User(username="foo")
        u2 = User(username="bar")

        db.session.add(u1)
        db.session.add(u2)
        u1.follow(u2)
        db.session.commit()

        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, u2.username)

        u1.unfollow(u2)
        db.session.commit()

        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.all(), [])

    def test_follow_posts(self):
        u1 = User(username="foo")
        u2 = User(username="bar")
        u3 = User(username="baz")
        u4 = User(username="qux")

        now = datetime.utcnow()
        p1 = Post(body="post from u1", author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from u2", author=u2, timestamp=now + timedelta(seconds=2))
        p3 = Post(body="post from u3", author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from u4", author=u4, timestamp=now + timedelta(seconds=4))

        db.session.add_all([u1, u2, u3, u4, p1, p2, p3, p4])

        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)

        db.session.commit()

        fp1 = u1.followed_posts().all()
        fp2 = u2.followed_posts().all()
        fp3 = u3.followed_posts().all()
        fp4 = u4.followed_posts().all()

        # NOTE: Implicitly testing the sort order desc here, as well...
        self.assertEqual(fp1, [p4, p2, p1])
        self.assertEqual(fp2, [p3, p2])
        self.assertEqual(fp3, [p4, p3])
        self.assertEqual(fp4, [p4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
