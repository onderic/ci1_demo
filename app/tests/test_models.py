from django.test import TestCase
from udms.models import DisciplinaryCase

class DisciplinaryCaseTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        DisciplinaryCase.objects.create(title='cheating exams', description='was caught cheating in final exams')
    
    def test_title_label(self):
        case = DisciplinaryCase.objects.get(id=1)
        field_label = case._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        case = DisciplinaryCase.objects.get(id=1)
        field_label = case._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_created_at_auto_now_add(self):
        case = DisciplinaryCase.objects.get(id=1)
        self.assertIsNotNone(case.created_at)
      

    def test_updated_at_auto_now(self):
        case = DisciplinaryCase.objects.get(id=1)
        # Simulate update
        case.title = 'Updated Title'
        case.save()
        updated_case = DisciplinaryCase.objects.get(id=1)
        self.assertNotEqual(case.created_at, updated_case.updated_at)
        # ^ Changed from case.created_at to case.updated_at
        self.assertEqual(case.updated_at, updated_case.updated_at)
      