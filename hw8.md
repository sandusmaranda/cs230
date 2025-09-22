---
layout: default
---

# Homework 8, Part A: Who dunn it?!

**Goals:**
* Learn how to implement HashTables
* Learn two strategies for handling hash collisions
* Continue practicing the OOP paradigm


**Pair Programming:**
We will assign you a peer to collaborate with on this assignment. Please,
* Reach out to your partner ASAP to discuss when you will meet to work on the assignment. You will probably have to meet several times.
* Work *together* (pair programming) rather than splitting the homework and working separately.
* *Discuss* the ideas and diagrams before diving into coding.


**Context:** In the fall of 2024, we, Professors Yacoby and Sandu, embarked on an epic, never-ending saga of rivalry with the world's most cunning nemesis: the west-wing scanner. It all began when it gleefully devoured the students' CS 230 midterms and spewed forth an artistic masterpiece that looked more like a 3D Rorschach tests. Thankfully, Professor Sohie Lee was around to help us turn things around. Watching her work her magic, we learned that the scanner only responds well to scented candles, words of affirmation, and lots (and lots) of encouragement. But what caused the scanner to behave like this?

Enter Professor Turbak, whose tenure in the department dates back to the early 1900s—or so the legend goes. He reminisced about a chilly winter evening in 1982, when the scanner apparently committed "unspeakable things" that still induce dramatic pauses today. His theory? The scanner was hacked!

In an effort to unravel the mystery, we enlisted the expertise of Professors Anderson and VanHattum, who helped us snag the scanner's logs, chronicling every IP address that dared whisper sweet nothings into its circuits. However, we were so traumatized by the scanner's antics that we seemed to have forgotten how to implement all data structures. Now, we desperately need your help.

If the scanner logs from 1982 reveal the same IP address as that fateful night when the midterms turned into modern art, it means our dear scanner wasn't just hacked---it was haunted by the same techno-ghost! Dust off your detective hats, because this is one glitch in the matrix you won't want to miss. Your mission, should you choose to accept it, is to determine if the same IP address was found in both logs.



<br/>

# Task 0

Create a new BlueJ project called "HashTables." In this project, create a file for the following interface:

`HashTable.java`:
```java
public interface HashTable<K, V> {
    /**
     * Inserts the specified key-value pair into the hash table. 
     * If the key already exists in the hash table, its value is updated to the specified value.
     *
     * @param key   The key with which the specified value is to be associated.
     * @param value The value to be associated with the specified key.
     */
    public void put(K key, V value);

    /**
     * Returns the value associated with the specified key, or null if the hash table contains no mapping for the key.
     *
     * @param key The key whose associated value is to be returned.
     * @return The value associated with the specified key, or null if the hash table contains no mapping for the key.
     */
    public V get(K key);

    /**
     * Returns the number of key-value mappings in the hash table.
     *
     * @return The number of key-value mappings in the hash table.
     */
    public int size();

    /**
     * Returns true if the hash table contains no key-value mappings.
     *
     * @return true if the hash table contains no key-value mappings.
     */
    public boolean isEmpty();
}
```

You will create several Hash Tables that implement this interface. Next, create a file called `Entry.java`, representing a single HashTable entry as follows. This will prove useful in your implementation of the Hash Tables.

`Entry.java`:
```java
/**
 * Represents an entry in the HashTable
 *
 * @author CS 230 Staff
 * @version Fall 2024
 */
public class Entry<K, V> {
    private K key;
    private V value;

    /**
     * Constructs an entry with the specified key and value.
     *
     * @param key   The key associated with this entry.
     * @param value The value associated with this key.
     */
    public Entry(K key, V value) {
        this.key = key;
        this.value = value;
    }

    /**
     * Returns the key associated with this entry.
     *
     * @return The key associated with this entry.
     */
    public K getKey() {
        return this.key;
    }

    /**
     * Sets the key for this entry.
     *
     * @param key The key to set for this entry.
     */
    public void setKey(K key) {
        this.key = key;
    }

    /**
     * Returns the value associated with this entry.
     *
     * @return The value associated with this entry.
     */
    public V getValue() {
        return this.value;
    }

    /**
     * Sets the value for this entry.
     *
     * @param value The value to set for this entry.
     */
    public void setValue(V value) {
        this.value = value;
    }
}
```



