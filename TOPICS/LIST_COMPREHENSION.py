# THIS FORMAT WILL BE FOLLOWED WHEN DOING THIS

# variable_name = [(the_OUTPUT_u_want_to_get) for i in range(the_value_upto_before_this_will_work) (condition)]
nums = [-2, -1, -4, -4, 1, 5, 6]
nums = [0 if val < 0 else val for val in nums]
print(nums)