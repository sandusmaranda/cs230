---
layout: default
---


# Homework 6, Part A: Doubly Linked Lists

Here, you will create your own implementation of a doubly linked list.
A doubly linked list is a linked list in which every node maintains a reference to the item next in the list,
**as well as** the item previous in the list:

<center>
<img src="https://miro.medium.com/v2/resize:fit:1230/format:webp/1*5wRMqVjLatOGX88VrZgacA.jpeg" />
</center>


## Task 0: Getting Settled

Copy over the `LinearList<T>` interface from the [in-class exercise](/linked-lists).
Your linked list should implement this interface.


## Task 1: Doubly Linear Node

Create a class, `DoublyLinearNode<T>`, to represent a node in your linked list.
You can follow the `LinearNode` from the [in-class exercise](/linked-lists) for inspiration.


## Task 2: Implementing the Doubly Linked list

Create a class, `DoublyLinkedList<T>` that uses your `DoublyLinearNode<T>` to implement the `LinearList<T>` interface.
Before implementing each method, **draw a memory diagram** to make sure you know what pointer manipulations you plan to use.
You may find it helpful to draw multiple versions of these memory diagrams corresponding to lists of various sizes.

Additionally, in your implementation, please:
* Store both a reference to the front of the list **and the rear**.
* Update these references appropriately when inserting/removing.
* Use the reference to rear for fast get/insertion/removal from the very end of the list (i.e. if someone wants to operate on the last element of the list, they shouldn't have to iterate over the whole list to find it).

**Hints:** For both *insert* and *remove*, you may want to break your code into several cases:
* When the list is empty
* When removing from a list of size 1
* When inserting/removing at the front
* When inserting/removing at the rear


## Task 3: Testing

Please test your `DoublyLinkedList<T>` in a main method belonging to the same class.
You can save your tests in `DoublyLinkedListTests.txt`.
There's no need to test your `DoublyLinearNode<T>`.



<br/>

# Homework 6, Part B: Merge-Sorting a Linked List

In this assignment, we will walk you through implementing merge sort for a linked list.
In addition to the coding problems, we ask you to answer **open-response questions** and submit your answers in a file called `Answers.txt`.


<br/>


## Task 0: Creating your BlueJ project

Create a BlueJ project with the following starter code.

`LinearList.java`:
```java
public interface LinearList<T> {
    public boolean isEmpty();
    public int size();
    public T get(int position);
    public void insert(int position, T element);
    public T remove(int position);
    public String toString();
}
```

`LinearNode.java`:
```java
public class LinearNode<T> {
   private LinearNode<T> next;
   private T element;

   public LinearNode() {
      next = null;
      element = null;
   }

   public LinearNode(T elem) {
      next = null;
      element = elem;
   }

   public LinearNode<T> getNext() {
      return next;
   }

   public void setNext(LinearNode<T> node) {
      next = node;
   }

   public T getElement() {
      return element;
   }

   public void setElement(T elem) {
      element = elem;
   }
}
```

`LinkedList.java`:
```java
public class LinkedList<T> implements LinearList<T> {
    protected LinearNode<T> front;
    protected int count;
    
    public LinkedList() {
        this.front = null;
        this.count = 0;
    }
    
    public boolean isEmpty() {
        return this.count == 0;
    }
    
    public int size() {
        return this.count;
    }

    protected LinearNode<T> getNode(int position) {
        if (position < 0 || position >= this.count) {
            throw new RuntimeException(
                "Asking for element at index " + position 
                + " in a list of size" + this.count
            );
        }
        
        LinearNode<T> current = this.front;
        for (int i = 0; i < position; i++) {
            current = current.getNext();
        }
        
        return current;
    }
    
    public T get(int position) {
        LinearNode<T> node = this.getNode(position);
        if (node == null) {
            return null;
        }
        
        return node.getElement();
    }
    
    public void insert(int position, T element) {
        LinearNode<T> node = new LinearNode<T>(element);
        
        if (position == 0) {
            node.setNext(front);
            front = node;
        } else {
            LinearNode<T> before = this.getNode(position - 1);
            node.setNext(before.getNext());
            before.setNext(node);
        }
        
        this.count++;
    }
    
    public T remove(int position) {
        LinearNode<T> current;
        if (position == 0) {
            current = front;
            front = front.getNext();
        } else {
            LinearNode<T> before = this.getNode(position - 1);
            current = before.getNext();
            before.setNext(current.getNext());
        }  
        
        this.count--;
        return current.getElement();
    }

    public String toString() {
        String s = "[ ";
        
        LinearNode<T> current = this.front;
        for (int i = 0; i < this.size(); i++) {
            s += current.getElement().toString() + ", ";
            current = current.getNext();
        }
        
        return s + "]";
    }
}
```

Then, answer:
* Which instance variables/methods are `protected`?
* Why would we choose to make them `protected` instead of `private` for this assignment?


<br/>

## Task 1

**Instructions.** Create a class, `SortableLinkedList`, with the following header:

```java
public class SortableLinkedList<T extends Comparable<T>> extends LinkedList<T> {
  ...
}
```

This is the class in which you will implement your sortable linked list.

**Answer.**
* What does each part of the syntax in the class header mean?
* Why do we mention `Comparable<T>` in the class header?





<br/>

## Task 2

**Instructions.** Implement a helper method with the following header:
```java
private SortableLinkedList<T> split() {
  ...
}
```

This method cuts `this` linked list into two halves.
The left half should remain in `this`, while the right half should be returned as its own linked list.
This method should take no more than O(N) time.

**Tests.** After implementing this method, **test it** in the `main` method of the same file.
You can store the results of all of your testing in `SortableLinkedlistTesting.txt`.
We highly recommend you **do not** continue without confidence this method words correctly.




<br/>

## Task 3

**Instructions.** Implement a helper method with the following header:
```java
private void reverse() {
  ...
}
```

As the name suggests, this method should reverse the order of the nodes in the linked list.
This method should take no more than O(N) time.

**Hint.** You should be able to do this with a single while loop and without any additional data structures.
If you wish, you may use a Queue or Stack from the Java API (only using the appropriate methods).

**Tests.** As before, after implementing this method, **test it** in the `main` method of the same file.
We highly recommend you **do not** continue without confidence this method words correctly.



<br/>

## Task 4

**Instructions.** Implement a helper method with the following header:
```java
private void merge(SortableLinkedList<T> right) {
  ...
}
```

This method takes in a second linked list, `right`, and merges into `this` linked list, using merge-sort's merge algorithm.
This method should take no more than O(N) time.

**Hints.**
* You may want to create a **new linked list** to contain the merged elements. Then, you can assign its contents to `this`.
* You should do this **without** any pointer manipulation, only relying on other methods of the linked list.
* Consider using the helper methods you've already implemented.

**Tests.** As before, after implementing this method, **test it** in the `main` method of the same file.
We highly recommend you **do not** continue without confidence this method words correctly.



<br/>

## Task 5

**Instructions.** Finally, implement merge sort:
```java
public void sort() {
  ...
}
```

**Hint.** Every helper method above you haven't yet used will be helpful here.

**Tests.** Don't forget to test your sorting algorithm!
For ease of checking your code, you may want to sort something simple, like integers, instead of strings:
```
SortableLinkedList<Integer> l = new SortableLinkedList<Integer>();
l.insert(0, 0);
...
```



<br/>



# Submission Checklist

* You submitted **all** `.java` files and all `.txt` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.




<!--


# Homework 6: Stacks and Linked Lists


## Learning Goals

* Gaining experience with using multiple implementations for the same task
* Work with [Java's Stack class](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html)
* Work with [Java's LinkedList class](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html)
* Think about time complexity and compare different programs based on it

## Three ways to store a collection

### Task 1: CDcollection using a Stack and a LinkedList

Recall the very first collection we saw in this class, the `CDcollection`. It uses an array to keep track of the `CD`s in someone's possession. A client program, `Tunes`, acts as a driver for the `CDcollection`. In this exercise you will write two more implementations for managing a collection of CDs:
  1. `CDcollection_Stack`, which will use a Stack to manage the collection, and
  2. `CDcollection_LinkedList` which will use a LinkedList to do so.

Create a BlueJ project, adding the three files below to it. Review the code to refresh your memory on how the application works.

`CD.java`:
```java
//********************************************************************
//  CD.java       Java Foundations
//
//  Represents a compact disc.
//********************************************************************

import java.text.NumberFormat;

public class CD
{
   private String title, artist;
   private double cost;
   private int tracks;

   //-----------------------------------------------------------------
   //  Creates a new CD with the specified information.
   //-----------------------------------------------------------------
   public CD (String name, String singer, double price, int numTracks)
   {
      title = name;
      artist = singer;
      cost = price;
      tracks = numTracks;
   }

   //-----------------------------------------------------------------
   //  Returns a string description of this CD.
   //-----------------------------------------------------------------
   public String toString()
   {
      NumberFormat fmt = NumberFormat.getCurrencyInstance();

      String description;

      description = fmt.format(cost) + "\t" + tracks + "\t";
      description += title + "\t" + artist;

      return description;
   }
}
```

`CDCollection.java`:
```java
//********************************************************************
//  CDCollection.java       Java Foundations
//
//  Represents a collection of compact discs.
//********************************************************************

import java.text.NumberFormat;

public class CDCollection
{
   private CD[] collection;
   private int count;
   private double totalCost;

   //-----------------------------------------------------------------
   //  Constructor: Creates an initially empty collection.
   //-----------------------------------------------------------------
   public CDCollection ()
   {
      collection = new CD[100];
      count = 0;
      totalCost = 0.0;
   }

   //-----------------------------------------------------------------
   //  Adds a CD to the collection, increasing the size of the
   //  collection if necessary.
   //-----------------------------------------------------------------
   public void addCD (String title, String artist, double cost,
                      int tracks)
   {
      if (count == collection.length)
         increaseSize();

      collection[count] = new CD (title, artist, cost, tracks);
      totalCost += cost;
      count++;
   }

   //-----------------------------------------------------------------
   //  Returns a report describing the CD collection.
   //-----------------------------------------------------------------
   public String toString()
   {
      NumberFormat fmt = NumberFormat.getCurrencyInstance();

      String report = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
      report += "My CD Collection\n\n";

      report += "Number of CDs: " + count + "\n";
      report += "Total cost: " + fmt.format(totalCost) + "\n";
      report += "Average cost: " + fmt.format(totalCost/count);

      report += "\n\nCD List:\n\n";

      for (int cd = 0; cd < count; cd++)
         report += collection[cd].toString() + "\n";

      return report;
   }

   //-----------------------------------------------------------------
   //  Increases the capacity of the collection by creating a
   //  larger array and copying the existing collection into it.
   //-----------------------------------------------------------------
   private void increaseSize ()
   {
      CD[] temp = new CD[collection.length * 2];

      for (int cd = 0; cd < collection.length; cd++)
         temp[cd] = collection[cd];

      collection = temp;
   }
}
```

`Tunes.java`:
```java
//********************************************************************
//  Tunes.java       Java Foundations
//
//  Demonstrates the use of an array of objects.
//********************************************************************

public class Tunes
{
   //-----------------------------------------------------------------
   //  Creates a CDCollection object and adds some CDs to it. Prints
   //  reports on the status of the collection.
   //-----------------------------------------------------------------
   public static void main (String[] args)
   {
      CDCollection music = new CDCollection ();

      music.addCD ("Storm Front", "Billy Joel", 14.95, 10);
      music.addCD ("Come On Over", "Shania Twain", 14.95, 16);
      music.addCD ("Soundtrack", "Les Miserables", 17.95, 33);
      music.addCD ("Graceland", "Paul Simon", 13.90, 11);

      System.out.println (music);

      music.addCD ("Double Live", "Garth Brooks", 19.99, 26);
      music.addCD ("Greatest Hits", "Jimmy Buffet", 15.95, 13);

      System.out.println (music);
   }
}
```


**Task 1A: Prepare the Client program** (Tunes class)

Prepare the client program `Tunes` first. The client should create the same collection of CDs:
first using the array implementation of the CD collection, (as it currently is), then using the `CDcollection_Stack`, and finally using `CDcollection_LinkedList`.

When this client program executes, the output should be presented so that it is clear which part of it is produced by which implementation.

**Task 1B: CD collection using a Stack** (CDcollection_Stack class)

Define the `CDcollection_Stack` class. As said already, you have to employ a Stack to hold the CDs. Use [java's Stack class](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html) for it. (Think about: What other Stack implementations could you have used?)

Define any methods you need in order to have a well-designed Object Oriented Program. The goal is  that the client produces output identical to the original output of `Tunes`.

Run your program and compare its output with the original one.

**Task 1C: CD collection using a LinkedList** (CDcollection_LinkedList class)

Similar to the previous task, define the `CDcollection_LinkedList` class. This time the CDs will be held in a LinkedList. Use [java's LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) implementation. (Think about: What other LinkedList implementations could you have used?)

Once more, the output from the client should be identical to the two previous ones. Your client should print the very same thing three times, each time using a different implementation.

### Task 2: Complexity of the three implementations
At this point you have three different implementations for the same task: to manage a (very simple) collection of CDs.

You might be wondering "why do we need three programs all doing exactly the same thing?"

One reason might be **time complexity**: different implementations may have different running times. Then a client -depending on their specific circumstances- may choose one over another.

In a couple of paragraphs compare these three implementations. What are the pros and cons of each one? Write your thoughts in a file named `Complexity.txt`.

In another paragraph, describe what you learned from this exercise.

### How to submit your Work
Submit `Tunes.java`, `CDcollection_Stack.java`, `CDcollection_LinkedList.java` and  the `Complexity.txt` to Gradescope. You do not need to submit any prinout of the client. Don't forget to test **each one** of these Java classes.

And as always, add appropriate javadoc, including `@author` and `@version` tags!




<br/>

# Submission Checklist

* You submitted **all** `.java` files and all `.txt` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.


-->
