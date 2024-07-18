from derec.exporters import get_country_by_id
import pytest 


def test_countries_exist():
    assert 'USA' == get_country_by_id(1201).Name
    assert 'China' == get_country_by_id(1202).Name
    assert 'India' == get_country_by_id(1203).Name 
    assert 'Australia' == get_country_by_id(1204).Name
