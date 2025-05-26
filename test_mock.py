import Mock as mk
countries = {
    "Singapore": [{"city": "Singapore", "population": 5450000}],
    "Japan": [{"city": "Tokyo", "population": 13960000}, {"city": "Osaka", "population": 2690000}],
    "Indonesia": [{"city": "Jakarta", "population": 10560000}, {"city": "Surabaya", "population": 2800000}]
}

def test_avg():
    avg=(5450000+13960000+2690000+10560000+2800000)/5
    y=mk.Avg_population_cities()
    assert(avg==y)
