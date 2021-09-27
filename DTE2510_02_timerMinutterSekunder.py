

def format(seconds):

    sec = seconds%60

    minu = ((seconds-sec)//60)%60

    hour = (seconds)//3600

    print(f'{hour}:{minu}:{sec}')

format(int(input("Legg inn antall sekunder som skal konverteres: ")))