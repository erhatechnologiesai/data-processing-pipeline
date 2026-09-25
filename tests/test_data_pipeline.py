import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestDataPipeline(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_data_cleansing(self):
        payload = {
            "records": [
                {"Customer Name ": " Alpha Corp ", " MRR ": 4500},
                {"Customer Name ": " Beta LLC ", " MRR ": "N/A"}
            ]
        }
        res = self.client.post("/clean-data", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["total_records"], 2)
        self.assertEqual(data["anomalies_flagged"], 1)
        self.assertIn("customer_name", data["cleaned_records"][0])

if __name__ == "__main__":
    unittest.main()
