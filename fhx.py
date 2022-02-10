import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('LOGIN : raydennewbiejr@gmail.com/n
PASSW : HujAi88uajjai8iaHTyhURSJL==/n
START : Pekanbaru/Riau/Sungai Siak/n
END   : Jawa Barat/Kuningan/n
DEVICE: Infinix HOT 10s/n
NEW DE: Oppo CPH2083/n
')
