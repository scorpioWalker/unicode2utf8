# -*- coding:utf-8 -*-


def split_by_len(s_str, by=6):
    def _split(origin_str, by_len):
        while origin_str:
            yield origin_str[-by_len:]
            origin_str = origin_str[0:-by_len]
    return list(_split(s_str, by))


def unicode_char2utf8_char(u_char):
    if not isinstance(u_char, unicode):
        raise Exception("parameter should be <Type unicode>")

    origin_u_char = u_char.encode("unicode-escape")
    if u"\u0000" <= u_char <= u"\u007f":
        return origin_u_char
    elif u_char <= u"\u07ff":
        byte_mask = ["110", "10"]
    elif u_char <= u"\uffff":
        byte_mask = ["1110", "10", "10"]
    elif u_char <= u"\u10ffff":
        byte_mask = ["1110", "10", "10", "10"]
    else:
        raise Exception("out of bound for unicode")
    if origin_u_char.startswith("\\u"):
        origin_u_char = origin_u_char[2:]               # strip '\u' prefix
        bin_char = bin(int(origin_u_char, 16))[2:]      # convert hex to bin str with `0b` striped
        splited_bin = split_by_len(bin_char)
        assert len(splited_bin) == len(byte_mask)
        char_list = []
        byte_mask.reverse()
        for i, m in enumerate(byte_mask):
            prefix_len = len(m)
            bin_len = len(splited_bin[i])
            concat_bin = m + ('0' * (8 - prefix_len - bin_len)) + splited_bin[i]
            hex_part = hex(int(concat_bin, 2))
            char_list.insert(0, hex_part)
        return "".join(char_list)
    else:
        raise Exception("after encode as unicode-escape, the str should start with `\\u`")


def unicode2utf8(u_str):
    return "".join([unicode_char2utf8_char(c) for c in u_str])


print repr(unicode2utf8(u"你"))
print repr(u"你".encode("utf-8"))

print repr(unicode2utf8(u"中国"))
print repr(u"中国".encode("utf-8"))

print repr(unicode2utf8(u"中"))
print repr(u"中".encode("utf-8"))
