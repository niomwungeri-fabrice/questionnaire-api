from unittest import TestCase
from questions.models import Question, Comment
from tests.factories import sample_user, test_user, sample_super_user
from tests.set_up import AuthenticateUser
from meetups.models import MeetUp, Tag


class AccountModelTests(TestCase):
    def test_user_creation_successfully(self):
        user = sample_user()
        self.assertTrue(user.email, test_user['email'])
        self.assertTrue(user.check_password(test_user['password']))

    def test_super_user_creation_successfully(self):
        user = sample_super_user()
        self.assertTrue(user.email, test_user['email'])
        self.assertTrue(user.check_password(test_user['password']))
        self.assertEqual(user.is_superuser, True)

    def test_super_user_creation_failed(self):
        with self.assertRaises(ValueError):
            sample_super_user(is_superuser=False)

    def test_staff_creation_failed(self):
        with self.assertRaises(ValueError):
            sample_super_user(is_superuser=False, is_staff=False)

    def test_user_with_invalid_email(self):
        with self.assertRaises(ValueError):
            sample_user(email=None, password='2489284kdjf')


class QuestionModelTests(AuthenticateUser):

    def test_create_question(self):
        question = Question.objects.create(user=self.user, body="body1038")
        self.assertEqual(str(question), question.body)


class CommentModelTests(AuthenticateUser):
    def test_create_comment_successfully(self):
        question = Question.objects.create(user=self.user, body="body1038")
        comment = Comment.objects.create(user=self.user, question=question,
                                         body="comment body487")
        self.assertEqual(str(comment), comment.body)


class MeetUpsModelTests(AuthenticateUser):
    def test_create_meetUps_successfully(self):
        payload = {
            "name": "Another meeting",
            "venue": "Kenya",
            "event_type": "FESTIVAL_OR_FAIR",
        }
        meet_up = MeetUp.objects.create(user=self.user, **payload)
        self.assertEqual(str(meet_up), meet_up.name)


class TagModelTests(AuthenticateUser):
    def test_create_comment_successfully(self):
        tag = Tag.objects.create(name="tag body487")
        self.assertEqual(str(tag), tag.name)
