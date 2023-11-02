from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_nonoverlap():
    initial = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    final = time_range("2010-01-12 13:00:00", "2010-01-12 15:00:00")
    expected = []
    assert compute_overlap_time(initial, final) == expected

def test_severalintervals():
    initinterval = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 3)
    finalinterval = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:35:00"), ("2010-01-12 10:35:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00","2010-01-12 10:40:00"), ("2010-01-12 10:40:00","2010-01-12 10:45:00")]
    assert compute_overlap_time(initinterval, finalinterval) == expected

def test_endtime():
    initial = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    final = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")
    expected = [("2010-01-12 12:00:00","2010-01-12 12:00:00")]
    assert compute_overlap_time(initial, final) == expected