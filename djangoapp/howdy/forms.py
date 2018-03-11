from django import forms

class ContactForm(forms.Form):
    p = forms.ChoiceField(
        choices=[(1, 'tt'), (2, 'dd')],
        widget=forms.Select(attrs={'style': 'border-color: blue;',
                                   'padding':'25%'})

    )

    link = forms.CharField(
        label="LINK",
        max_length=2000,
        widget=forms.Textarea(),#attrs={'style': 'border-color: orange;'}),
        help_text='Put some link here!'
    )

    e_type = forms.ChoiceField(
        choices=[(1, 'penguins'), (2, 'mammoth')],
        widget=forms.Select(),#attrs={'style': 'border-color: blue;'})
    )

    d_type = forms.ChoiceField(
        choices=[(1, 'type1'), (2, 'type2')],
        widget=forms.Select(),#attrs={'style': 'border-color: blue;'})
    )


    # source = forms.CharField(       # A hidden input for internal use
    #     max_length=50,              # tell from which page the user sent the message
    #     widget=forms.HiddenInput()
    # )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        link = cleaned_data.get('link')
        if not link:
            raise forms.ValidationError('You have to give the link!')