#waktu tanggal pembuatan adalah 3 Februari 2020
#by Chelseano Putra
#masih ada yang salah
#edit g bisa
try:
    import os, time
    from datetime import datetime
    a = str(datetime.today())
    
    
    #for date in a[:10]:
       # print(date, end = '')
    
    aksi = open('aksi.txt','r')
    akread = aksi.read()
    reaksi = open('reaksi.txt','r')
    reakread = reaksi.read()

    
#list        
    ans = [i for i in akread.split('/')]
    jwb = [i for i in reakread.split('/')]

    print('perintah yang dapat diberikan saat chat:')
    
    for loop in enumerate(ans,start = 1):
        print(str(loop))
    print()
    print('''perintah spesial saat chat:
1. open chrome (jika chrome sudah dimasukan sebagai bagian dari environment PATH)
2. play osu (jika osu sudah dimasukan kedalah environment PATH)
3. ngedit(jika pilihan software editing sudah diimasukan kedalam environment PATH)
00. untuk perkembangan selanjutnya silahkan ditunggu :)''') 

       
    print('============================================================')

    
#petunjuk    
    a = ('''   ]perintah[
    ketik (?) untuk melihat perintah
    ketik (+) untuk menambahkan keyword
    ketik (exit) untuk memberhentikan program
    ketik (chat) untuk memulai chat
    masuk kedalam chat dahulu agar dapat memberi perintah
    agar bot tidak salah merespon maka jangan typo saat sedang chat''')
    print()
    print('ENJOY !!!')
    print(a)

    
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
                os.system('python chat.py')
                exit()

            elif inp == 'exit':
                break
            elif inp == 'chat':
                chat()



#chat
    def chat():
        try:
            print('masuk ke tempat chat. .');time.sleep(2)
            print('silahkan . . .')
            
            while True:
                inp = input('me   : ')
                if 'chrome' in inp:
                    print('yuvi :ok . . . siap. proses membuka',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.')
                    os.system('chrome htpps://www.google.com/')
                    print()
                    print()
                    continue

                elif 'ngedit' in inp:
                    p = input('yuvi :tuan mau corel atau photoshop? ')
                    if p == 'corel':
                        print('yuvi :ok . . . siap. proses membuka',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.')
                        os.system('CorelDRW')
                        print()
                        print()
                        continue
                    elif p == 'photoshop':
                        print('yuvi :ok . . . siap. proses membuka',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.',end = ' ')
                        time.sleep(1)
                        print('.')
                        os.system('PhotoshopCS6')
                        print()
                        print()
                        continue
                    else:
                        print('yuvi :jawaban yang kamu berikan belum tersedia :v. Coba lagi . . ')
                        chat()
                elif 'osu' in inp:
                    print('yuvi :ok . . . siap. proses masuk',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.',end = ' ')
                    time.sleep(1)
                    print('.')
                    os.system('osu!')
                    print()
                    print()
                    continue
                elif 'tangal' in inp or 'tgl' in inp:
                    print('yuvi :tanggal sekarang adalah:')
                    tgl()
                elif 'print' in inp:
                    txt = inp[7:-2]
                    print('yuvi :'+txt)
                    continue
                
                elif inp == 'exit':
                    print()
                    print()
                    print('memasuki menu utama',end = ' ')
                    time.sleep(1)
                    print('.', end = ' ')
                    time.sleep(1)
                    print('.', end = ' ')
                    time.sleep(1)
                    print('.')
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
                akrep.write('/'+aprep)
                
                apqrep = input('masukan respon untuk bot: ')
                reakrep = open('reaksi.txt','a')
                reakrep.write('/'+apqrep)

                akrep.close()
                reakrep.close()
                print('fitur telah ditambahkan . . . program direstart',end = ' ')
                print('.',end = ' ')
                print('.')
                os.system('python chat.py')
                exit()
        aksi.close()
        reaksi.close()
        
    def tgl():
        tanggal = str(datetime.today())
        print('      ',end = '')
        for date in tanggal[:10]:
            print(date, end = '')
        print()


    
except ValueError:
    print('mungkin input yang kamu berikan salah . . :(')
    print('kembali ke menu awal')
    menu()




menu()
print()
print('Terimakasih telah menggunakan program ini . . .')
print('''







''')
