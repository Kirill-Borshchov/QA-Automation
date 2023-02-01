import unittest

import requests
import json

# Open `https://reqres.in` URL in browser - you will see the documentation
api_url = "https://reqres.in/api"
users_path = api_url + "/users"
headers = {
    'Content-type': 'application/json'
}


# Test cases for GET requests
class GetUsersTestCase(unittest.TestCase):

    def test_get_all_users(self):
        # Performing GET request
        response = requests.get(users_path, headers=headers)
        # Retrieving JSON
        result = response.json()

        # Verifying the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["page"], 1)

        per_page_value = result["per_page"]
        user_data = result["data"]
        self.assertTrue(len(user_data) <= per_page_value, "Data length should be less or equal to per page value")

        for user in user_data:
            self.assert_user_is_not_none(user)

    def test_get_single_user(self):
        # Building request URL and performing the request
        id = 2
        response = requests.get(users_path + "/" + str(id), headers=headers)
        result = response.json()

        user = result["data"]
        self.assert_user_is_not_none(user)
        self.assertEqual(user["id"], id)

    def test_get_single_user_not_found(self):
        non_existing_id = 23
        response = requests.get(users_path + "/" + str(non_existing_id), headers=headers)
        self.assertEqual(response.status_code, 404)

    def assert_user_is_not_none(self, user):
        self.assertIsNotNone(user)
        self.assertIsNotNone(user["id"])
        self.assertIsNotNone(user["email"])
        self.assertIsNotNone(user["first_name"])
        self.assertIsNotNone(user["last_name"])
        self.assertIsNotNone(user["avatar"])


# Test cases for POST requests
class PostUsersTestCase(unittest.TestCase):

    def test_create_new_user(self):
        id = 2
        name = "morpheus"
        job = "leader"
        user_data = {
            "name": name,
            "job": job
        }
        user_json = json.dumps(user_data)
        response = requests.put(users_path + "/" + str(id), headers=headers, data=user_json)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], name)
        self.assertEqual(result["job"], job)
        self.assertIsNotNone(result["updatedAt"])


# Test cases for PUT requests
class PutUsersTestCase(unittest.TestCase):

    def test_update_user(self):
        id = 2
        name = "morpheus"
        job = "zion resident"
        user_data = {
            "name": name,
            "job": job
        }
        user_json = json.dumps(user_data)
        response = requests.post(users_path + "/" + str(id), headers=headers, data=user_json)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["name"], name)
        self.assertEqual(result["job"], job)
        self.assertIsNotNone(result["id"])
        self.assertIsNotNone(result["createdAt"])


# Test cases for DELETE requests
class DeleteUsersTestCase(unittest.TestCase):

    def test_delete_user(self):
        id = 2
        response = requests.delete(users_path + "/" + str(id), headers=headers)

        self.assertEqual(response.status_code, 204)


# Creating the suite of test cases
def suite():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests([
        loader.loadTestsFromTestCase(GetUsersTestCase),
        loader.loadTestsFromTestCase(PostUsersTestCase),
        loader.loadTestsFromTestCase(PutUsersTestCase),
        loader.loadTestsFromTestCase(DeleteUsersTestCase),
    ])
    return test_suite


# Running the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
