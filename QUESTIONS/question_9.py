numbers = (1, 2, 3, 4, 5, 6, 7, 8)

# seperate tuple creation :-
# tuple for odd numbers and even numbers
even_tuple = ()
odd_tuple = ()

# moving around the tuple to find out the odd and even numbers and then putting them in
# their respective places
for int in numbers:
    if (int % 2 == 0):
        # TUPLES CAN NOT BE MODIFIED WHEN CREATED , SO TO ADD NEW VALUES IN THIS , U HAVE TO USE THE
        # GENERAL METHOD LIKE THIS --> (adding_value , ) U HAVE TO USE THE COMMA WITH THE VALUE
        # TO BE ADDED IN THE TUPLE CREATED SUCH THAT IT IS A tuple with one element NOT JUST A
        # NUMBER 4 IN THE TUPLE
        even_tuple += (int,)
    else:
        odd_tuple += (int,)

print(even_tuple)
print(odd_tuple)
