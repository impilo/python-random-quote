def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt","a")
  f.write("My new quote added here")
  f.close();

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #print(quotes[0], end='')
  #print(quotes[15])
  
  for x in quotes:
      print(x, end='')

if __name__== "__main__":
  primary()
