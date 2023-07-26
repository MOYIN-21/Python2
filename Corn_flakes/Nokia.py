print("1. Phone book", "\n2. Messages", "\n3. Chat", "\n4. Call register", "\n5. Tones", "\6. Settings", "\n7. Call divert", "\n8. Games", "\n9. Calculator", "\n10. Remainder", "\n11 .Clock", "\n12. Profile", "\n13. SIM services")
User = int(input('Press a number: '))
if User == 1:
    print("1. Search", "\n2. Service Nos", "\n3. Add name","\n4. Erase", "\n5. Edit", "\n6. Assign tone", "\n7. Send b’card", "\n8. Options", "\n9. Speed dial", "\n10. Voice tags")
    User = int(input("Enter a number: "))
    if User == 8:
        print("1. Type of view", "\n2. Memory status")
    else:
        print("Enter the correct integer: ")
elif User == 2:
    print("1. Write messages","\n2. Inbox", "\n3. Outbox", "\n4. Picture messages", "\n5. Templates", "\n6. Smileys", "\n7. Message settings", "\n8. Info service", "\n9. Voice mailbox", "\n10. Service command editor")
    User = int(input("Enter a number: "))
    if User == 7:
        print("1. Set", "\n2. Common")
        User = int(input("Enter a number: "))
        if User == 1:
            print("1. Message centre number", "\n2. Messages sent as", "\n3. Message validity")
        elif User == 2:
            print("1. Delivery reports", "\n2. Reply via same centre", "\n3. Character support")
elif User == 4:
    print("1. Missed calls", "\n2. Received calls", "\n3. Dialled numbers", "\n4. Erase recent call lists", "\n5. Show call duration", "\n6. Show call cost", "\n7. Call cost settings", "\n8. Prepaid credit")
    User = int(input("Enter a number: "))
    if User == 5:
        print("1. Last call duration", "\n2. All calls’ duration", "\n3. Received calls’ duration", "\n4. Dialled calls’ duration","\n5. Clear timers")
    elif User == 6:
        print("1. Last call cost", "\n2. All calls’ cost", "\n3. Clear counters")
    elif User == 7:
        print("1. Call cost limit", "\n2. Show costs in")
elif User == 5:
    print("1. Ringing tone", "\n2. Ringing volume", "\n3. Incoming call alert", "\n4. Composer", "\n5. Message alert tone", "\n6. Keypad tones", "\n7. Warning and game tones", "\n8. Vibrating alert", "\n9. Screen saver")
elif User ==6:
    print("1.Call settings", "\n2.Phone settings", "\n3.Security settings", "\n4.Restore factory settings")
    User = int(input("Enter a number: "))
    if User ==1:
        print("1. Automatic redial", "\n2. Speed dialling", "\n3. Call waiting options", "\n4. Own number sending", "\n5. Phone line in use", "\n6. Automatic answer")
    elif User ==2:
        print("1. Language", "\n2. Cell info display", "\n3. Welcome note", "\n4. Network selection", "\n5. Lights2", "\n6. Confirm SIM service actions")
    elif User == 3:
        print("1. PIN code request","\n2. Call barring service", "\n3. Fixed dialling", "\n4. Closed user group", "\n5. Phone security", "\n6. Change access codes")
elif User =="11":
    print("1. Alarm clock", "\n2. Clock settings", "\n3. Date setting", "\n4. Stopwatch", "\n5. Countdown timer", "\n6. Auto update of date and time")





# print(10, 20, 30, 40, sep= " ")
# print(10, 20, 30, 40, sep= " , ")
# print(10, 20, 30, 40)
# print(10, 20, 30, 40, end= " ")
# print(10, 20, 30, 40, end= " , ", sep=" , ")
#
#
#
#
#

