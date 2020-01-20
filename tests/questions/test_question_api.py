from rest_framework import status

from tests.set_up import BaseTest


class QuestionPrivateAPITests(BaseTest):

    def test_create_question_successfully(self):
        res = self.client.post('/api/v1/questions/', {
            'title': "tittle089887",
            'body': "body1038",
            'meet_up_id': self.meet_up.id
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_up_vote_question_successfully(self):
        res = self.client.patch('/api/v1/questions/{}/upvote'.
                                format(self.question.id),
                                {'title': "tittle089887", 'body': "body1038",
                                 'meet_up_id': self.meet_up.id})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['votes'], 1)

    def test_down_vote_question_successfully(self):
        res = self.client.patch('/api/v1/questions/{}/downvote'.
                                format(self.question.id),
                                {'title': "tittle089887",
                                 'body': "body1038",
                                 'meet_up_id': self.meet_up.id})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['votes'], -1)
