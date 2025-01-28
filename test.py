import main

def test_euc_dist():
    assert int(main.euc_dist([3,0],[0,4])) == 5
    assert int(main.euc_dist([0,7],[24,0])) == 25
    assert main.euc_dist([1.5, 1.5], [0.0, 3.5]) == 2.5

def test_min_geo_dist():
    assert main.min_geo_dist([[1,2], [2,3]], [[1,0], [1,3.5]]) == [[1,3.5], [1,3.5]]
    assert main.min_geo_dist([[1,0], [2,0]], [[1,0], [2.5,0]]) == [[1,0], [2.5,0]]


