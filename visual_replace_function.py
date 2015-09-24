# I can't figure out how to grab Custom UI elements from Editorial, so I'm making this simple. I'm putting them in as text in the input to the workflow as a string, splitting them up into separate values, and using those as the variables.

import workflow

values = workflow.get_input() #value order = "find-type,find-text,replace-text,case_switch"
split_values = values.split(',')

replace_cancel = bool(split_values[4])
find_type = split_values[0]
find_text  = split_values[1]
replace_text = split_values[2]
case_switch = int(split_values[3])

if replace_cancel = False:
    workflow.stop()
else:
