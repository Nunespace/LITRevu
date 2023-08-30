from django import forms
from .models import Ticket, Review, UserFollows
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineRadios


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Titre du livre ou article'})
        }


class ReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'headline',
            InlineRadios('rating'),
            'body'
        )

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            "headline": forms.TextInput(attrs={'placeholder': 'Titre de votre critique'}),
            'rating': forms.RadioSelect(choices=((i, i) for i in range(0, 6)))
        }


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]
