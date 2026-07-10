ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# List
ft_list[1] = 'World!'

# Tuple
list = list(ft_tuple)
list[1] = 'Morocco!'
ft_tuple = tuple(list)

# Set
ft_set.pop()
ft_set.pop()
ft_set.add('Hello')
ft_set.add('BenGuerir!')

# Dict
ft_dict['Hello'] = '1337BenGuerir!'

#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)