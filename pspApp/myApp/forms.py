from django import forms


class VolebniObdobiForm(forms.Form):
    id_obdobi = forms.IntegerField(required=False)

    def clean_id_obdobi(self):
        data = self.cleaned_data["id_obdobi"]
        if data is not None:
            return data
        return 173

