from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.thing = Snack.objects.create(name="pickle", rating=1, reviewer=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.thing), "pickle")

    def test_snacks_content(self):
        self.assertEqual(f"{self.thing.name}", "pickle")
        self.assertEqual(f"{self.thing.reviewer}", "tester")
        self.assertEqual(self.thing.rating, 1)

    def test_snacks_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snacks_list.html")

    def test_snacks_detail_view(self):
        response = self.client.get(reverse("snacks_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Reviewer: tester")
        self.assertTemplateUsed(response, "snacks_detail.html")

    def test_snacks_create_view(self):
        response = self.client.post(
            reverse("snacks_create"),
            {
                "name": "Rake",
                "rating": 2,
                "reviewer": self.user.id,
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("snacks_list"))
        self.assertContains(response, "Rake")

    def test_snacks_update_view_redirect(self):
        response = self.client.post(
            reverse("snacks_update", args="1"),
            {"name": "Updated name", "rating": 3, "reviewer": self.user.id},
        )

        self.assertRedirects(
            response, reverse("snacks_detail", args="1"), target_status_code=200
        )

    def test_snacks_update_bad_url(self):
        response = self.client.post(
            reverse("snacks_update", args="9"),
            {"name": "Updated name", "rating": 3, "reviewer": self.user.id},
        )

        self.assertEqual(response.status_code, 404)

    def test_snacks_delete_view(self):
        response = self.client.get(reverse("snacks_delete", args="1"))
        self.assertEqual(response.status_code, 200)

    # you can also tests models directly
    def test_model(self):
        thing = Snack.objects.create(name="rake", reviewer=self.user)
        self.assertEqual(thing.name, "rake")