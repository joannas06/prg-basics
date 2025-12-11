import queue

# Creates a queue of files to print
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        file_name = input('Enter file name to print: ')
        # Add new file to the end of the queue using .put()
        files_to_print.put(file_name)
        print(f"File '{file_name}' has been added to the print queue.")

    elif menu == '2':
        # Check if queue is not empty before trying to print
        if not files_to_print.empty():
            # Get the file from the front of the queue using .get()
            file_to_print = files_to_print.get()
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('The print queue is empty. There is nothing to print.')

    elif menu == '0':
        print("Exiting printer manager.")
        break
        
    print("-" * 20) # Just a separator for readability