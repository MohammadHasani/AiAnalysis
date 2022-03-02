# from unittest.mock import patch
#
# from applications.Api.github import GithubAPI
#
#
# @patch('users.requests.get')  # Mock 'requests' module 'get' method.
# def test_download_repo():
#     bad_repo_path = "https://github.com/Kodex-AI/bad-coding-challenges-input/archive/master.tar.gz"
#     repo_path = "https://github.com/Kodex-AI/coding-challenges-input/archive/master.tar.gz"
#
#     class BasicTests(unittest.TestCase):
#         def test_request_response_with_decorator(self, mock_get):
#             """Mocking using a decorator"""
#             mock_get.return_value.status_code = 200  # Mock status code of response.
#             response = get_users()
#
#             # Assert that the request-response cycle completed successfully.
#             self.assertEqual(response.status_code, 200)
#     bad_result = GithubAPI.download_repo(bad_repo_path)
#     correct_result = GithubAPI.download_repo(repo_path)