<br/>

# Task 1

* Create a file called `LinearProbingHashTable.java` and in it, implement a HashTable with linear probing.
* Since all Java objects extend `Object`, they all inherit a method called `hashCode` that can be used in a hash table. In your HashTable, please use the `hashCode` method of `K` as your has function. Note that this function may return a negative integer, so take the absolute value of the output of the function.
* At the bottom of the file, create a main method and use it to test your code. We recommend picking `K` to be a `String` when testing. Save the output of your tests in a file called `LinearProbingHashTable.txt` and submit it along with your code.


<br/>

# Task 2

* Create a file called `LinkedHashTable.java` and in it, implement a HashTable with separate chaining. For this class, you're welcome to use Java's `LinkedList` class.
* Add a method `public V remove(K key)` to this implementation that allows one to remove the item associated with the provided `key`. Note that this is not possible to do for a Hash Table with linear probing---can you think of why?
* As before, create a main method and use it to test your code and save the output of your testing in `LinkedHashTable.txt` to submit it along with your code.


<br/>

# Task 3

Now that you have your HashTable ready, you can start your investigation! Implement a driver class called `Detective.java` that:
* Reads in the log files from [1982](/static_files/hashtables/log-1982.txt) and [2024](/static_files/hashtables/log-2024.txt), containing the lists of IP addresses
* Uses one of your Hash Table implementations to cross references the IP addresses from 1982 with those from 2024 to find the overlap
* For the IP address that overlap, your code should report how many times the IP address appears in each log


<br/>

# Task 4

In a file called `Answers.txt`, answer:
1. Which IP address did you find? Is it a valid IP address (you may use Google to help you answer this)? 
2. How many times did it appear in the 1982 log and in the 2024 log?
3. If the log from 1982 had `N` lines and the file from 2024 had `M` lines, what's the computational complexity of your algorithm?
4. And what's the space complexity of your algorithm?


<br/>

# Submission Checklist

* You submitted **all** `.java`, `.txt` and `.pdf` files.
* Your files are named **exactly** as in the homework specification, *including file extensions*.
* You tested **every possible** pathway in your code.
* You signed every class (or file) with `@author` and `@version`, accompanied by a description of what the class does.
* You wrote javadoc for every function, which includes `@param` and `@return`.
* You wrote inline comments explaining the logic of your code.

# Homework 8, Part B: Tree Recursion
Learning Goals

    Practice recursive tree algorithms

Tasks

First, create a BlueJ project with the following starter code.

BTNode.java:

import java.util.LinkedList;

public class BTNode<T> {
    protected T element;
    protected BTNode<T> left, right;

    public BTNode(T elmt) {
        element = elmt;
        left = right = null;
    }

    public T getElement() { 
        return element; 
    }

    public void setElement(T element)
    { this.element = element; }

    public BTNode<T> getLeft() { 
        return left; 
    }

    public void setLeft(BTNode<T> left) { 
        this.left = left; 
    }

    public BTNode<T> getRight() { 
        return right; 
    }

    public void setRight(BTNode<T> right) {
        this.right = right; 
    }

    public BTNode<T> find(T target) {
        BTNode<T> result = null;

        if (element.equals(target)) {
            result = this;
        } else {
            if (left != null)
                result = left.find(target);
            if (result == null && right != null)
                result = right.find(target);
        }

        return result;
    }

    public int count() {
        int result = 1;

        if (left != null)
            result = result + left.count();

        if (right != null)
            result = result + right.count();

        return result;
    }

BSTNode.java:

public class BSTNode<T extends Comparable<T>> extends BTNode<T> {

