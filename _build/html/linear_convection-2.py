u,x = convection(151, 51, 0.5, 2.0, 0.5)
plot_convection(u,x,151,'Figure 1: c=0.5m/s, nt=151, nx=51')

u,x = convection(151, 1001, 0.5, 2.0, 0.5)
plot_convection(u,x,151,'Figure 2: c=0.5m/s, nt=151, nx=1001')