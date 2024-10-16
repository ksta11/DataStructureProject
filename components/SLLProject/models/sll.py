import pygame
from models.color import Color

color = Color()

class Node:
    def __init__(self, value):
        self.data_node = value
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_initial_node(self, value):
        if self.size == 9:
            return 0
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return 1

    def add_final_node(self, value):
        if self.size == 9:
            return 0
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return 1

    def add_index_node(self, value, index):
        if self.size == 9:
            return 0
        if index < 0 or index > self.size:
            return 2
        if index == 0:
            return self.add_initial_node(value)
        if index == self.size:
            return self.add_final_node(value)
        new_node = Node(value)
        prev_node = None
        current_node = self.head
        for i in range(index):
            prev_node = current_node
            current_node = current_node.next
        
        prev_node.next = new_node
        new_node.next = current_node
        self.size += 1
        return 1
    
    def add_odd_positions_node(self, value):
        if self.head is None:
            return self.add_final_node(value)
        if self.size >= 5:
            return 0
        
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        current_node = self.head
        self.size += 1

        while current_node.next is not None:
            new_node = Node(value)
            current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            current_node = new_node
            self.size += 1
        return 1


    def delete_initial_node(self):
        if self.head is None:
            return 0
        else:
            current_node = self.head.next
            self.head = current_node
        self.size -= 1
        return 1

    def delete_final_node(self):
        if self.head is None:
            return 0
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev_node = self.head
            current_node = self.head.next
            while current_node.next is not None:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = None
            self.tail = prev_node
        self.size -= 1
        return 1

    def delete_index_node(self, index):
        if index < 0 or index > self.size-1:
            return 2
        if index == 0:
            return self.delete_initial_node()
        if index == self.size-1:
            return self.delete_final_node()
        prev_node = None
        current_node = self.head
        for i in range(index):
            prev_node = current_node
            current_node = current_node.next
        
        prev_node.next = current_node.next
        current_node.next = None
        self.size -= 1
        return 1

    def delete_duplicate_nodes(self):
        if self.head is None:
            return 0
        if self.head == self.tail:
            return 2
        prev_node = self.head
        comparative_nodes_values = [self.head.data_node]
        current_node = self.head.next
        while current_node is not None:
            if current_node.data_node in comparative_nodes_values:
                prev_node.next = current_node.next
                self.size -= 1
                if current_node.next is None:
                    self.tail = prev_node
            else:
                comparative_nodes_values.append(current_node.data_node)
                prev_node = current_node
            current_node = current_node.next
        return 1

    def delete_even_nodes(self):
        if self.head is None:
            return 0
        if self.head == self.tail:
            return 2
        current_node = self.head
        while current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
            if current_node.next is None:
                self.tail = current_node
            current_node = current_node.next
            self.size -= 1
        return 1
    
    def delete_every_two_nodes(self):
        if self.head is None:
            return 0
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return 1
        self.delete_initial_node()
        current_node = self.head
        while current_node.next is not None and current_node.next.next is not None:
            current_node = current_node.next
            next_node = current_node.next
            current_node.next = next_node.next
            self.size -= 1
            if current_node.next is None:
                self.tail = current_node
                return 1
            current_node = current_node.next
        return 1

    def reverse_nodes(self):
        if self.head is None:
            return 0
        if self.head == self.tail:
            return 2
        new_head = self.tail
        current_node = self.head
        reverse_node = new_head
        while self.head.next is not None:
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            reverse_node.next = current_node
            reverse_node = reverse_node.next
            current_node = self.head
        self.head = new_head
        self.tail = reverse_node
        return 1


    def print_sll(self):
        if self.head is None:
            return None
        height = 115
        width = self.size * 135
        image = pygame.Surface((width, height))
        image.fill(color.BACKGROUND_COlOR)
        current_node = self.head
        x = 0
        y = 0
        while current_node is not None:
            image.blit(current_node.data_node.image, (x, y))
            x += 135
            current_node = current_node.next
        return image
