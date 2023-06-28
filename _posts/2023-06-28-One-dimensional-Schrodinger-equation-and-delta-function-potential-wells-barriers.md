---
layout: post
title:  "One-dimensional Schrodinger equation and delta-function potential wells-barriers"
date:   2023-06-28
categories: ['x', 'psi', 'psi x', 'e', 'frac']
---
# One-dimensional Schrodinger equation and delta-function potential wells-barriers

一维薛定谔方程和δ-函数势阱/势垒

在量子力学中，薛定谔方程是描述微观粒子（如电子）行为的主要工具。这里我们将考虑一个简单的情况，即一维空间中的粒子受到一个δ-函数势阱或势垒的影响。

薛定谔方程为：

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)
$$

其中，$\hbar$为约化普朗克常数，$m$为粒子质量，$\psi(x)$为粒子在位置$x$处的波函数，$E$为粒子的总能量，$V(x)$为势能函数。

当粒子受到一个位于原点的δ-函数势垒的影响时，$V(x)$被定义为$V(x)=V_0\delta(x)$，其中$V_0$为δ函数的强度。

我们可以将原始的薛定谔方程分解为两个独立的方程，分别描述粒子在$x<0$和$x>0$的行为：

在$x<0$时，我们有
$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = E\psi(x)
$$

这个方程的解为
$$
\psi(x) = A e^{ikx} + B e^{-ikx}
$$
其中，$k=\sqrt{2mE}/\hbar$, $A$和$B$是待定系数。

在$x>0$时，我们有
$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = E\psi(x)
$$

这个方程的解为
$$
\psi(x) = C e^{ikx} + D e^{-ikx}
$$
其中，$C$和$D$是待定系数。

由于波函数必须在$x=0$处连续，我们有
$$
A + B = C + D \tag{1}
$$

另外，由于δ函数在$x=0$处的特性，我们有
$$
\frac{\hbar^2}{2m}(\psi'(0^+)-\psi'(0^-))=V_0\psi(0)
$$
这可以改写为
$$
ik(C-D) - ik(A-B) = \frac{2m V_0}{\hbar^2}(A+B) \tag{2}
$$

从上述两个方程中，我们可以解出待定的系数。然后，我们可以通过插入粒子的能量$E$，求解出粒子的波函数$\psi(x)$。

总

的来说，δ-函数势阱或势垒在量子力学中是一个非常重要的模型，它可以帮助我们理解粒子在特定条件下的行为。例如，一个δ-函数势垒可以模拟一个突然的能量改变，例如一个电子遇到一个原子核；而一个δ-函数势阱可以模拟一个电子被一个原子核束缚的情况。

希望这个回答对你有所帮助！