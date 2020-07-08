"""
This is my implementation of this paper
Taylor, Matthew, Ruturaj K. Vaidya, Drew Davidson, Lorenzo De Carli, and Vaibhav Rastogi.
"SpellBound: Defending Against Package Typosquatting." arXiv preprint arXiv:2003.03471 (2020).
And,
Hu, Yangyu, Haoyu Wang, Ren He, Li Li, Gareth Tyson, Ignacio Castro, Yao Guo, Lei Wu, and Guoai Xu.
"Mobile app squatting." In Proceedings of The Web Conference 2020, pp. 1727-1738. 2020.
"""
from itertools import groupby
import constants


class OSSquat:
    def __init__(self, package_name: str):
        self.package_name = package_name

    def get_repeated_characters(self):
        characters = list(self.package_name)
        for k, g in groupby(characters):
            num_repeats = sum(1 for i in g)
            if num_repeats > 1:
                yield k, num_repeats

    def has_swapped_characters(self):
        pass

    def get_swapped_words(self):
        for delimiter in constants.pypi_delimiters:
            if delimiter in self.package_name:
                words = self.package_name.split(delimiter)
                return words[1] + delimiter + words[0]

    def has_common_typos(self):
        pass



