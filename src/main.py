import speedtest 
import time

st = speedtest.Speedtest()
results = st.results.dict()

while True:
    try:
        print("Hello, please select an option:\n1. Download\n2. Upload\n3. Ping\n4. Other Informations")
        option = int(input("Your option: "))
        print("Processing...")
        time.sleep(3)

        if option == 1:
            print(f"Download: {st.download()/1024:.3f} Mbits/s")
        elif option == 2:
            print(f"Upload: {st.upload()/1024:3f} Mbits/s")
        elif option == 3:
            print(f"Ping: {st.results.ping}ms")
        elif option == 4:
            for k, v in results.items():
                print(f"{k} = {v}")
        else:
            print("\033[31mOption Error\033[m")

        resp = str(input("Continue? [y/n] "))
        if resp == 'y' or resp == 'Y':
            continue
        elif resp == 'n' or resp == 'N':
            break
        else:
            print("\033[31mTry again\033[m")
    except Exception as error:
        print("\033[31Try again\033[")