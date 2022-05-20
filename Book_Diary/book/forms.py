from django import forms

class BooksForm(forms.Form):
    title = forms.CharField(
        label='タイトル', 
        max_length=100,
        required=True)

    name = forms.CharField(
        label='著者', 
        max_length=100,
        required=True)

    image = forms.ImageField(
        label='写真'
    )

    comment = forms.CharField(
        label='感想',
        widget=forms.Textarea
    )

    endday = forms.DateField(
        label='読み終えた日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%d']
    )

    endday = forms.DateField()
