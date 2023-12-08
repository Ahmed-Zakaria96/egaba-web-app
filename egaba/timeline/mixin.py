from accounts.models import UserProfile
import random

class SuggestionsMixin:

    def get_user_object(self):
        user = self.request.user
        return UserProfile.objects.get(user=user)

    def get_suggestions(self):
        user = self.get_user_object()
        following = user.following.all()
        suggestions = UserProfile.objects.all().exclude(pk__in=following)
        random_suggestion = random.choice(suggestions)
        return random_suggestion
