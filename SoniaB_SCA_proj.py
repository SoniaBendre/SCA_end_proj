import re

# Asks user for statement that contains profanity which needs to be removed
input_text = input("Type the statement to remove profanity from.")

# States the profanity to check for
profanity_record = "fuck|shit|bitch|ass"

# Removes all the profanity in "input_text"
profanity_removed = re.sub(profanity_record, "", input_text)

# Removes unnecessary spaces from "profanity_found"
refined_result = re.sub(" ", "", profanity_removed)

# Prints the refined_result
print(refined_result)
