class ECG_Class(object):

    """This class treats a file containing ECG data as an object

    It has many associated methods that process and display this data"""

    def __init__(self, filename, avemins=1,outName="assignment02",lowerThresh=60,upperThresh=100):
        from load_data import load_data
        from HRinst import HRinst
        self.name = filename[:-4]
        self.mins = avemins
        self.outputfile = outName
        self.bradyT = lowerThresh
        self.tachyT = upperThresh
        self.data = load_data(self.name)
        self.time = self.data[:][0]
        self.voltage = self.data[:][1]
        self.instHR = HRinst(self.data)

    def avg(self):
        from take_average import average

        return average(self.instHR,self.time,self.mins)

    def brady(self):
        from tachybradycardia import bradycardia
        brady =  bradycardia(self.instHR,self.bradyT,self.tachyT)
        return brady

    def tachy(self):
        from tachybradycardia import tachycardia
        tachy = tachycardia(self.instHR, self.bradyT, self.tachyT)
        return tachy

    def output(self,filename="assignment02_output.csv"):

        """ Creates a file containing the output of these functions

        :param mins: (int) Number of minutes to take HR over
        :param filename: (str) optional name of file if you don't want
        :returns: An ndarray of average heart rate at each time point
        """

        from write_output import write_output
        if self.outputfile == "assignment02":
            oName = self.name + '_output.txt'

        ave = self.avg()
        btc = self.btc()
        b = self.brady()
        t = self.tachy()

        return write_output(self.time, self.HRinst, ave, b, t, filename)

