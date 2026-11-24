from contextlib import redirect_stdout
from io import StringIO

from django.test import TestCase


class ChurnRatePageTests(TestCase):
    def test_get_displays_form(self):
        response = self.client.get("/")

        self.assertContains(response, 'name="PresentCust"')
        self.assertContains(response, 'name="initialCust"')

    def test_post_displays_calculated_rate_and_preserves_inputs(self):
        response = self.client.post(
            "/",
            {"PresentCust": "25", "initialCust": "100"},
        )

        self.assertContains(response, "Churn Rate: 25.00%")
        self.assertContains(response, 'name="PresentCust" min="0" step="1" value="25"')
        self.assertContains(response, 'name="initialCust" min="1" step="1" value="100"')

    def test_post_prints_inputs_and_result_to_server_output(self):
        output = StringIO()

        with redirect_stdout(output):
            self.client.post("/", {"PresentCust": "23", "initialCust": "20"})

        self.assertIn("PresentCust = 23", output.getvalue())
        self.assertIn("initialCust = 20", output.getvalue())
        self.assertIn("Churn Rate = 115.0", output.getvalue())

    def test_post_with_zero_initial_customers_displays_validation_error(self):
        response = self.client.post(
            "/",
            {"PresentCust": "25", "initialCust": "0"},
        )

        self.assertContains(response, "Initial customers must be greater than zero.")
        self.assertNotContains(response, "Churn Rate:")

    def test_post_with_blank_values_displays_validation_error(self):
        response = self.client.post(
            "/",
            {"PresentCust": "", "initialCust": ""},
        )

        self.assertContains(response, "Enter whole numbers for both customer counts.")
