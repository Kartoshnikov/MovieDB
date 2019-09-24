from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from core.models import Movie
from core.views import MovieList

# Create your tests here.


class MovieListPaginationTestCase(TestCase):
	
	ACTIVE_PAGINATION_HTML = """
	<li class="page-item">
  	    <a class="page-link" href="{}?page={}">{}</a>
	</li>
	"""

	def setUp(self):
		for i in range(20):
			Movie.objects.create(
				title=f'Title {i}',
				year=1990 + i,
				runtime=100,
			)
	
	def testFirstPage(self):
		movie_list_url = reverse('core:movie_ls')
		request = RequestFactory().get(path=movie_list_url)
		response = MovieList.as_view()(request)

		self.assertEqual(200, response.status_code)
		self.assertTrue(response.context_data['is_paginated'])
		self.assertInHTML(
				self.ACTIVE_PAGINATION_HTML.format(movie_list_url, 1, 1),
				response.rendered_content,
		)
