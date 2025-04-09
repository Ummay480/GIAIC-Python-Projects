def mad_libs():

 print("Let\'s play Mad Libs! fill in the blanks with your ")

 name = input("Give me a name: ")
 place = input("Give me a place: ")
 funny_adjective = input("give me a funny_adjective: ")
 random_object = input("Give me a random_object: ")
 animal = input("Give me an animal: ")
 action_verb = input("Give me an action verb: ")
 funny_exclamation = input("Give me a funny exclamation: ")

 story = f"""
 One day, {name} went to {place}. 
 They saw a {funny_adjective} {random_object} and a {animal}.
 The {animal} started to {action_verb}!
 "{funny_exclamation}!" shouted {name}.

 """
 print("\n Here is your Mad Lib story:")
 print(story)

if __name__ == "__main__":
    mad_libs()
