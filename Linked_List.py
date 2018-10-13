###MODIFIED POST-SUBMISSION DO NOT USE FOR CS241###

class Linked_List :

# ------------------------------------------------------------------------------------------ #

    class __Node :
    
        def __init__(self, val, next_val = None , prev_val = None) :

            # declare and initialize the private attributes
            # for objects of the Node class.

            self.val = val
            self.next = next_val
            self.prev = prev_val

# ------------------------------------------------------------------------------------------ #

    def __init__(self) :

        # declare and initialize the private attributes
        # for objects of the sentineled Linked_List class

        self.__header = self.__Node("HEADER")
        self.__trailer = self.__Node("TRAILER")
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0
    
    def __len__(self) :

        # return the number of value-containing nodes in 
        # this list.

        return self.__size

    def append_element(self, val) :

        # increase the size of the list by one, and add a
        # node containing val at the new tail position. this 
        # is the only way to add items at the tail position.

        newest = self.__Node(val , self.__trailer)

        if self.__size == 0 :

            self.__header.next = newest
            newest.next = self.__trailer
            newest.prev = self.__header
            self.__trailer.prev = newest
            self.__size += 1

        else :

            old_end = self.__trailer.prev
            old_end.next = newest
            newest.next = self.__trailer
            self.__trailer.prev = newest
            newest.prev = old_end
            self.__size += 1

    def insert_element_at(self, val, index) :

        # assuming the head position (not the header node)
        # is indexed 0, add a node containing val at the 
        # specified index. If the index is not a valid 
        # position within the list, raise an IndexError 
        # exception. This method cannot be used to add an 
        # item at the tail position.

        if index >= self.__size or index < 0 :

            raise IndexError

        newest = self.__Node(val)
        current = self.__header.next

        if index == 0 :

            self.__header.next = newest
            current.prev = newest
            newest.prev = self.__header
            newest.next = current
            self.__size += 1

        elif float(self.__size / 2) <= index :

            current = self.__trailer.prev

            for i in range((self.__size - index) - 1) :

                current = current.prev

            prev_element = current.prev
            newest.prev = prev_element
            prev_element.next = newest
            current.prev = newest
            newest.next = current
            self.__size += 1
        
        else :

            for i in range(index - 1) :

                current = current.next

            prev_element = current.next
            newest.next = prev_element
            prev_element.prev = newest
            current.next = newest
            newest.prev = current
            self.__size += 1

    def remove_element_at(self, index) :

        # assuming the head position (not the header node)
        # is indexed 0, remove and return the value stored 
        # in the node at the specified index. If the index 
        # is invalid, raise an IndexError exception.

        if index >= self.__size or index < 0 :

            raise IndexError

        current = self.__header.next

        if index == 0 :

            deleted_val = current.val
            new_start = self.__header.next.next
            self.__header.next = new_start
            new_start.prev = self.__header
            self.__size -= 1
            return deleted_val

        elif index == self.__size - 1 :

            current = self.__trailer.prev
            deleted_val = current.val
            new_end = current.prev
            new_end.next = self.__trailer
            self.__trailer.prev = new_end
            self.__size -= 1
            return deleted_val

        elif float(self.__size / 2) <= index :

            current = self.__trailer.prev

            for i in range((self.__size - index) - 2) :

                current = current.prev

            deleted_val = current.prev.val
            val_after_del = current.prev.prev
            current.prev = val_after_del
            val_after_del.next = current
            self.__size -= 1
            return deleted_val

        else :

            for i in range(index - 1) :

                current = current.next

            deleted_val = current.next.val
            val_after_del = current.next.next
            current.next = val_after_del
            val_after_del.prev = current
            self.__size -= 1
            return deleted_val

    def get_element_at(self, index) :

        # assuming the head position (not the header node)
        # is indexed 0, return the value stored in the node 
        # at the specified index, but do not unlink it from 
        # the list. If the specified index is invalid, raise 
        # an IndexError exception.

        if index >= self.__size or index < 0 :

            raise IndexError

        elif index == 0 :

            return self.__header.next.val
            
        elif index == self.__size - 1 :

            return self.__trailer.prev.val

        elif float(self.__size / 2) <= index :

            current = self.__trailer.prev

            for i in range((self.__size - index) - 1) :

                current = current.prev

            return current.val

        else :

            current = self.__header.next

            for i in range(index) :

               current = current.next

            return current.val
            

    def rotate_left(self) :

        # rotate the list left one position. Conceptual indices
        # should all decrease by one, except for the head, which
        # should become the tail. For example, if the list is
        # [ 5, 7, 9, -4 ], this method should alter it to
        # [ 7, 9, -4, 5 ]. This method should modify the list in
        # place and must not return a value.

        if self.__size <= 1 :

            return

        old_start = self.__header.next
        old_end = self.__trailer.prev
        new_start = old_start.next
        self.__header.next = new_start
        self.__trailer.prev = old_start
        old_start.next = self.__trailer
        new_start.prev = self.__header
        old_start.prev = old_end
        old_end.next = old_start

    def change_val(self , index , newval) :

        if index >= self.__size or index < 0 :

            raise IndexError

        elif index == 0 :

            self.__header.next.val = newval

        else: 

            current = self.__header.next

            for i in range(index) :

               current = current.next

            current.val = newval

    def contains_element(self , val) :

        if self.__size == 0 :

            raise IndexError

        else :

            current = self.__header.next

            for i in range(self.__size) :

                if current.val == val :

                    return True

                else :

                    current = current.next

            return False



    def __str__(self) :

        # return a string representation of the list's
        # contents. An empty list should appear as [ ].
        # A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ].
        # You may assume that the values stored inside of the
        # node objects implement the __str__() method, so you
        # call str(val_object) on them to get their string
        # representations.

        if self.__size == 0 :

            out_txt = "[ ]"
            return out_txt

        else :

            out_txt = "[ "

            for element in self :

                out_txt = out_txt + (str(element)) + ", "

            out_txt = out_txt[:-2] + " ]"
            return out_txt
        
    def __iter__(self) :

        # initialize a new attribute for walking through your list

        self.__loop_val = self.__header.next
        return self

    def __next__(self) :

        # using the attribute that you initialized in __iter__(),
        # fetch the next value and return it. If there are no more 
        # values to fetch, raise a StopIteration exception.

        __out_val = self.__loop_val.val

        if __out_val == "TRAILER" :

            raise StopIteration

        self.__loop_val = self.__loop_val.next
        return __out_val

