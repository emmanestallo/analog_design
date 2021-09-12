gm_des = 500*(10**(-6))
gm_curr = 88.62*(10**(-6))

curr_width = 160*(10**(-9))

mult_fact = gm_des/gm_curr 
new_width = curr_width*mult_fact

print(new_width)