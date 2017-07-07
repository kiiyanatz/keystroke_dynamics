from core import KeystrokeCaptureData
from features import FeatureExtractor
from model import Fingerprint



def create_fingerprint_from_capture_data(name, capture_data):
    assert isinstance(capture_data, KeystrokeCaptureData)
    fe = FeatureExtractor()
    capture_data.feed(fe)
    features = fe.extract_features()
    return Fingerprint.from_features(name, features)