    public BSTNode(T element) {
        super(element);
    }

    public void add(T item) {
        if (item.compareTo(element) < 0) {
            if (left == null)
                left = new BSTNode(item);
            else //  Add recursively 
                ((BSTNode) left).add(item);
        } else { //  item >= element, go right
            if (right == null)
                right = new BSTNode (item);
            else //  Add recursively 
                ((BSTNode) right).add (item);
        }
    }

    public BSTNode<T> find(T target) {
        if (target.compareTo(element) == 0)
            return this;
            
        // Since left and right are defined as BTNodes in the parent class,
        // we cast them to BSTNodes here so we can call compareTo
        BSTNode<T> l = (BSTNode<T>) left;
        BSTNode<T> r = (BSTNode<T>) right;
        
        if (target.compareTo(element) < 0 && l != null) {
            return l.find(target);
        }
            
        if (r != null) {
            return r.find(target);
        }
        
        return null;
    }
}

Next, implement the following instance methods:

    Implement public int countLeaves() in the BTNode class. This method should return an integer counting the number of leaves in tree.
    Implement public int countNodesAtLevel(int level) in the BTNode class. This method should return the number of nodes at a given level in the tree. In this method, we’ll say that level 0 represents the root.
    Implement public LinkedList<T> collectOnlyChildren() in the BTNode class. This method should return a list of all elements T that belong to nodes that have no siblings.
    Implement public boolean isValid() in the BSTNode class. This method should return true if the tree is a valid binary search tree.

Please test your code as you go, putting your test in a driver class called Driver.java.


Submission Checklist

