#!/usr/bin/env python
# coding: utf-8

# In[37]:


#For the RA: Execute this code to figure out the order of the tests at the beginning of the session. 

#This creates a list of the possible tasks. The word list task file 1 will always be fun first and word list task file 2
#will always be run last. Please refer to the experimental protocol for more detail.

import random as ran
import smtplib

current_participant = ": Saul Quintero" #<- Type in the name of the current participant in between the quotation marks
email_subject_line = "Multisensory Training Project Order"+str(current_participant)

sifi = "sifi"
mcgurk = "mcgurk"
speech = "speech"
digitspan = "digitspan"
reading = "reading"

order_of_tasks = [sifi, mcgurk, reading, speech, digitspan]

ran.shuffle(order_of_tasks)

current_participant_order = "This is the order of the tasks for " +str(current_participant)+ " "+ str(order_of_tasks)
current_participant_order_email = ("This is a message relating to the multisensory training project. This is the order of the tasks for " +str(current_participant)+ " "+ str(order_of_tasks))

from email.mime.text import MIMEText

fromx = 'multisensorytrainingproject@gmail.com'
to  = 'multisensorytrainingproject@gmail.com'
msg = MIMEText(str(current_participant_order_email))
msg['Subject'] = str(email_subject_line)
msg['From'] = fromx
msg['To'] = to

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.ehlo()
server.login('multisensorytrainingproject@gmail.com', 'shams10101')
server.sendmail(fromx, to, msg.as_string())
server.quit()

#Below you should see the order of the tasks in the square brackets as an example. 
#Because we need to know the order of the tasks for the post-test, this code also
#automatically sends an email to Saul with the details.

print(current_participant_order)


# In[ ]:




