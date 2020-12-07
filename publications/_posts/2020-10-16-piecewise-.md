---
date:   2020-10-16 04:31:08+00:00
title: Piecewise-Linear Motion Planning amidst Static, Moving, or Morphing Obstacles
status: sb
authors: Bachir El Khadir, Jean Bernard Lasserre,  Vikas Sindhwani
link: https://arxiv.org/pdf/2010.08167.pdf
journal: 
remark: 
---

We propose a novel method for planning shortest length piecewise-linear motions through complex environments punctured with static, moving, or even morphing obstacles. Using a moment optimization approach, we formulate a hierarchy of semidefinite programs that yield increasingly refined lower bounds converging monotonically to the optimal path length.

For computational tractability, our global moment optimization approach motivates an iterative motion planner that outperforms competing sampling-based and nonlinear optimization baselines. Our method natively handles continuous time constraints without any need for time discretization, and has the potential to scale better with dimensions compared to popular sampling-based methods.

