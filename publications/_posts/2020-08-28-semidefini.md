---
date:   2020-08-28 00:53:26+00:00
title: Semidefinite Representations in Semialgebraic Optimization and Dynamics-Oriented Learning
status: sb
authors: Bachir El Khadir
links: 
  - PDF: "/assets/pdfs/bachir_el_khadir_thesis_princeton.pdf"
  - Slides: https://bachirelkhadir.github.io/thesis-princeton-orfe/#/
journal: PhD Thesis
---

Semidefinite programming (SDP) has known a recent surge in popularity
in the last few decades in the mathematical optimization
community. This surge could be explained by two main reasons. On the
one hand, a mature theoretical and computational foundation backing
SDP allows one to efficiently compute solutions and obtain formal
guarantees on their quality. On the other hand, breakthrough
developments connecting SDP to real algebraic geometry have resulted
in fundamentally new approaches to tackling semialgebraic optimization
problems. The same reasons also make SDP-based approaches well-suited
for applications in dynamical systems theory where systems of interest
can often be described by algebraic data, and where one seeks to
certify various notions of stability, safety, and robustness on the
behavior of these systems.



The contribution of the first part of this thesis is at the interface
of SDP and semialgebraic optimization.  We start by presenting a
framework for semidefinite programs whose objective function and
constraints vary polynomially with time. Our goal is then to find a
time-dependent solution that maximizes the aggregate of the objective
function over time while satisfying the constraints at all times. We
then turn our attention to studying the relationship between two
notions that are known to make semialgebraic optimization problems
more tractable: the geometric notion of convexity and the algebraic
one of being a sum of squares. The interplay between the two notions
is poorly understood. For instance, to this date, no example of a
convex homogeneous polynomial (of any degree $d$ and in any number of
variables $n$) that is not a sum of squares is known. We show that no
such example exists in the case where $n=4$ and $d=4$, and if a
certain conjecture of Blekherman related to the so-called
\emph{Cayley-Bacharach} relationships is true, no such example exists
in the case where $n=3$ and $d=6$ neither. These were the two minimal
cases where one would have any hope of seeing convex homogeneous
polynomials that are not sums of squares, due to known obstructions.
%The main ingredient of the proof is a generalization of
%the classical Cauchy-Schwarz inequality.


In the second part of this thesis, we study the power of SDP and
semialgebraic optimization when applied for the task of analyzing
dynamical systems. First, we focus on the notion of stability --- one
of the most fundamental properties that a dynamical system can
verify. An ingenious idea, which was proposed by Lyapunov in his
thesis at the end of the $19\text{th}$ century, turns the question of
testing whether a dynamical system is locally asymptotically stable to
the question of existence of an associated \emph{Lyapunov} function;
but it was an open question for some time whether this Lyapunov
function could be assumed to be a polynomial in the special case where
the dynamical system is given by a polynomial vector field with
rational coefficients. We give the first example of a globally (and in
particular, locally) asymptotically stable polynomial vector field
with integer coefficients that does not have an analytic Lyapunov
function, let alone a polynomial one. We show by contrast that an
asymptotically stable dynamical system given by a {homogeneous}
vector field admits a {rational} (i.e., ratio of two polynomials)
Lyapunov function, and we give a hierarchy of semidefinite programs
that is guaranteed to find this Lyapunov function in finite time.


Interestingly, the same tools that help analyze dynamical systems can
also be applied for learning these dynamical systems from data. We
develop a mathematical formalism of the problem of learning a vector
field that fits sample measured trajectories and satisfies a concrete
collection of local or global properties (side information). We extend
results from constrained polynomial-approximation theory to show that,
under some conditions, polynomial vector fields can fit the
trajectories of any continuously-differentiable vector field to
arbitrary accuracy while respecting side information. Furthermore, we
show that SDP-based techniques are particularly suited for this
learning task.  We end by showing an application to imitation learning
problems in robotics.

