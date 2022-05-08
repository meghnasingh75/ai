# ALGORITHM:
# 1. Start. 
# 2. Take the GOAT first. 
# 3. Leave the LION with the CABBAGE. 
# 4. Row back and pick up the LION. 
# 5. Take the LION across and bring back the GOAT. 
# 6. Leave the GOAT and take the CABBAGE cross. 
# 7. Leave the LION with the CABBAGE. Row back and bring the GOAT. 
# 8. Everyone is now safe! 
# 9. End. 




left_elements=['M','L','G','C']
right_elements=[]
print("Before the river crossing:")
print("Elements present in the left side of the river bank:", left_elements)

while True:
  print(left_elements[1],",", left_elements[2],",", left_elements[3], ":Select any one from the list")
  i=input("Enter the item you want to take (In CAPS-ON):")
  if left_elements[1]==i and left_elements[2]=='G' and left_elements[3]=='C':
    print("Goat will eat cabbage!!")
    break
  elif left_elements[2]==i and left_elements[3]!='C':
    right_elements.append(left_elements[2])
    if len(right_elements)==2 and right_elements[0]=='G':
      left_elements[2]=right_elements[0]
      right_elements[0]=right_elements[1]
      right_elements.pop()
  elif left_elements[1]==i and left_elements[2]=='G':
   right_elements.append(left_elements[1])
   left_elements[1]=left_elements[2]
   left_elements[2]=''
  elif left_elements[1]==i and left_elements[2]=='C':
   right_elements.append(left_elements[1])
   left_elements[1]=left_elements[2]
   left_elements[2]=''
   if len(right_elements)==2 and right_elements[0]=='G':
     left_elements[2]=right_elements[0]
     right_elements[0]=right_elements[1]
     right_elements.pop()
  elif left_elements[1]==i and left_elements[2]!='C' and left_elements[2]!='G':
   right_elements.append(left_elements[1])
   right_elements.append('M')
   left_elements[1]=''
   left_elements=[]
   if len(right_elements)>4:
    print("River Crossing Unsucessfull")
    break
   print("Goal is reached!!!")
   break
  if left_elements[2]==i  and left_elements[3]=='C':
   right_elements.append(left_elements[2])
   left_elements[2]=left_elements[3]
   left_elements[3]=''
  if left_elements[3]==i:
   print("Lion will eat the Goat!!")
   break

print("After River Crossing")
print("Elements in the Left Side Bank ", left_elements)
print("Elements in the Right Side Bank ", right_elements)