# ------------------------------------------------------------------------------------------ #

if __name__ == '__main__' :

    # Your test code should go here. Be sure to look at cases
    # when the list is empty, when it has one element, and when 
    # it has several elements. Do the indexed methods raise exceptions
    # when given invalid indices? Do they position items
    # correctly when given valid indices? Does the string
    # representation of your list conform to the specified format?
    # Does removing an element function correctly regardless of that
    # element's location? Does a for loop iterate through your list
    # from head to tail? Your writeup should explain why you chose the
    # test cases. Leave all test cases in your code when submitting.

# ------------------------------------------------------------------------------------------ #

    def test_insert_element_at(test_linked_list , test_val , test_index) :

        print("List before insertion:" , test_linked_list)
        test_linked_list.insert_element_at(test_val , test_index)
        print("List after insertion:" , test_linked_list)

    def test_append_element(test_linked_list , test_val) :

        print("List before appending:" , test_linked_list)
        test_linked_list.append_element(test_val)
        print("List after appending:" , test_linked_list)

    def test_remove_element_at(test_linked_list , test_index) :

        print("List before removal:" , test_linked_list)
        test_removed_val = test_linked_list.remove_element_at(test_index)
        print("Removed element value:" , test_removed_val)
        print("List after removal:" , test_linked_list)

    def test_get_element_at(test_linked_list , test_index) :

        print("List: " , test_linked_list)
        test_out_val = test_linked_list.get_element_at(test_index)
        print("Value at index" , test_index , "is" , test_out_val)

    def test_rotate_left(test_linked_list) :

        print("List before rotation:" , test_linked_list)
        test_linked_list.rotate_left()
        print("List after rotation:" , test_linked_list)

# ------------------------------------------------------------------------------------------ #

    test_loop = True
    test_list = Linked_List()

    while test_loop == True :

        print()
        print("Choose a test to run:")
        print("1) Print your test list and its length")
        print("2) Print the value of an element at a specified index")
        print("3) Insert an element at a specified index")
        print("4) Remove an element at a specified index")
        print("5) Append an element to the end of the list")
        print("6) Rotate all values left")
        print("7) Clear entire list")
        print("8) Run Josephus problem on current list")
        print("0) Exit the program")
        print()
        choice_string = str(input("Enter choice: "))

        if choice_string == "0" :

            test_loop = False

        elif choice_string == "1" :

            print(test_list)
            print("List length:" , len(test_list))

        elif choice_string == "2" :

            test_index = int(input("Enter desired index value: "))
            test_get_element_at(test_list , test_index)

        elif choice_string == "3" :

            test_input_val = int(input("Enter desired value to insert: "))
            test_index = int(input("Enter desired index location to place new value: "))
            test_insert_element_at(test_list , test_input_val , test_index)

        elif choice_string == "4" :

            test_index = int(input("Enter desired index location to remove value: "))
            test_remove_element_at(test_list , test_index)

        elif choice_string == "5" :

            test_val = int(input("Enter desired value to append: "))
            test_append_element(test_list , test_val)

        elif choice_string == "6" :

            test_rotate_left(test_list)

        elif choice_string == "7" :

            print("List before clearing:" , test_list)
            test_list = Linked_List()
            print("Cleared list:" , test_list)

        elif choice_string == "8" :

            print("Initial order:" , test_list)
            count = 1

            for i in range(len(test_list) - 1) :

                test_list.rotate_left()
                test_list.remove_element_at(0)
                print(test_list)
                count += 1

            print("The survivor is:" , test_list.get_element_at(0))