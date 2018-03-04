from django.urls import reverse
from django.test import TestCase

from .models import Mineral


# Create your tests here.
class CourseViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Test',
            image_filename='Test',
            image_caption='Test',
            category='Test',
            formula='Test',
            strunz_classification='Test',
            crystal_system='Test',
            unit_cell='Test',
            color='Test',
            crystal_symmetry='Test',
            cleavage='Test',
            mohs_scale_hardness='Test',
            luster='Test',
            streak='Test',
            diaphaneity='Test',
            optical_properties='Test',
            group='Test',
            refractive_index='Test',
            crystal_habit='Test',
            specific_gravity='Test',
        )

        self.mineral2 = Mineral.objects.create(
            name='Test2',
            image_filename='Test2',
            image_caption='Test2',
            category='Test2',
            formula='Test2',
            strunz_classification='Test2',
            crystal_system='Test2',
            unit_cell='Test2',
            color='Test2',
            crystal_symmetry='Test2',
            cleavage='Test2',
            mohs_scale_hardness='Test2',
            luster='Test2',
            streak='Test2',
            diaphaneity='Test2',
            optical_properties='Test2',
            group='Test2',
            refractive_index='Test2',
            crystal_habit='Test2',
            specific_gravity='Test2',
        )

    def test_mineral_index_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_mineral_list_sort_by_group(self):
        resp = self.client.get(reverse(
            'minerals:group',
            kwargs={'group': 'Test'}
        ))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')

    def test_search_by_term(self):
        resp = self.client.get(reverse('minerals:search'), {'q': 'test'})
        resp2 = self.client.get(reverse('minerals:search'), {'q': 'test'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')

    def test_search_by_letter(self):
        resp = self.client.get(
            reverse('minerals:letter', kwargs={'letter': 't'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')
