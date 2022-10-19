class hash():
    def __init__(name,ph_no,res_country,prog_app,app_status):
        self.name = name
        self.ph_no = ph_no
        self.res_country = res_country
        self.prog_app = prog_app
        self.app_status = app_status

    def initializeHash(self):
        self.tabel = [None]

    def insertAppDetails(name,ph_no,res_country,prog_app,app_status):
        inputfile = open('inputPS07Q1.txt','w')

        inputfile.write(f"{name}/{ph_no}/{res_country}/{prog_app}/{app_status}")
        inputfile.close()

    def updateAppDetails()

        
