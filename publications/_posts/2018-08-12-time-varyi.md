---
date:   2018-08-12 16:28:55+00:00
title: Time-Varying Semidefinite Programs
status: sb
authors: Amir Ali Ahmadi, Bachir El Khadir
link: https://arxiv.org/abs/1808.03994
journal: Mathematics of Operations Research
remark: Accepted with minor revision to Mathematics of Operations Research
images:

    - url: "time-varying-semidefinite-programs/Screenshot_2019-10-31_21.59.34.png"
      thumbnail: "time-varying-semidefinite-programs/Screenshot_2019-10-31_21.59.34_thumb.png"
      description: "Example of a TV-SDP"
    
    - url: "time-varying-semidefinite-programs/tv-maxflow.png"
      description: "Time-varying maxflow instance"
    
    - url: "time-varying-semidefinite-programs/tv-wireless.png"
      thumbnail: "time-varying-semidefinite-programs/tv-wireless_thumb.png"
      description: "Wireless coverage instance"
---

We study time-varying semidefinite programs (TV-SDPs), which are semidefinite programs whose data (and solutions) are functions of time. Our focus is on the setting where the data varies polynomially with time. We show that under a strict feasibility assumption, restricting the solutions to also be polynomial functions of time does not change the optimal value of the TV-SDP. Moreover, by using a Positivstellensatz on univariate polynomial matrices, we show that the best polynomial solution of a given degree to a TV-SDP can be found by solving a semidefinite program of tractable size. We also provide a sequence of dual problems which can be cast as SDPs and that give upper bounds on the optimal value of a TV-SDP (in maximization form). We prove that under a boundedness assumption, this sequence of upper bounds converges to the optimal value of the TV-SDP. Under the same assumption, we also show that the optimal value of the TV-SDP is attained. We demonstrate the efficacy of our algorithms on a maximum-flow problem with time-varying edge capacities, a wireless coverage problem with time-varying coverage requirements, and on bi-objective semidefinite optimization where the goal is to approximate the Pareto curve in one shot.

