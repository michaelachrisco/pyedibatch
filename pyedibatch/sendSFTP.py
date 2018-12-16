import pysftp


class SendSFTP:
    # TODO: Cred class!
    # myHostname = "yourserverdomainorip.com"
    # myUsername = "root"
    # myPassword = "12345"

    def __init__(self, myHostName, myUsername, myPassword):
        self.myHostname = myHostName
        self.myUsername = myUsername
        self.myPassword = myPassword

#TODO: Take a look at the proper way to initialize this and create try/catch!
    def run(self):
        with pysftp.Connection(host=self.myHostname, username=self.myUsername, password=self.myPassword) as sftp:
            print
            "Connection successfully established ... "

            # Define the file that you want to upload from your local directory
            # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
            localFilePath = './TUTORIAL2.txt'

            # Define the remote path where the file will be uploaded
            remoteFilePath = '/var/integraweb-db-backups/TUTORIAL2.txt'

            sftp.put(localFilePath, remoteFilePath)
