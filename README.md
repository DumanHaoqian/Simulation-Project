# Simulation-Project
This project uses Stochastic Approximation to estimate the gradient of complicate functions. And use the estimated gradient to do the optimization and solve the real world problems. 
(For queuing system and investment optimization)
And this project is from PKU GLOBEX PROGRAMME Prof.Bernd HEIDERGOTT's course Simulation Methods for Optimization and Learning.
At least, sincerely thanks my team mates:Cui Gehao, Han Yufeng, Lie Bob Jesse, Yuan Huan.

Stochastic Approximation:
# SPSA, IV (Fully Stochastic Models)

Assume that 

- Let \( (A1) \) be in force for 

\[
P(\Delta_n(i) = -1) = \frac{1}{2} = P(\Delta_n(i) = 1),
\]

for all \( i, n \).

- Let 

\[
(Y^{SPSA}(\theta_n, \omega))_i = \frac{h(\theta_n + \eta_n \Delta_n, \omega) - h(\theta_n - \eta_n \Delta_n, \omega)}{2 \eta_n \Delta_n(i)},
\]

for \( 1 \leq i \leq d \).

- Note that \( Y_n \) requires only two samples of \( h \) for evaluating approximately the entire gradient of size \( d \) for arbitrary \( d \).
 
