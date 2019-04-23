# understandiing cryptography problem 2.l
import string
alphabet = string.ascii_lowercase
#
ALPHABET_LIST = [alphabet[i] for i in range(len(alphabet))]


def create_alphabet_dict(alphabet_list=ALPHABET_LIST):
    # alphabetを数値かする
    output_dict = {}
    for i in range(len(alphabet_list)):
        output_dict[alphabet_list[i]] = i
    return output_dict


ALPHABET_DICT = create_alphabet_dict()
def encryptt(plain_letter,key_alphabet,alphabet_dict=ALPHABET_DICT):
	num_letter = alphabet_dict[plain_letter]
    num_key = alphabet_dict[key_alphabet]
    remainder = (num_letter+num_key) % 26

    return ALPHABET_LIST[remainder]

def decrypt(plain_letter, key_alphabet, alphabet_dict=ALPHABET_DICT):
    # this can also be used for decrypt
    num_letter = alphabet_dict[plain_letter]
    num_key = alphabet_dict[key_alphabet]
    remainder = (num_letter-num_key) % 26

    return ALPHABET_LIST[remainder]


if __name__ == "__main__":
    plain = "bsaspp"
    key = "rsidpy"
    # print(encrypt("a","b"))
    for i in range(len(plain)):
        tmp = decrypt(plain[i], key[i])
        print(tmp)
