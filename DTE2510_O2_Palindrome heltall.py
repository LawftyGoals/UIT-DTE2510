
def reverse(number):
    reversed = ""
    for i in number:
        reversed = i + reversed
    
    return reversed

def isPalindrome(number):
    lav = 0
    hoy = int(len(number)-1)
    halv = len(number)//2
    isaPalindrome = True

    while lav < halv:
        
        if number[lav] != number[hoy]:
            isaPalindrome = False
            break
        
        lav += 1
        hoy -= 1
    
    return "Tallet er et palindrome tall!" if isaPalindrome == True else "Tallet er ikke et palindrome tall!"

def main():
    print(reverse(input("Velg et tall for å reversere den: ")))

    print(isPalindrome(input("Velg et tall for å sjekke om den er en palindrome: ")))





main()