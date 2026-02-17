from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'contact_number',
            'role',
            'skills',
            'years_of_experience',
            'bio',
            'portfolio_link',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'email': 'Enter your email address',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'contact_number': 'Contact Number',
            'role': 'Select Role (Freelancer or Client)',
            'skills': 'Add your key skills (comma-separated)',
            'years_of_experience': 'Years of Experience',
            'bio': 'Tell us something about yourself',
            'portfolio_link': 'Link to your portfolio (optional)',
            'password1': 'Create a strong password',
            'password2': 'Confirm your password',
        }

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control bg-dark text-light border-0 shadow-sm mb-3',
                'placeholder': placeholders.get(field, ''),
                'required': 'required',
                'style': 'background-color: #1e1e2f; color: #fff; border-radius: 8px;'
            })

        # Give dropdown a clean look
        self.fields['role'].widget.attrs['class'] = 'form-select bg-dark text-light border-0 shadow-sm mb-3'


# -------------------------------
# Login Form
# -------------------------------
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control bg-dark text-light border-0 shadow-sm mb-3',
                'placeholder': 'Email Address',
                'required': 'required',
                'style': 'background-color: #1e1e2f; color: #fff; border-radius: 8px;'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control bg-dark text-light border-0 shadow-sm mb-3',
                'placeholder': 'Password',
                'required': 'required',
                'style': 'background-color: #1e1e2f; color: #fff; border-radius: 8px;'
            }
        )
    )


class PasswordResetEmailForm(forms.Form):
    email = forms.EmailField(label="Enter your registered email")
