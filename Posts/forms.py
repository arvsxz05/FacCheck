from django import forms

from Posts.models import Report


class ReportForm(forms.ModelForm):
    pic_report = forms.FileField(required=False)

    def save(self, commit=True):
        instance = super(ReportForm, self).save(commit=commit)
        # print (self.cleaned_data['avatar'])
        if self.cleaned_data['pic_report']:
            instance.profile.pic_report = self.cleaned_data['pic_report']
            instance.profile.save()

    class Meta:
        model = Report
        fields = ['report_type', 'description', 'report_title', 'location', 'pic_report', 'owner']