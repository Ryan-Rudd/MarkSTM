class RH_CRED(object):
    def __init__(self, USERNAME: str, PASSWORD: str, USES_2FA: bool) -> None:
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.USES_2FA = USES_2FA