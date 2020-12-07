---
date:   2019-05-20 17:33:20+00:00
title: Learning Dynamical Systems with Side Information
status: pb
authors: Amir Ali Ahmadi, Bachir El Khadir
link: https://arxiv.org/abs/2008.10135
journal: Proceedings of Machine Learning Research vol   120:1–10, 2020
remark: 
---

We present a mathematical and computational framework for the problem of learning a dynamical system from noisy observations of a few trajectories and subject to side information. Side information is any knowledge we might have about the dynamical system we would like to learn besides trajectory data. It is typically inferred from domain-specific knowledge or basic principles of a scientific discipline. We are interested in explicitly integrating side information into the learning process in order to compensate for scarcity of trajectory observations. We identify six types of side information that arise naturally in many applications and lead to convex constraints in the learning problem. First, we show that when our model for the unknown dynamical system is parameterized as a polynomial, one can impose our side information constraints computationally via semidefinite programming. We then demonstrate the added value of side information for learning the dynamics of basic models in physics and cell biology, as well as for learning and controlling the dynamics of a model in epidemiology. Finally, we study how well polynomial dynamical systems can approximate continuously-differentiable ones while satisfying side information (either exactly or approximately). Our overall learning methodology combines ideas from convex optimization, real algebra, dynamical systems, and functional approximation theory, and can potentially lead to new synergies between these areas.

