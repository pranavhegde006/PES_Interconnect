## Programming paradigms

-   Procedural
-   Object oriented
-   Functional
-   Generic
-   Object based
-   Exception based


## Object oriented Programming

-  ### Type
    -   A set of values and a set of operators
    -   specifies what it can do
    -   not how it can do
-  ### Class
    -   User defined type
    -   pure class is like a type
    -   class = what it can do + how it can do
    -   CLASS = INTERFACE (type) + IMPLEMENTATION
   
-  ### The important concept that need to be supported by OOP are:
    -   #### Abstraction
        -   Capture the essential features, ignore the non essential features
        -   abstraction of an object depends on the observer
        -   eg: earth from pov of an astronaut to a geologist, bank cheque with a POV of printer, banker, customer etc


    -  #### Encapsulation
        -   Put together attributes and behaviours
        -   access control
        -   Hiding the implementation
        -   Not about security, use some encryption techniques or otherwise
        -   hide what could change, expose what should not change
        -   hide implementation, expose interface


        -  ##### Iterator
            -   Consider searching on a data structure
            -   We have various ways to return the desired functionality
                -   We could just print “FOUND” when the element is found and “NOT FOUND” when the element is not found.
                -   We could make it a boolean function returning true or false when the element is found or not.
                -   We could return the element itself
                -   We could return the index of that element
                -   We could return a pointer to that element
                -   We could return an opaque object called iterator
                    -   This iterator object will never change forever because once it is returned to the user, it contains all the useful information which would be useful to the user in the future
                    -   This iterator object contains the details of the pointer, index, key value, pointer to the next and previous elements etc
        -  ##### Eager vs lazy
            -   eager ds will return the address/pointer
            -   lazy ds will just return the latest value


    -   #### Composition
        -   “has a” relationship
        -   flexible, dynamic
        -   runtime binding between objects
        -   rescue mechanism


    -  #### Inheritance
        -   “is a” relationship
        -   compile time binding between classes
        -   also rescue mechanism
        -   avoid if statements based on values of attributes
        -   should follow Liskov’s property
            -   property of substitution
                -   replace an object of a base class by an object of a derived class
                -   inheritance of the base class should also be interface of the derived class


    -  #### Polymorphism
        -   many forms
        -   same interface: calls different implementations based on what we have at runtime