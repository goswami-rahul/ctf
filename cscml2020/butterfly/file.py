NULL = '\x00'

PASSWORD = 'AAAAAAAAAAAAAAA'

def normal(x: str):
    try:
        return x.encode('ascii', errors='surrogateescape').decode('utf-8')
    except:
        pass
    return x

def main():
    buffer = create_buf(PASSWORD)
    if authenticate(buffer):
        print('THE SECRET FLAG IS: CENSORED')

def create_buf(password):
    password = password + NULL
    buffer = Buffer(2*len(password))
    pass_buffer = Buffer.from_string(password)
    buffer.write_string(pass_buffer, len(password))
    return buffer

def authenticate(buffer):
    print('Enter password:', end=' ')
    user_input = normal(input())
    # user_input = normal('ß' * 16)

    if len(user_input) > 16:
        print('PLEASE INPUT A PASSWORD LESS THAN 16 CHARACTERS LONG')
        return False

    user_input = user_input + NULL
    user_input = user_input.upper()

    pass_check_buffer = Buffer.from_string(user_input)
    buffer.write_string(pass_check_buffer, 0)

    success = buffer.buf[:16] == buffer.buf[16:]

    if not success:
        print('INCORRECT PASSWORD')
        return False
    if success:
        print('SUCCESS!')
        return True

class Buffer(object):
    def __init__(self, length):
        self.buf = [NULL] * length
    
    def write_string(self, buffer, start):
        i = 0
        while i < len(buffer.buf) and buffer.buf[i] != NULL:
            self.buf[start + i] = buffer.buf[i]
            i += 1

    @staticmethod
    def from_string(s):
        buffer = Buffer(len(s))
        i = 0
        while i < len(buffer.buf) and s[i] != NULL:
            buffer.buf[i] = s[i]
            i += 1
        return buffer

if __name__ == '__main__':
    main()
