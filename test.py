import function as cm

i = 1
# Open the file once outside the loop for better performance
with open("shielding_const.txt", "a") as file:
    while i <= 118:
        result = cm.shealding_constant(i)
        file.write(str(result) + "\n") 
        i += 1  # Increment to avoid infinite loop
                                                    
