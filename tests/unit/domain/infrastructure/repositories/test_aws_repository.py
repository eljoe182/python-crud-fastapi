import unittest
from unittest.mock import MagicMock
from context.aws.infrastructure.repository.AWSRepository import AWSRepository
from shared.infrastructure.persistence.aws import AWSClient


class TestAWSRepository(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock(spec=AWSClient)
        self.mock_s3_client = self.mock_client.get_client_s3.return_value
        self.repository = AWSRepository(client=self.mock_client)

    def test_list_files_with_contents(self):
        # Setup mock response
        self.mock_s3_client.list_objects_v2.return_value = {
            "Contents": [{"Key": "file1.txt"}, {"Key": "file2.txt"}]
        }
        bucket_name = 'test-bucket'
        
        # Call the method
        result = self.repository.list_files(bucket_name)
        
        # Assert the result
        self.assertEqual(result, [{"Key": "file1.txt"}, {"Key": "file2.txt"}])
        self.mock_s3_client.list_objects_v2.assert_called_once_with(Bucket=bucket_name)

    def test_list_files_empty_bucket(self):
        # Setup mock response
        self.mock_s3_client.list_objects_v2.return_value = {}
        bucket_name = 'empty-bucket'
        
        # Call the method
        result = self.repository.list_files(bucket_name)
        
        # Assert the result is an empty list
        self.assertEqual(result, [])
        self.mock_s3_client.list_objects_v2.assert_called_once_with(Bucket=bucket_name)


if __name__ == '__main__':
    unittest.main()