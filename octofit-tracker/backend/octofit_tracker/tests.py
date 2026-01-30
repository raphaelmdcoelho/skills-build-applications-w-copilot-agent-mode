from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pw', team=team)
        self.assertEqual(user.team, team)

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pw', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=10, distance=2.5)
        self.assertEqual(activity.user, user)

    def test_workout_create(self):
        team = Team.objects.create(name='Test Team')
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for=team)
        self.assertEqual(workout.suggested_for, team)

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=42)
        self.assertEqual(leaderboard.team, team)
