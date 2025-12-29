import imaplib
import email
import DataKeeper


def read_email_from_gmail():
        #DownloadAttachment.dodwLoadAttachments()
        
        emaicontent=[]
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        email_address =DataKeeper.emailid
        email_sk = DataKeeper.securitykey
        (retcode, capabilities)=mail.login(email_address,email_sk)
        mail.list()
        mail.select('inbox')

        n=0
        (retcode, messages) = mail.search(None, '(UNSEEN)')
        
        if retcode == 'OK':
        
           for num in messages[0].split() :
              print("num ",n)
              print ('Processing ')
              n=n+1
              typ, data = mail.fetch(num,'(RFC822)') # to fetch the contents and make it read
              typ, data = mail.fetch(num,'(BODY.PEEK[])') # Just to get the content and leave it as unread
              
              
          
                       
              emailfrom=""
              emailsub=""
              emailbody=""
              for response_part in data:
               
                 if isinstance(response_part, tuple):
                     original = email.message_from_bytes(response_part[1])
        
                     print ("From: ",original['From'])
                     print ("Subject: ",original['Subject'])
                     raw_email = data[0][1]
                     raw_email_string = raw_email.decode('utf-8')
                     email_message = email.message_from_string(raw_email_string)
                     print(email_message)
                   
                     for part in email_message.walk():
                         if (part.get_content_type() == "text/plain"): # ignore attachments/html
                             body = part.get_payload(decode=True)
                             bodytxt=body.decode('utf-8')
                             emailbody=bodytxt
                         
                            
                                               # 
                     
                                     
                     emailfrom= original['From']
                     emailsub= original['Subject']
                     emaildate=original['date']
                  
                    
                     
                    
                         
                         
                     
                     print("From ID ",emailfrom)
                     print("From SUB ",emailsub)
                     print("Received Date: ",emaildate)
                     print("BODY ",emailbody)
                     print("\n ==================================\n")
                     temp=[]
                     temp.append(emailfrom)
                     temp.append(emailsub)
                     temp.append(emaildate)
                     temp.append(emailbody)
                     emaicontent.append(temp)
             
        
        return emaicontent        
                   
                     

# nothing to print here
#emaillist=read_email_from_gmail()
#for row in emaillist:
 #    print(row)
#     fromrec=row[0]
#     subject=row[1]
 #    body=row[2]
  #   print(fromrec)
   #  print(subject)
   #  print(body)
   #  print("\n ====================================================\n")
    
    
    
    
    
    
    