# Some illustrations for [this project](https://github.com/SMPyBandits/SMPyBandits)

Here are some plots illustrating the performances of the different [policies](../SMPyBandits/Policies/) implemented in this project, against various problems (with [`Bernoulli`](../SMPyBandits/Arms/Bernoulli.py) arms only):

## Histogram of regrets at the end of some simulations
On a simple Bernoulli problem, we can compare 16 different algorithms (on a short horizon and a small number of repetitions, just as an example).
If we plot the distribution of the regret at the end of each experiment, `R_T`, we can see this kind of plot:

![Histogramme_regret_monoplayer_2.png](Histogramme_regret_monoplayer_2.png)

It helps a lot to see both the mean value (in solid black) of the regret, and its distribution of a few runs (100 here).
It can be used to detect algorithms that perform well in average, but sometimes with really bad runs.
Here, the [Exp3++](../SMPyBandits/Policies/Exp3PlusPlus.py) seems to had one bad run.

---

## Demonstration of different [Aggregation policies](../Aggregation.md)
On a fixed Gaussian problem, aggregating some algorithms tuned for this exponential family (ie, they know the variance but not the means).
Our algorithm, [Aggregator](../SMPyBandits/Policies/Aggregator.py), outperforms its ancestor [Exp4](../SMPyBandits/Policies/Aggregator.py) as well as the other state-of-the-art experts aggregation algorithms, [CORRAL](../SMPyBandits/Policies/CORRAL.py) and [LearnExp](../SMPyBandits/Policies/LearnExp.py).

![main____env3-4_932221613383548446.png](main____env3-4_932221613383548446.png)

---

## Demonstration of [multi-player algorithms](../MultiPlayers.md)
Regret plot on a random Bernoulli problem, with `M=6` players accessing independently and in a decentralized way `K=9` arms.
Our algorithms ([RandTopM](../SMPyBandits/PoliciesMultiPlayers/RandTopM.py) and [MCTopM](../SMPyBandits/PoliciesMultiPlayers/RandTopM.py), as well as [Selfish](../SMPyBandits/Policie/Selfish.py)) outperform the state-of-the-art [rhoRand](../SMPyBandits/PoliciesMultiPlayers/rhoRand.py):

![MP__K9_M6_T5000_N500__4_algos__all_RegretCentralized____env1-1_8318947830261751207.png](MP__K9_M6_T5000_N500__4_algos__all_RegretCentralized____env1-1_8318947830261751207.png)


Histogram on the same random Bernoulli problems.
We see that some all algorithms have a non-negligible variance on their regrets.

![MP__K9_M6_T10000_N1000__4_algos__all_HistogramsRegret____env1-1_8200873569864822246.png](MP__K9_M6_T10000_N1000__4_algos__all_HistogramsRegret____env1-1_8200873569864822246.png)


Comparison with two other "state-of-the-art" algorithms ([MusicalChair](../SMPyBandits/Policies/MusicalChair.py) and [MEGA](../SMPyBandits/Policies/MEGA.py), in semilogy scale to really see the different scale of regret between efficient and sub-optimal algorithms):

![MP__K9_M3_T123456_N100__8_algos__all_RegretCentralized_semilogy____env1-1_7803645526012310577.png](MP__K9_M3_T123456_N100__8_algos__all_RegretCentralized_semilogy____env1-1_7803645526012310577.png)

---

## Other illustrations
### Piece-wise stationary problems
Comparing [Sliding-Window UCB](../SMPyBandits/Policies/SlidingWindowUCB.py) and [Discounted UCB](../SMPyBandits/Policies/DiscountedUCB.py) and [UCB](../SMPyBandits/Policies/UCB.py), on a simple Bernoulli problem which regular random shuffling of the arm.
![Demo_of_DiscountedUCB2.png](Demo_of_DiscountedUCB2.png)

### Sparse problem and Sparsity-aware algorithms
Comparing regular [UCB](../SMPyBandits/Policies/UCB.py), [klUCB](../SMPyBandits/Policies/klUCB.py) and [Thompson sampling](../SMPyBandits/Policies/Thompson.py) against ["sparse-aware" versions](../SMPyBandits/Policies/SparseWrapper.py), on a simple Gaussian problem with `K=10` arms but only `s=4` with non-zero mean.

![Demo_of_SparseWrapper_regret.png](Demo_of_SparseWrapper_regret.png)

---

## Demonstration of the [Doubling Trick policy](../DoublingTrick.md)
On a fixed problem with full restart:
![main____env1-1_3633169128724378553.png](main____env1-1_3633169128724378553.png)

On a fixed problem with no restart:
![main____env1-1_5972568793654673752.png](main____env1-1_5972568793654673752.png)

On random problems with full restart:
![main____env1-1_1217677871459230631.png](main____env1-1_1217677871459230631.png)

On random problems with no restart:
![main____env1-1_5964629015089571121.png](main____env1-1_5964629015089571121.png)
