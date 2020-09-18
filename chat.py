#waktu tanggal pembuatan adalah 3 Februari 2020
#by Chelseano Putra
#masih ada yang salah

a = ('''   ]perintah[
    ketik (?) untuk melihat perintah
    ketik (+) untuk menambahkan keyword
    ketik (exit) untuk memberhentikan program
    ketik (chat) untuk memulai chat
    masuk kedalam chat dahulu agar dapat memberi perintah
    agar bot tidak salah merespon maka jangan typo saat sedang chat''')
print()

try:
    import os,time
    
    aksi = open('aksi.txt','r')
    akread = aksi.read()
    reaksi = open('reaksi.txt','r')
    reakread = reaksi.read()

    
#list        
    ans = [i for i in akread.split('/')]
    jwb = [i for i in reakread.split('/')]

        
#menu
    def menu():        
        while True:
            inp = input('me   : ')
            print()
            if inp == "?":
                print(a)
            elif inp == '+':
                ap = input('masukan keyword yang ingin ditambahkan: ')
                akplus = open('aksi.txt','a')
                akplus.write('/'+ap)
                
                apq = input('masukan respon untuk bot: ')
                reakplus = open('reaksi.txt','a')
                reakplus.write('/'+apq)

                akplus.close()
                reakplus.close()
                print('fitur telah ditambahkan . . . program direstart',end = ' ')
                print('.',end = ' ')
                print('.')
                os.system('python chatb0t.py')
                exit()

            elif inp == 'exit':
                break
            elif inp == 'chat':
                chat()



#chat
    def chat():
        try:
            print('masuk ke tempat chat. .  silahkan . .')
            
            while True:
                inp = input('me   : ')
                if inp == 'open chrome':
                    print('yuvi :ok . . . siap. proses membuka',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.')
                    os.system('chrome htpps://www.google.com/')
                    continue

                elif inp == 'mau ngedit dong':
                    p = input('yuvi :tuan mau corel atau photoshop? ')
                    if p == 'corel':
                        print('yuvi :ok . . . siap. proses membuka',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.')
                        os.system('CorelDRAW X7 (64-Bit)')
                        continue
                    elif p == 'photoshop':
                        print('yuvi :ok . . . siap. proses membuka',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.')
                        os.system('Adobe Photoshop CS6')
                        continue
                    else:
                        print('yuvi :jawaban yang kamu berikan salah :v. Coba lagi . . ')
                        chat()
                elif inp == 'play osu':
                    print('yuvi :ok . . . siap. proses masuk',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.')
                    os.system('osu!')
                    continue
                
                elif inp == 'exit':
                    break
                    menu()
                h = ans.index(inp)
                print('yuvi :',jwb[h])

                
        except ValueError:
            repair = input('fitur ini belum di tambahkan . . . lakukan penambahan sekarang ? ')
            if repair == 'tidak' or repair == 'N' or repair == 'n':
                chat()
            elif repair == 'ya'or repair == 'Y' or repair == 'y':
                aprep = input('masukan keyword yang ingin ditambahkan: ')
                akrep = open('aksi.txt','a')
                akrep.write('/'+ap)
                
                apqrep = input('masukan respon untuk bot: ')
                reakrep = open('reaksi.txt','a')
                reakrep.write('/'+apq)

                akrep.close()
                reakrep.close()
                print('fitur telah ditambahkan . . . program direstart',end = ' ')
                print('.',end = ' ')
                print('.')
                os.system('python chatb0t.py')
                exit()
                
    aksi.close()
    reaksi.close()


    
except ValueError:
    print('mungkin input yang kamu berikan salah . . :(')
    print('kembali ke menu awal')
    menu()




menu()
print()
print('Terimakasih telah menggunakan program ini . . .')
print('''







''')