    You submitted all .java files and all .txt files.
    Your files are named exactly as in the homework specification, including file extensions.
    You tested every possible pathway in your code.
    You signed every class (or file) with @author and @version, accompanied by a description of what the class does.
    You wrote javadoc for every function, which includes @param and @return.
    You wrote inline comments explaining the logic of your code.


<!--
# Homework 10, Part A: Hash Tables


## Goals
* Better understanding of using a Hash Table
* Designing a program on your own



## Exercise: Use Hashtables to analyze word frequencies

In this exercise, you will use a hash table to count frequencies of words in some files.


### Task 0 

Download the [DataFiles](static_files/DataFiles.zip) for testing your work.

### Task 1
Look at `WordTable_Hash.java` below. In the code, a hash table was used to count word frequencies in a single file. Go over the code, and make sure you understand it well before moving on. You should use parts of that code in the program you will write in the next step.

`WordTable_Hash.java`:
```java
import java.util.Hashtable;
import java.util.Scanner;
import java.util.Enumeration;
import java.io.File;
import java.io.IOException;

/* Read in a text file and store the number of occurrences of distinct word in the file.
 * You should use the file name and relative path as a command-line argument
 * E.g., "DataFiles/GreenEggs.txt"
 */
public class WordTable_Hash  {

    // Instance variables
    private int totalWords;
    private Hashtable<String, Integer> table;

    // Constructor
    public WordTable_Hash() {
        totalWords = 0;
        table = new Hashtable<String, Integer>();
    }

    // Instance methods
    public void readInFile(String filename) {
        try {
            Scanner reader = new Scanner(new File(filename));
            while (reader.hasNext()) {
                String word = reader.next();
                if (table.containsKey(word)) {
                    int previousCount = table.get(word);
                    table.put(word, previousCount+1);
                }
                else table.put(word, 1);
                totalWords++;
            }
            reader.close();
        } catch (IOException ex) {
            System.out.println(ex);
        }
    }

    public int getTotalWords() {
        return totalWords;
    }

    public int getNumDistinctWords() {
        return table.size();
    }

    public String toString() {
        return table.toString();
    }

    public void printKeysAndValues(){
        Enumeration contents = table.keys();
        String key;
        System.out.println("Key: \t Value: \n");
        while(contents.hasMoreElements()) {
            key = (String) contents.nextElement();
            System.out.println(key+ "\t" + table.get(key));
        }
    }

    public static void main (String[] args) throws IOException {
        if (args.length == 0)
            System.out.println("When executing this application, please enter the name of a file as a command line arguemnt.");
        else {
            long start = System.currentTimeMillis();
            WordTable_Hash wt = new WordTable_Hash();
            wt.readInFile(args[0]);
            long stop = System.currentTimeMillis();

            // Output results
            //System.out.println("The contents of the word frequency table are: ");
            //System.out.println(wt);
            System.out.println("Using WordTable_Hash");
            wt.printKeysAndValues(); // to enumerate them
            System.out.println("The file has " + wt.getTotalWords() + " words");
            System.out.println("of which " + wt.getNumDistinctWords() + " are different");
            System.out.println("Reading in file took " + (stop-start) + " milliseconds.");
        }
    } 
}
```


### Task 2
In this part, we will count word frequencies among multiple files, in particular all the files contained in a given directory (folder). The input of the program should be the name of a directory to be processed.
The output of the program should include:
* the total number of words read from **all files** in the given directory
* the number of distinct words in there, and
* the most frequent word among all files, together with its frequency.

You can iterate over the files in a directory like this:

```java
import java.io.File;

// args[0] is the name of a directory
dir= new File(args[0] + "/");

// dir points to the directory’s contents
File[]files= dir.listFiles();
System.out.println(files.length + "files");

for (File f : files) 
  if (!f.isHidden()) 
    process(f);
```    

The design of this program, i.e, what methods to have, what inputs they may take etc, is left up to you. As you design your application, remember some of the basic principals for writing code:
 * break your code into methods so that each method definition is not too long
 * code repetition (writing the some piece of code more than once) should be avoided
 * the `main()` method should be short, high-level and basically only call other methods
 * use descriptive names for methods, variables etc to improve the readability and the overall quality of your code



**Specifications:**
Please adhere to the following specifications:

* Name your program `WordFrequenciesDirectory_Hash.java`
* Your program should take the name of the folder to be processed as a **command line argument**. If no command line argument is provided by the user, the downloaded folder `DataFiles` should be used as input.
* Structure your output to look similar to this:

<pre>
Folder processed: DataFiles
Total number of words read: 1501990  
Number of distinct words: 60660
Most frequent word: the (frequency: 55965)
</pre>


### Task 3
Once you are done with the previous task, try to add some more functionality to your program:

Given a specific word, present the number of times it has repeated among all files in the directory processed by your program. Notice that it is left up to you how to get the "specific word" into your program.  Some ideas include:

* Hardwire it into your program
* Get it as (one more) command line argument
* Ask the user to type the word in the keyboard and read it into your program
* Perhaps, get in a dialogue with the user and allow them to enter, through the keyboard, more than
one such words.



### What to submit

 Submit to Gradescope your `WordFrequenciesDirectory_Hash.java` and your **testing transcript**  (running your program on the DataFiles directory you downloaded).







<br/>

# Homework 10, Part B: Trees

## Exercise: Tree Terminology

This exercise tests your understanding of some definitions for trees. Consider the following tree:

<img src="_images/figs/tree.png" />

1. Produce a preorder traversal of this tree.
2. Produce an inorder traversal of this tree.
3. Produce a postorder traversal of this tree.
4. Produce a level-order traversal of this tree.
5. Draw an array to represent this tree using the computed links implementation strategy.
6. Draw an array to represent this tree using the stored links implementation strategy. For this question, place the nodes in the array in alphabetical order.
Use -1 to denote the location of a child that does not exist.
7. What is the big-O time complexity of the find operation in the LinkedBinaryTree class?
8. What is the time complexity of the inorder operation in the LinkedBinaryTree class?



### What do submit

Submit to gradescope a single file, `TreeTerminology.pdf`, containing your answers.

-->


