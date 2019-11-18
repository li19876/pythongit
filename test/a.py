import base64
import zlib


def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token.encode())
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    return token_string
if __name__ == '__main__':
    a = 'eJwljc2NwjAQhXvh4KPjJOBESD4gTkiIGwWYZAwDsR2Nx0j0wJ0mqIB62D7W2j29T0/vZ2EJ7G40SgyW4R+QHwfrwfw8X9/PW4wYAtA25sAbZioZEWdGn9M2jmBqJSLhGcORJnNhntO6qk5X6QE52yCH6KvC6YKVmO25FIoQl0lTN1rMk2UXyRebMN32cIepcIrERuQEf38542hc63SvO9DDql+6trXadbJedU2vVaO1rKWSavELlbZHsA=='

    token1 = decode_token(a)
    print(token1)
