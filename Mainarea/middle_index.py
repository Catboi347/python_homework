def append_middle(s1, s2):
  middle_index = int(len(s1) /2)
  print("The original strings are", s1,"and", s2)
  middle_three = s1[:middle_index-1:]+ s2 +s1[middle_index-1:]
  print("The string is now: ", middle_three) 
append_middle("Dangreat", "yal is ")