while True:
    try:
        line = input("> ")
    except:
        print("Please enter something")
    if line[0] == '#':
        continue
    if line == 'bye':
        break
    print(line)
print("Session Ended")