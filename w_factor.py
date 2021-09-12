gm_des = 500*(10**(-6))
gm_curr = 566.55*(10**(-9))

curr_width = 1*(10**(-6))

mult_fact = gm_des/gm_curr 
new_width = curr_width*mult_fact

print(new_width)