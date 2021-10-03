function z = surf_3d(n_x,n_y,x)
    L = 1;
    z = (2/L)*sin(n_x*pi*x/L).*sin(n_y*pi*x/L);
end