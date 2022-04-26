import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

dot = .2
dash = dot * 3

morse = "a.-b-...c-.-.d-..e.f..-.g--.h....i..j.---k-.-l.-..m--n-.o---p.--.q--.-r.-.s...t-u..-v...-w.--x-..-y-.--z--.."

def blink(length):
    utime.sleep(dot)
    led_onboard.value(1)
    utime.sleep(length)
    led_onboard.value(0)


def writeLetter(sequence):
    for i in sequence:
        if i == '.':
            blink(dot)
        elif i == '-':
            blink(dash)

    utime.sleep(dash)


def interpreter(letter):
    foundIndex = 0
    startIndex = 0
    endIndex = 0

    for i in range(0, len(morse) + 1):
        if morse[i] == letter and foundIndex == 0:
            foundIndex = 1
            startIndex = i+1
        elif (morse[i] != '.' and morse[i] != '-') and foundIndex == 1:
            endIndex = i
            return morse[startIndex:endIndex]


def writeSentence(sentence):
    for i in sentence:
        if i == ' ':
            utime.sleep(dash * 7)
        else:
            print(i+"\n")
            print(interpreter(i))
            writeLetter(interpreter(i))
            

sentence = "hello"
writeSentence(sentence)
