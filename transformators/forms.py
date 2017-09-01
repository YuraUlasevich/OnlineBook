from django.forms import ModelForm
from .models import Pupil


class PupilForm(ModelForm):
    class Meta:
        model = Pupil
        fields = ['fio', 'group_number', 'test_number']

    def save(self):
        data = self.cleaned_data
        pupil = Pupil(
            fio=data['fio'],
            group_number=data['group_number'],
            test_number=data['test_number']
        )
        pupil.save()
        return pupil
