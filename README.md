# Simulation-Project
This project uses Stochastic Approximation to estimate the gradient of complicate functions. And use the estimated gradient to do the optimization and solve the real world problems. 
(For queuing system and investment optimization)
And this project is from PKU GLOBEX PROGRAMME Prof.Bernd HEIDERGOTT's course Simulation Methods for Optimization and Learning.
At least, sincerely thanks my team mates:Cui Gehao, Han Yufeng, Lie Bob Jesse, Yuan Huan.

Stochastic Approximation:
#  **Simultaneous Perturbation Stochastic Approximation (SPSA)**

We revisit the analysis of the two-sided FD scheme in the \( d \)-dimensional setting.

Let $\( c_n = \eta_n \Delta_n \)$, where $\( \eta_n \)$ is a scalar and $\( \Delta_n \)$ is a random vector such as $\( \{\Delta_n\} \)$ is an iid sequence, with $\( \Delta_n(k) \)$ as well as $\( 1/\Delta_n(k) \)$ being bounded, symmetric around zero, and the components of $\( \Delta_n(k) \)$ are mutually independent.

- A standard choice is 

$\[
P(\Delta_n(i) = -1) = \frac{1}{2} = P(\Delta_n(i) = 1),
\]$

for all $\( i, n \)$.

- Let 

$\[
(\nabla J^{SPSA}(\theta_n))_i = \frac{J(\theta_n + \eta_n \Delta_n) - J(\theta_n - \eta_n \Delta_n)}{2 \eta_n \Delta_n(i)},
\]$

for $\( 1 \leq i \leq d \)$.

- Note that $\( \nabla J^{SPSA} \)$ requires only two evaluations of $\( J \)$ for evaluating approximately the entire gradient of size $\( d \)$ for arbitrary $\( d \)$.

This method is called **Simultaneous Perturbation Stochastic Approximation (SPSA)**.

# Description of the problem 1:
In this project, we aim to determine the optimal investment strategy for an investor with a
total capital of 1 unit. The capital is to be distributed among n companies over a time period
of t units. The market value of company i at time t is given by Xi
. Let xi ∈ R, i = 1, . . . , n be
given thresholds. Company i will not be able to generate any profft if Xi < xi
. If Xi ≥ xi, thereturn on the investment is given by Yi
. Investing a fraction pi of the capital yields an expected
return of
$$
\p_i
$$
$$
\p_i E[\Y_i \1_{\X_i \geq \x_i}]
$$

for company i, where 
Xn
i=1
pi = 1 and 0 ≤ pi ≤ 1. (2)
Assume that n = 3 and Yi are independent and uniformly distributed on [0, Xi
]. We let
Xi =
ρV +
p
1 − ρ
2ηi
max(W, 1)
, 1 ≤ i ≤ n, (3)
with ηi normally distributed with mean 0 and variance i modeling the company’s idiosyncratic
risk, V standard normally distributed modeling the common factor that affects the economy, and
W exponentially distributed with rate 1/0.3 modeling common market shocks. The variables
V , W, and ηi
’s are all independent. The weight factor is set to ρ = 0.6, and the thresholds are
x1 = 2, x2 = 3, and x3 = 1.
The investor seeks to ffnd the optimal investment strategy by maximizing the risk-adjusted
performance of the investment, also known as the Sharpe ratio, which leads to the objective
function:
max
p1,p2,p3≥0,
Ppi=1
E


 P3
i=1
piYi1Xi≥xi
std
P3
i=1
piYi1Xi≥xi


 , (4)
where std(X) denotes the standard deviation of the random variable X. To simplify the problem
and solution process, we converted the objective function to:
min
p1,p2,p3≥0,
Ppi=1
−E


 P3
i=1
piYi1Xi≥xi
std
P3
i=1
piYi1Xi≥xi


 , (5)
In order to visualize the objective function for the optimization, we drew the 3D plot of the
function (Figure 1 and Figure 2).

 
