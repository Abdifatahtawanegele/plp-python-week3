count = 1
total = 0

# BUG: Missing colon at end of while statement. Python requires a colon to start a loop block. Fixed by adding :
while count < 6:
    total = total + count
    count = count + 1

# BUG: Condition was count < 5 which only sums 1+2+3+4=10. Need to include 5. Fixed by changing to count < 6 (or <=5)
# BUG: Cannot concatenate string and integer with +. total is an int. Fixed by converting total to string with str() or using f-string.
print("Sum of 1 to 5 is: " + str(total))
