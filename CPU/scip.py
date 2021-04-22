import os


for i in range(1,15):
    os.system('./CPUBenchmark '+str(i)+'00000000 '+str(1)+' > 0'+str(i)+'ioflo1')
    os.system('./CPUBenchmark '+str(i)+'00000000 '+str(2)+' > 0'+str(i)+'ioflo2')
    os.system('./CPUBenchmark '+str(i)+'00000000 '+str(4)+' > 0'+str(i)+'ioflo4')
    os.system('./CPUBenchmark '+str(i)+'00000000 '+str(8)+' > 0'+str(i)+'ioflo8')

