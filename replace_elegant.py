user_comment = "NGL, i just loved the moviee...... excellent work !!!"

print(f"input string: {user_comment}")

clean_comment = user_comment #copy the string in new variable, we'll store the result in this variable

# define list of punctuation to be removed
punctuation = ['.','.','!']

# iteratively remove all occurrences of each punctuation in the input
for p in punctuation:

    clean_comment = clean_comment.replace(p,'') #not specifying 3rd param, since we want to remove all occurrences

print(f"clean string: {clean_comment}")