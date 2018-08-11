import pytest
from lcs.representations import UBR


class TestUBR:

    def test_should_compare_without_ordering(self):
        # given
        o1 = UBR(0, 2)
        o2 = UBR(2, 0)

        # then
        assert o1 == o2
        assert (o1 != o2) is False

    @pytest.mark.parametrize("items, expected_length", [
        ([UBR(2, 5), UBR(5, 2)], 1),
        ([UBR(2, 5), UBR(2, 5)], 1),
        ([UBR(2, 5), UBR(2, 6)], 2)
    ])
    def test_should_not_allow_duplicates(self, items, expected_length):
        # given
        container = set(items)

        # then
        assert len(container) == expected_length
