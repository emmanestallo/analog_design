x = linspace(0,1,100);

y_1 = waveForm(1,1,x);
y_2 = waveForm(2,1,x);
y_3 = waveForm(3,1,x);

y_sq1 = y_1.^2;
y_sq2 = y_2.^2;
y_sq3 = y_3.^2;

figure
plot(x,y_1,'r')
hold on 
plot(x,y_2,'g')
plot(x,y_3,'b') 
legend('n=1','n=2','n=3')
title('Wave Function')
grid on

figure 
plot(x,y_sq1,'r')
hold on 
plot(x,y_sq2,'g')
plot(x,y_sq3,'b') 
legend('n=1','n=2','n=3')
title('Probability Density')
grid on 