# -*- coding: utf-8 -*-
r""" The epsilon-decreasing random policy.

- :math:`\varepsilon(t) = \min(1, \varepsilon_0 / \max(1, t))`
- Ref: https://en.wikipedia.org/wiki/Multi-armed_bandit#Semi-uniform_strategies
"""
from __future__ import division, print_function  # Python 2 compatibility

__author__ = "Lilian Besson"
__version__ = "0.2"

from .EpsilonGreedy import EpsilonGreedy

#: Default value for epsilon
EPSILON = 0.1


class EpsilonDecreasing(EpsilonGreedy):
    r""" The epsilon-decreasing random policy.

    - :math:`\varepsilon(t) = \min(1, \varepsilon_0 / \max(1, t))`
    - Ref: https://en.wikipedia.org/wiki/Multi-armed_bandit#Semi-uniform_strategies
    """

    def __init__(self, nbArms, epsilon=EPSILON, lower=0., amplitude=1.):
        super(EpsilonDecreasing, self).__init__(nbArms, lower=lower, amplitude=amplitude)
        assert 0. <= epsilon <= 1., "Error: the 'epsilon' parameter for EpsilonDecreasing class has to be in [0, 1]."  # DEBUG
        self._epsilon = epsilon

    def __str__(self):
        return "EpsilonDecreasing(e:{})".format(self._epsilon)

    # This decorator @property makes this method an attribute, cf. https://docs.python.org/2/library/functions.html#property
    @property
    def epsilon(self):
        r"""Decreasing :math:`\varepsilon(t) = \min(1, \varepsilon_0 / \max(1, t))`."""
        return min(1, self._epsilon / max(1, self.t))
