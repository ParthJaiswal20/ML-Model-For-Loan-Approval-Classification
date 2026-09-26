data = True
line = 1
# OPENING THE FILE USING THE with KEYWORD SUCH 
# THAT I DONT HAVE TO CLOSE IT MANNUALY
with open("demo.text", "r") as f:
    # GOING TO READ LINE BY LINE , thats why
    # USING THE LOOP TO PERFORM THE TASK
    while data:
        data = f.readline()
        if ("parth" in data):
            print("parth words was found at the line number", line)
            # AS AFTER FINDING I WANT
            # TO COME OUT IF IT IS THERE
            break
        line += 1
