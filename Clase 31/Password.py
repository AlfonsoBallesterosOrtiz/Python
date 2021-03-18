import random

def newpassword():

    capital = ['A',	'B',	'C',	'D',	'E',	'F',	'G',	'H',	'I',	'J',	'K',	'L',	'M',	'N',	'O',	'P',	'Q',	'R',	'S',	'T',	'U',	'V',	'W',	'X',	'Y',	'Z']
    lower = ['a',	'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z']
    simbol = ['!', '@','#','$', '%', '&', '/','*']
    number = ['1',	'2',	'3',	'4',	'5',	'6',	'7',	'8',	'9',	'0']

    carac = capital + lower + simbol + number

    password = []

    for i in range(8):
        carac_random = random.choice (carac)
        password.append (carac_random)

    password = "".join(password)
    return password

    
    # print (carac)

def run():
    password = newpassword()
    print ('Tú nueva constraseña es: ' + password )




if __name__ == '__main__':
    # newpassword ()
    run ()