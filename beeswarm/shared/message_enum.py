from enum import Enum


class Messages(Enum):
    STOP = 'STOP'
    START = 'START'
    CONFIG = 'CONFIG'
    BROADCAST = 'BROADCAST'
    OK = 'OK'
    FAIL = 'FAIL'
    PUBLISH_CONFIG = 'PUBLISH_CONFIG'
    # KEY DRONE_ID DRONE_PRIVATE_KEY
    KEY = 'KEY'
    # CERT DRONE_ID DRONE_CERT
    CERT = 'CERT'
