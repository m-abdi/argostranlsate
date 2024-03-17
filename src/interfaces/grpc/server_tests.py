import unittest

from .argostranslate_pb2_grpc import ArgosTranslateStub, grpc, Request


class TestGRPCServer(unittest.TestCase):
    def setUp(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = ArgosTranslateStub(self.channel)

    def test_correct_translation(self):
        expected = "Hello"
        result = self.stub.translate(
            Request(text="سلام", from_lang="fa", to_lang="en")
        ).text
        self.assertEqual(result, expected)

    def test_incorrect_translation(self):
        not_expected = "dog"
        result = self.stub.translate(
            Request(text="گربه", from_lang="fa", to_lang="en")
        ).text
        self.assertNotEqual(result, not_expected)


if __name__ == "__main__":
    unittest.main()
