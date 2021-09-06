import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto import Random


class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def __pad(self, p_t):
        number_of_bytes_to_pad = self.block_size - len(p_t) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_p_t = p_t + padding_str
        return padded_p_t

    @staticmethod
    def __unpad(p_t):
        last_character = p_t[len(p_t) - 1:]
        bytes_to_remove = ord(last_character)
        return p_t[:-bytes_to_remove]

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        p_t = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(p_t)

    def alexdikersec(self, p_t):
        p_t = self.__pad(p_t)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.alexdikersec(p_t.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")