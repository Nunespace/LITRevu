from django import forms
from .models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Titre du livre ou article'})
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            "headline": forms.TextInput(attrs={'placeholder': 'Titre de votre critique'}),
            'rating': forms.RadioSelect(attrs={'aria-label': "Attribuez une note de 0 à 5"}, choices=((i, i) for i in range(0, 6)))
        }


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]
