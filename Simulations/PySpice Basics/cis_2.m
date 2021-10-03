x = linspace(0,1,100);

n_1_1 = surf_3d(1,1,x);
n_1_2 = surf_3d(1,2,x); 
n_2_1 = surf_3d(2,1,x);
n_2_2 = surf_3d(2,2,x); 

figure 
plot(x,n_1_1)
title('n_x = 1, n_y = 1')
grid on

figure 
plot(x,n_1_2)
title('n_x = 1, n_y = 2')
grid on

figure 
plot(x,n_2_1)
title('n_x = 2, n_y = 1')
grid on

figure 
plot(x,n_2_2)
title('n_x = 2, n_y = 2')
grid on