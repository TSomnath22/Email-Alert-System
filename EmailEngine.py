import time
import DataKeeper
import EmailReader
import WhatsAppSender
emailid="t.s.dahiphale@gmail.com";
email_security_key="mzdg ufsf apat hpna"
DataKeeper.setEmailData(emailid, email_security_key)
mobilenumber="+919850813254"
unique_lst=[]




while True:
    count=1
    time.sleep(5)
    print("Visited the Email ID")
    wa_str="Hi, You have Received following emails\n"
    status=0
    emaildata_list=EmailReader.read_email_from_gmail()
    for single_email in emaildata_list:
        if single_email not in unique_lst:
            status=1
            unique_lst.append(single_email)
            emailfrom= single_email[0]
            emailsub= single_email[1]
            emaildate=single_email[2]
            countstr=str(count)
            wa_str=wa_str+"Email No : ["+countstr+"]\n"
            wa_str=wa_str+"FROM :"+emailfrom+"\n"
            wa_str=wa_str+"SUBJECT :"+emailsub+"\n"
            
            wa_str=wa_str+"TIME :"+emaildate+"\n\n\n"
            count=count+1
            
    wa_str=wa_str+"Regards : Automatic Email Information System on WhatsApp \n Thank You"  
    if(status==1):
        print(wa_str)
        WhatsAppSender.sendMsgonWA(wa_str, mobilenumber)
        
    else:
        print("You have No new emails Received")  
        
    print("\n\n ==================================================================\n\n")    
    time.sleep(30)      
            

    
    
    
  