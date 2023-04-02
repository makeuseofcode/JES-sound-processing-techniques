# Change volume  
def changeVolume(vol): 
  file = pickAFile() 
  if file != None and file.endswith(".wav"):
    sound = makeSound(file)
    
    for i in range(0, getLength(sound)):
      if vol == 'up':
        sampleVal = getSampleValueAt(sound, i)
        setSampleValueAt(sound, i, sampleVal*2)
        
      if vol == 'down':
        sampleVal = getSampleValueAt(sound, i)
        setSampleValueAt(sound, i, sampleVal/2)  
        
    explore(sound)
  else:
    print("Invalid file selected. Please choose a valid WAV file.")
  

# Reverse a sound
def reverseSound():
  file = pickAFile() 
  if file != None and file.endswith(".wav"):
    sound = makeSound(file) 
    newReversedSound = makeEmptySound(getLength(sound))
    for i in range(0, getLength(newReversedSound)):
      sampleVal = getSampleValueAt(sound, getLength(sound)-1-i)
      setSampleValueAt(newReversedSound, i, sampleVal)
    
    explore(sound)
    explore(newReversedSound)
  else:
    print("Invalid file selected. Please choose a valid WAV file.")
  
 
# Joins 2 Sounds together
def joinSounds():
  file1 = pickAFile() 
  if file1 == None or not file1.endswith(".wav"):
    print("Invalid file selected. Please choose a valid WAV file.")
    
  file2 = pickAFile() 
  if file2 == None or not file2.endswith(".wav"):
    print("Invalid file selected. Please choose a valid WAV file.")
    
  sound1 = makeSound(file1) 
  sound2 = makeSound(file2) 
  
  newSoundLength = getLength(sound1)+getLength(sound2)
  joinedSound = makeEmptySound(newSoundLength)
  
  # Copy the first sound onto the new longer sound clip
  for i in range(0, getLength(sound1)):
    sampleVal = getSampleValueAt(sound1, i)
    setSampleValueAt(joinedSound, i, sampleVal)
  
  # Copy the second sound  
  for i in range(0, getLength(sound2)):
    sampleVal = getSampleValueAt(sound2, i)
    endOfFirstSound = getLength(sound1)-1
    setSampleValueAt(joinedSound, endOfFirstSound+i, sampleVal) 
    
  explore(joinedSound)
  
   





