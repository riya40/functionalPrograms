import random
"""
Generating the coupoun by using the given characters
"""


def generating_coupoun(num_chars):
    characters = '0154fymf5mgkfmvkifbfknh'
    coupoun = ''
    for i in range(num_chars):
        slice_start = random.randint(0, len(characters)-1)
        coupoun += characters[slice_start: slice_start+1]
    print(coupoun)


if __name__ == '__main__':
    num_chars = int(input("enter"))
    generating_coupoun(num_chars)
