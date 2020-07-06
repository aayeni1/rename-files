import os 

def RenameFilesLower(path):
  my_list = []
  for file in os.listdir(path):
    if os.path.join(path, file.lower()) not in my_list and not os.path.isdir(
        os.path.join(path, file)):
      os.rename(os.path.join(path, file), os.path.join(path, file.lower()))
      my_list.append(os.path.join(path, file.lower()))
    elif os.path.join(path, file.lower()) in my_list and not os.path.isdir(
        os.path.join(path, file)):
      counter = 1
      head, ext = os.path.splitext(file)
      new_value = head + str(counter) + ext
      new_value = new_value.lower()
      if os.path.join(path, new_value) not in my_list:
        my_list.append(os.path.join(path, new_value))
        os.rename(os.path.join(path, file), os.path.join(path, new_value))
      elif os.path.join(path, new_value) in my_list:
        counter += 1
        new_value = head + str(counter) + ext
        new_value = new_value.lower()
        my_list.append(os.path.join(path, new_value))
        os.rename(os.path.join(path, file), os.path.join(path, new_value))
    elif os.path.isdir(os.path.join(path, file)):
      new_path = os.path.join(path, file)
      for sub_file in os.listdir(new_path):
        if os.path.join(new_path,
                        sub_file.lower()) not in my_list and not os.path.isdir(
                            os.path.join(new_path, sub_file)):
          os.rename(
              os.path.join(new_path, sub_file),
              os.path.join(new_path, sub_file.lower()))
          my_list.append(os.path.join(new_path, sub_file.lower()))
        elif os.path.join(new_path,
                          sub_file.lower()) in my_list and not os.path.isdir(
                              os.path.join(new_path, sub_file)):
          counter = 1
          head, ext = os.path.splitext(sub_file)
          new_value = head + str(counter) + ext
          new_value = new_value.lower()
          if os.path.join(new_path, new_value) not in my_list:
            my_list.append(os.path.join(new_path, new_value))
            os.rename(
                os.path.join(new_path, sub_file),
                os.path.join(new_path, new_value))
          elif os.path.join(new_path, new_value) in my_list:
            counter += 1
            new_value = head + str(counter) + ext
            new_value = new_value.lower()
            my_list.append(os.path.join(new_path, new_value))
            os.rename(
                os.path.join(new_path, sub_file),
                os.path.join(new_path, new_value))

  return my_list
