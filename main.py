class hashId():
    def initializeHash(self):
        self.ApplicationRecords = {}

    def insertAppDetails(ApplicationRecords, name, phone, country, program, status):
        data = {name,phone,country,program,status}
        ApplicationRecords = data
        print(ApplicationRecords)


    def updateAppDetails(ApplicationRecords, name, phone, country,program, status):
        data = {name,phone,country,program,status}
        for i in ApplicationRecords:
            if ApplicationRecords[i][0] == name:
                ApplicationRecords[i] = data

    def memRef(ApplicationRecords, Program):
        output = open('outputPS07Q1.txt','a')
        output.write(f'-------Application for {Program}-------\n')
        if ApplicationRecords.has_key(Program):
            print()

    def appStatus(ApplicationRecords):
        applied = 0
        rejected = 0
        approved = 0
        for i in len(ApplicationRecords):
            if ApplicationRecords[i][4] == 'Applied':
                applied+=1
            elif ApplicationRecords[i][4] == 'Rejected':
                rejected+=1
            elif ApplicationRecords[i][4] == 'Approved':
                approved+=1
            
        output = open('outputPS07Q1.txt','a')
        output.write('\n------- Application Status -------\n')
        output.write(f"Applied:{applied}\n") 
        output.write(f"Rejected:{rejected}\n") 
        output.write(f"Approved:{approved}\n") 
        output.write('------------------------------------\n')
        output.close()

    def destroyHash(ApplicationRecords):
        # ApplicationRecords.clear()
        print('DEl')


# 1. Read Data from inputfile
# 2. Insert that data to hash map
# 3. Print how many data inserted in output file
# 4. Read Instruction form prompt file
# 5. Accordingly call functions
# 6. Delete Hash map.

# Instantiating hashId Class:
t = hashId()

# Initializing Hash Map:
t.initializeHash()

# Opening input file:
input = open('inputPS07Q1.txt','r')

# Inserting data into hash map
cnt = 0
for line in input:
    words = line.split('/')
    name = words[0]
    phone = words[1]
    country = words[2]
    program = words[3]
    status = words[4]
    t.insertAppDetails(name,phone,country,program,status)
    cnt = cnt+1

# Closing input file:
input.close()

# Outputing insertion data into output file:
output = open('outputPS07Q1.txt','a')
output.write(f"Successfully inserted {cnt} applications into the system.")
output.close()

# Reading prompts from prompt file:
prompts = open('promptsPS07Q1.txt','r')
for x in prompts:
    instruction = x.split(None or ':')
    # print(instruction)
    if instruction[0] == 'Update':
        # print('Update')
        name = instruction[-1].split('/')[0]
        phone = instruction[-1].split('/')[1]
        country = instruction[-1].split('/')[2]
        program = instruction[-1].split('/')[3]
        status = instruction[-1].split('/')[4]
        t.updateAppDetails(name,phone,country,program,status)
    elif instruction == 'Program':
        print('memRef')
        program = instruction[-1]
        t.memRef(program)
    elif instruction == 'appStatus':
        print('appStatus')
        t.appStatus()

prompts.close()

t.destroyHash()
# print(t.ApplicationRecords)

