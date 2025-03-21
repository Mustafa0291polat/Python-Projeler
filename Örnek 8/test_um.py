from um import count

def test_count_single_um():
    assert count("um") == 1

def test_count_um_with_punctuation():
    assert count("um?") == 1

def test_count_um_in_sentence():
    assert count("Um, thanks for the album.") == 1

def test_count_multiple_um():
    assert count("Um, thanks, um...") == 2

def test_count_no_um():
    assert count("yummy") == 0

def test_count_um_case_insensitive():
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("Um") == 1
