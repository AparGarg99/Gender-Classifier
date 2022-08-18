""" Clean up names and gender, and turn into numerical representation """
def preprocess(names_genders, train=True):

  # Step 0: delete non-alphabetical characters from 'name' column
  names_genders['name'] = names_genders['name'].str.replace(r'[^a-zA-Z]', '', regex=True)

  # Step 1: Lowercase
  names_genders['name'] = names_genders['name'].str.lower()

  # Step 2: Split individual characters
  names_genders['name'] = [list(name) for name in names_genders['name']]

  # Step 3: Pad names with spaces to make all names same length
  name_length = 50
  names_genders['name'] = [
      (name + [' ']*name_length)[:name_length] 
      for name in names_genders['name']
  ]

  # Step 4: Encode Characters to Numbers
  names_genders['name'] = [
      [
          max(0.0, ord(char)-96.0) 
          for char in name
      ]
      for name in names_genders['name']
  ]
  if train:
      # Step 5: Encode Gender to Numbers
      # 0 or 1
      names_genders['gender'] = [
          0.0 if gender=='F' else 1.0 
          for gender in names_genders['gender']
      ]

  return names_genders