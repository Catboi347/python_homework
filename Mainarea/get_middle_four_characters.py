def get_middle_four_characters(sample_str):
  middleIndex = int(len(sample_str) /2)
  print("Original String is", sample_str)
  middle_four = sample_str[middleIndex-2:middleIndex+2]
  print("The middle four characters are: ", middle_four)  
get_middle_four_characters("goodcatsrock")
get_middle_four_characters("Carshavedoor")