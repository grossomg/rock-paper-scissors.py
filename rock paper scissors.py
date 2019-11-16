import random

rock = 1
paper = 2
scissors = 3


win = 0
loss = 0

history = []

while True:
  
  
  
    choice = input('rock paper or scissors?')
    
    print(choice)

    if len(history) < 3:
      value = random.randint(1, 3)
      #print(history)
    else:
      print(history)
      prediction = history.pop(0)
      
      if prediction == 1:
        value = 2
      if prediction == 2:
        value = 3
      if prediction == 3:
        value = 1


    if choice == 'rock':
      history.append(1)
    if choice == 'paper':
      history.append(2)
    if choice == 'scissors':
      history.append(3)


    print(value)
    
    if choice == 'rock' and value == rock:
      print('tie')
      print('win:' + str(win))
      print('loss:' + str(loss))
      
      

    elif choice == 'rock' and value == 2:
      print('loss')
      loss = loss + 1
      print('win:' + str(win))
      print('loss:' + str(loss))
      

    elif choice == 'rock' and value == 3:
      print('win')
      win = win +1
      print('win:' + str(win))
      print('loss:' + str(loss))

    elif choice == 'scissors' and value == 1:
      print('loss')
      loss = loss + 1
      print('win:' + str(win))
      print('loss:' + str(loss))
      

    elif choice == 'scissors' and value == 3:
      print('tie')
      print('win:' + str(win))
      print('loss:' + str(loss))
      

    elif choice == 'scissors' and value == 2:
      print('win')
      win = win +1
      print('win:' + str(win))
      print('loss:' + str(loss))

    elif choice == 'paper' and value == 2:
      print('tie')
      print('win:' + str(win))
      print('loss:' + str(loss))
      

    elif choice == 'paper' and value == 3:
      print('loss')
      loss = loss + 1
      print('win:' + str(win))
      print('loss:' + str(loss))
      

    elif choice == 'paper' and value == 1:
      print('win')
      win = win +1
      print('win:' + str(win))
      print('loss:' + str(loss))

    elif choice == 'exit':
      break
