from modules import languageL2


def test_languageL2():
    assert languageL2.get_is_accepted("0") == False
    assert languageL2.get_is_accepted("1") == False
    assert languageL2.get_is_accepted("00") == False
    assert languageL2.get_is_accepted("01") == False
    assert languageL2.get_is_accepted("10") == False
    assert languageL2.get_is_accepted("11") == True
    assert languageL2.get_is_accepted("000") == False
    assert languageL2.get_is_accepted("001") == False
    assert languageL2.get_is_accepted("010") == False
    assert languageL2.get_is_accepted("011") == False
    assert languageL2.get_is_accepted("100") == False
    assert languageL2.get_is_accepted("101") == False
    assert languageL2.get_is_accepted("110") == True
    assert languageL2.get_is_accepted("111") == False
    assert languageL2.get_is_accepted("0000") == False
    assert languageL2.get_is_accepted("0001") == False
    assert languageL2.get_is_accepted("0010") == False
    assert languageL2.get_is_accepted("0011") == False
    assert languageL2.get_is_accepted("0100") == False
    assert languageL2.get_is_accepted("0101") == False
    assert languageL2.get_is_accepted("0110") == False
    assert languageL2.get_is_accepted("0111") == False
    assert languageL2.get_is_accepted("1000") == False
    assert languageL2.get_is_accepted("1001") == False
    assert languageL2.get_is_accepted("1010") == False
    assert languageL2.get_is_accepted("1011") == False
    assert languageL2.get_is_accepted("1100") == True
    assert languageL2.get_is_accepted("1101") == False
    assert languageL2.get_is_accepted("1110") == False
    assert languageL2.get_is_accepted("1111") == True
