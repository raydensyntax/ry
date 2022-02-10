import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)

mengetik('Hai admin\nPerangkat baru terdeteksi login\n
Kedalam gmail anda, melalui CPH2803/nTerletak di jawa barat/nTepatnya di kuningan/nPada jam 13:44WIB')
