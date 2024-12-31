import logging
import datetime

def log(event):
    init=True
    
    if init==True:
        x = datetime.datetime.now()
        filename=str(x.year)+"_"+str(x.month)+"_"+str(x.day)+"_"+str(x.hour)+"_"+str(x.minute)+"_"+str(x.second)+".log"
        logging.basicConfig(filename=filename,format='%(asctime)s %(message)s', filemode='w')
        logger=logging.getLogger()

        logger.setLevel(logging.INFO)
        init=False
        
    if init==False:
        logger.info(event)
