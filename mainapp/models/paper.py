from django.db import models
from django.urls import reverse

from .default_fields import DefaultFields, ShortableNameFields
from .file import File
from .organization import Organization
from .paper_type import PaperType
from .person import Person


class Paper(DefaultFields, ShortableNameFields):
    reference_number = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    organizations = models.ManyToManyField(Organization, blank=True)
    # Only relevant if a person acts independently from one of the submitting organizations
    persons = models.ManyToManyField(Person, blank=True)
    # There isn't any logic built on change requests, so higher order change requests are allowed
    change_request_of = models.ForeignKey("self", null=True, blank=True)
    # This is relevant e.g. for deadlines
    legal_date = models.DateField(null=True, blank=True)
    main_file = models.ForeignKey(File, null=True, blank=True, related_name="paper_main_file")
    files = models.ManyToManyField(File, blank=True)
    paper_type = models.ForeignKey(PaperType, null=True, blank=True)

    def reference_number_autocomplete(self):
        """ A workaround to prevent empty values in the autocomplete-field in elasticsearch, which throws an error """
        return self.reference_number if len(self.reference_number) > 0 else ' '

    def __str__(self):
        return self.short_name

    def get_default_link(self):
        return reverse('paper', args=[self.id])
