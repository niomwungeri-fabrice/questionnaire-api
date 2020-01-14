from rest_framework import status

from tests.set_up import AuthenticateUser


class QuestionPrivateAPITests(AuthenticateUser):

    def test_create_question_successfully(self):
        res = self.client.post('/api/v1/questions/', {
            'body': "body1038"
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
