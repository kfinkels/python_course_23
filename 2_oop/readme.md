# **Running Notebook**

`jupyter lab`

# **Reference**

`https://jupyter.org/`


# **OOP**


* Create a deck of cards class.  Internally, the deck of cards should use another class, a card class.  
The requirements are:

    > * The Deck class should have a deal method to deal a single card from the deck
    > * Use Data Class
    > * After a card is dealt, it is removed from the deck.
    > * When you create the deck, make sure the deck has all 52 cards and then rearrange them randomly. (HINT: you can use 'from random import shuffle')
    > * The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    > * Execution:
    ```
        deck = Deck()
        cards = set()
        for i in range(52):
            cards.add(deck.deal())
        print(len(cards))
    ```
    > * Output: 
        52

# **Special Methods**

* Implement an iterator (class) for looping over a sequence (string\list) backward. 
  > * Execution:
  ```
      rev = Reverse('spam')
      for char in rev:
          print(char)
  ```
  > * Output:
  ```
      m
      a
      p
      s
  ```

# **Context Manager**

* Implement a Timer context manager class that will print the time it takes to do a code block. 
  > * Execution:
  ```
      with(Timer()):
          for i in range(1000):
              pass
  ```
  > * Output:
      0.000000052

