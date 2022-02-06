from time import sleep
DNS = {}
ip_list = []
def menu():
    while True:
        choice = input('please choose in the main menu:\na. IP system\nb. DNS system \nor type "exit" to quit:\n ')
        if choice == 'a':
            file_name = r'C:\files for python work\LAB10\ips.txt'
            file = open(file_name, 'r+')
            ip_str = file.read()
            file.close()
            ip_list = ip_str.split(',')
            choose = input('''1. search for ip address from a list\n2. add up address to a list\n3. delete ip address to a list\n4. print all the ips to the screen\n''')
            if choose == '1':
                search_ip = (input('please enter the ip that you want to search:\n'))
                if search_ip in ip_list:
                    print(f'the {search_ip} Found in the list')
                else:
                    print(f"the {search_ip} didn't Found in the list")
            elif choose == '2':
                add_ip = (input('please enter the ip that you want to Add:\n'))
                ip_list.extend([add_ip])
                file = open(file_name, 'r+')
                print(ip_list)
                file.write(str(ip_list))
                print(file.read())
                file.close()
            elif choose == '3':
                print(ip_list)
                delete_ip = int((input(
                    'please enter the number place of the ip that you want to Delete:\nthe counting start from zero\n')))
                ip_list.pop(delete_ip)
                print(ip_list)
                file = open(file_name, 'r+')
                file.write(str(ip_list))
                file.close()
            elif choose == '4':
                print('4444444444444444444')
                for i in ip_list:
                    print(i)
            else:
                print('choose 1 - 4 only!!!')
        elif choice == 'b':
            choose2 = input('1. search for url from a dictionary\n2. add url + ip address to a dictionary\n3. delete url from a dictionary\n4. update ip address of specific url\n5. print all the URL:IP to the screen\n')

            if choose2 == '1':
                # 1 search for url from a dictionary
                search = input('\nplease enter the url that you want to search:\n')
                if search in DNS.keys():
                    print(f'the {search} URL was found in the DNS')
            elif choose2 == '2':
                # 2 add url + ip address to a dictionary
                URL = input('\nplease enter the url:\n')
                IP = input('\nplease enter the IP of the URL:\n')
                DNS.update({URL: IP})
                print('the URL has been added successfully')
            elif choose2 == '3':
                del_URL = input(
                    '\nplease enter the url name that you want to delete:\n"Warning!!!!\t with the url the ip will also delete\n')
                del DNS[del_URL]
            elif choose2 == '4':
                update_URL = input('\nplease enter the url name that you want to update:\n')
                new_ip = input('\nplease enter the new IP of the URL:\n')
                DNS[update_URL] = new_ip
                print(DNS)
            elif choose2 == '5':
                # 5 print all the URL:IP to the screen
                print(DNS)
            else:
                print('choose 1-5 only!!!')
        elif choice == 'exit':
            break
        else:
            print('choose "a" "b" or "exit" only!!!')
            continue
menu()







