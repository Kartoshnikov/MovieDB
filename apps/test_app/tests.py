from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from test_app.models import Person, Citizen

class PersonModelTests(TestCase):
	
	def test_younger_than_30(self):
		Citizen(citizen='UK').save()
		a = Person(name='Jon', age='10', citizen=Citizen.objects.get(citizen='UK'))
		b = Person(name='Jon', age='40', citizen=Citizen.objects.get(citizen='UK'))
		self.assertIs(a.younger_than_30(), True)
		self.assertIs(b.younger_than_30(), False)


class IndexViewTest(TestCase):
	def test_no_citizen(self):
		response = self.client.get(reverse('test:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No citizen available.')
		self.assertQuerysetEqual(response.context_data['cit_list'], [])
