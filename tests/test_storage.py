import os

import boto3
import pytest
from moto import mock_aws


@pytest.fixture(autouse=True)
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


FAKE_STRIPE_KEY = "sk_test_fake_key_for_unit_tests_only"
FAKE_GITHUB_TOKEN = "ghp_fakefakefakefakefakefakefakefakefake"


@mock_aws
def test_upload_creates_object():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="exports")
    s3.put_object(Bucket="exports", Key="a.csv", Body=b"x")
    assert s3.list_objects(Bucket="exports")["Contents"]
