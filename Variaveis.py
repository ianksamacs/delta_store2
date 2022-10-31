from random import randrange


key_master = ["abracadabra", "abratisezamo"]

letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "x", "y", "z"]


def gerara_cod():
    return [letra[randrange(25)], letra[randrange(25)], letra[randrange(25)], letra[randrange(25)]]


print(gerara_cod())