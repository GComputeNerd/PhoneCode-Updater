ar = '+91' # Area Code you want to add to numbers that have no area code

with open('contacts.vcf') as f: # Open Contacts File
    data = f.readlines() # Get entries into list
    for i in range(len(data)):
        entry = data[i]
        if entry[0:3] == 'TEL': # This line has a phone number
            n = entry.find(':') + 1 # Index of where number starts from
            if (entry[n] != '+'): # Number doesn't have an area code
                entry = entry[:n] + ar + entry[n:] # Add area code to number
                data[i] = entry

with open("contacts(v1).vcf", 'w') as f: # Save to new file
    for i in data:
        f.write("%s \n" % i)
