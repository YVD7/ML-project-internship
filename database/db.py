# Now Inserting data into Cassandra Database from remote 
# loaction and getting it on to the local machine

# Database Name: 
# Keyspace Name:
# Table Name:

# importing required libreries
from app_logging import App_Logger
from cassandra.auth import PlainTextAuthenticator
from cassandra.cluster import Cluster
import pandas as pd
import csv

# creating log file
logger = App_Logger('log_Files/db.log')

# Creating class for database operation
class dataBaseOperation:

    # Now defining initialized functions
    def __init__(self):

        logger.info('INFO','Trying To Connect With The DataBase')
        self.keyspace = 'concrete'

        self.table_name = 'concrete_data'

        self.client_id = 'BcJzUqXsAeNSxlNTBJDnOQei'
        
        self.client_secret = '46kiDTUQC0sqbTd1euoWQ2enSwdLWapN2RO23iK.8+h-G.t5EN4lUo3r5RRGy8S5fWMj1W2tLshRKl02Ohw9wuLx9OlqT2Zt.jRydc,9R2KDBW,E3my75O4FpZTNAKn6'

        self.cloud_config = {
            'secure_connect_bundle':r"/home/yash/project/ineuron_internship_projects/ML-project-internship/secure-connect-concrete-data.zip"
        }

        # creating the connection to the database

        auth_provider = PlainTextAuthenticator(self.client_id,self.client_secret)
        cluster = Cluster(cloud=self.cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
        logger.info('INFO','The Connection Is Created')

    # defining the function for keyspace
    def usekeyspace(self):

        try:

            logger.info('INFO','Using The Keyspace The We Created At Time of Database Creating')
            self.session.execute("USE {keyspace};".format(keyspace=self.keyspace))

            logger.info('INFO', 'The {keyspace} Is Selected'.format(keyspace=self.keyspace))

        except Exception as e:
            raise Exception(f"(useKeySpace) - Their Is Something Wrong About useKeySpace Method \n" + str(e))

    # defining the function for creating the table
    def createtable(self):

        try:

            logger.info('INFO','Table Is Creating Inside The Selected Keyspace')
            self.session.execute("USE {keyspace};".format(keyspace = self.keyspace))

            self.session.execute()

            logger.info('INFO','The Table Is Created Inside The {keyspace} With Name {table_name}'.
                        format(Keyspace=self.keyspace, table_name = self.table_name))
        except Exception as e:
            raise Exception(f"(createTable) - Their Is Something Wrong About Creating Table Method \n" + str(e))


    # defining the function for inserting the data into the table created
    def insertiontable(self):

        try:

            logger.info('INFO','Inserting The Data Into Database')
            file = "/home/yash/project/ineuron_internship_projects/ML-project-internship/trials/Concrete_Data.csv"
            with open(file, mode='r') as f:
                next(f)

                reader = csv.reader(f, delimiter='\n')
                for i in reader:

                    data = ','.join([value for value in i])

                    self.session.execute("USE {keyspace};".format(keyspace=self.keyspace))

                    self.session.execute()

                logger.info('INFO','All The Data Entered Into The {keyspace} Having Table Name {table_name}'.
                            format(keyspace=self.keyspace, table_name = self.table_name))
        except Exception as e:
            raise Exception(f"(insertiontable) - Their Is Something Wrong About Insert Into Data Method \n" + str(e))


    # defining function to get data from the database
    def getdatafromdatabase(self):

        try:


            logger.info('INFO','Trying To Get The Data From The DataBase')
            df = pd.DataFrame()

            query = "SELECt * FROM {keyspace}.{table_name};".format(keyspace=self.keyspace, table_name = self.table_name)
            for row in self.session.execute(query):

                df = df.append(pd.DataFrame([row]))

            logger.info('INFO', 'We Gathered The Data From DataBase {}'.format(df))
        except Exception as e:
            raise Exception(f"(getData) - Their Is Something Wrong About getData Method \n" + str(e))
