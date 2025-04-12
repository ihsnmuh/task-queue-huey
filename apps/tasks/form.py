from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    due_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        label="Tenggat Waktu",
    )

    class Meta:
        model = Task
        fields = ["title", "description", "due_at"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full border px-4 py-2 rounded",
                    "placeholder": "Judul tugas...",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full border px-4 py-2 rounded",
                    "placeholder": "Deskripsi (opsional)...",
                    "rows": 4,
                }
            ),
        }
