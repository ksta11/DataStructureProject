import pygame
from models.color import Color

color = Color()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class AVL: #Arbol balanceado
    def __init__(self):
        self.root = None
        self.size = 0
        self.count_trail = 0
        self.initial_time = None
        self.current_time = None
        self.type_trail = 0
        self.level = 0

    def add_Node(self, value):
        if not self.root:
            self.root = Node(value)
            self.size += 1
        else:
            node = Node(value)
            self.add_recursive_node(node, self.root)

    def add_recursive_node(self, node, current_node):
        if node.value < current_node.value:
            #El nodo se agregaria a la izquierda
            if current_node.left is None:
                current_node.left = node
                self.size += 1
            else:
                self.add_recursive_node(node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = node
                self.size += 1
            else:
                self.add_recursive_node(node, current_node.right)

    def draw(self, screen):
        self.show_tree(screen, self.root, 445, 85, 400)
        if self.type_trail == 1:
            self.draw_inorder(screen)
        if self.type_trail == 2:
            self.draw_preorder(screen)
        if self.type_trail == 3:
            self.draw_postorder(screen)

    def show_tree(self, screen, node, x, y, width):
        if node is not None:
            width = int(width*(1/2))
            rect_circle = pygame.rect.Rect(x, y, 30, 30)
            pygame.draw.circle(screen, color.BLACK, rect_circle.topleft, rect_circle.width)
            font = pygame.font.SysFont("Tw Cen MT", 30)
            text_value = font.render(str(node.value), True, color.WHITE)
            
            if node.left is not None:
                pygame.draw.line(screen, color.BLACK, (x, y), (x - width, y + 60), 3)
                self.show_tree(screen, node.left, x - width, y + 65, width)
            if node.right is not None:
                pygame.draw.line(screen, color.BLACK, (x, y), (x + width, y + 60), 3)
                self.show_tree(screen, node.right, x + width, y + 65, width)
            screen.blit(text_value, (x - 8, y - 7))

    def draw_inorder(self, screen):
        if self.count_trail < self.size:
            if self.current_time - self.initial_time > (self.count_trail + 1) * 1000:
                self.count_trail += 1
            self.level = 0
            self.show_inorder_tree(screen, self.root, 445, 85, 400)
        else:
            self.count_trail = 0
            self.initial_time = None
            self.current_time = None
            self.type_trail = 0
            self.level = 0

    def show_inorder_tree(self, screen, node, x, y, width):
        if node is not None:
            width = int(width*(1/2))
            self.show_inorder_tree(screen, node.left, x - width, y + 65, width)

            if self.level == self.count_trail:
                rect_circle = pygame.rect.Rect(x, y, 30, 30)
                pygame.draw.circle(screen, color.BLUE, rect_circle.topleft, rect_circle.width)
                font = pygame.font.SysFont("Tw Cen MT", 30)
                text_value = font.render(str(node.value), True, color.WHITE)
                screen.blit(text_value, (x - 8, y - 7))
                self.level += 1
            elif self.level < self.count_trail:
                self.level += 1
            
            self.show_inorder_tree(screen, node.right, x + width, y + 65, width)

    def draw_preorder(self, screen):
        if self.count_trail < self.size:
            if self.current_time - self.initial_time > (self.count_trail + 1) * 1000:
                self.count_trail += 1
            self.level = 0
            self.show_preorder_tree(screen, self.root, 445, 85, 400)
        else:
            self.count_trail = 0
            self.initial_time = None
            self.current_time = None
            self.type_trail = 0
            self.level = 0

    def show_preorder_tree(self, screen, node, x, y, width):
        if node is not None:
            width = int(width*(1/2))

            if self.level == self.count_trail:
                rect_circle = pygame.rect.Rect(x, y, 30, 30)
                pygame.draw.circle(screen, color.RED, rect_circle.topleft, rect_circle.width)
                font = pygame.font.SysFont("Tw Cen MT", 30)
                text_value = font.render(str(node.value), True, color.WHITE)
                screen.blit(text_value, (x - 8, y - 7))
                self.level += 1
            elif self.level < self.count_trail:
                self.level += 1
            
            self.show_preorder_tree(screen, node.left, x - width, y + 65, width)
            self.show_preorder_tree(screen, node.right, x + width, y + 65, width)

    def draw_postorder(self, screen):
        if self.count_trail < self.size:
            if self.current_time - self.initial_time > (self.count_trail + 1) * 1000:
                self.count_trail += 1
            self.level = 0
            self.show_postorder_tree(screen, self.root, 445, 85, 400)
        else:
            self.count_trail = 0
            self.initial_time = None
            self.current_time = None
            self.type_trail = 0
            self.level = 0

    def show_postorder_tree(self, screen, node, x, y, width):
        if node is not None:
            width = int(width*(1/2))

            self.show_postorder_tree(screen, node.left, x - width, y + 65, width)
            self.show_postorder_tree(screen, node.right, x + width, y + 65, width)
            
            if self.level == self.count_trail:
                rect_circle = pygame.rect.Rect(x, y, 30, 30)
                pygame.draw.circle(screen, color.GREEN, rect_circle.topleft, rect_circle.width)
                font = pygame.font.SysFont("Tw Cen MT", 30)
                text_value = font.render(str(node.value), True, color.WHITE)
                screen.blit(text_value, (x - 8, y - 7))
                self.level += 1
            elif self.level < self.count_trail:
                self.level += 1

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Caso 1: Nodo sin hijos o con un solo hijo
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Caso 2: Nodo con dos hijos
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)

        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key)
            self.inorder_traversal(node.right)

    def delete_node(self, value, side):
        father_node_delete = self.find_father(self.root, value)
        node_delete = self.find_node(self.root, value)
        print(father_node_delete.value)
        print(node_delete.value)
        if side == 0:
            node_sucessor = self.find_node_sucessor(node_delete.left, side)
        elif side == 1:
            node_sucessor = self.find_node_sucessor(node_delete.right, side)
        
        if node_sucessor is None:
            if side == 0:
                node_delete = node_delete.right
            if side == 1:
                node_delete = node_delete.left
        elif node_sucessor is not None:
            if side == 0:
                node_sucessor.right = node_delete.right
            if side == 1:
                node_sucessor.left = node_delete.left
            node_delete = node_sucessor
            if father_node_delete is None:
                if side == 0:
                    node_sucessor.left = self.root.left
                    self.root = node_sucessor
                if side == 1:
                    node_sucessor.right = self.root.right
                    self.root = node_sucessor
            else:
                if father_node_delete.left.value == value:
                    father_node_delete.left = node_sucessor
                else:
                    father_node_delete.right = node_sucessor

    def find_node_sucessor(self, node, side):
        if node is None:
            return None
        
        if side == 0:
            node_sucessor = self.find_node_sucessor(node.right, side)
        elif side == 1:
            node_sucessor = self.find_node_sucessor(node.left, side)

        if node_sucessor is None:
            return node
        else:
            if side == 0:
                node_new = node_sucessor
                self.add_recursive_node(node, node_new)
                node.right = None
                return node_new
            elif side == 1:
                node_new = node_sucessor
                self.add_recursive_node(node, node_new)
                node.left = None
                return node_new


    def find_node(self, node, value):
        if node is not None:
            if node.value == value:
                return node
            elif node.value > value:
                return self.find_node(node.left, value)
            else:
                return self.find_node(node.right, value)
        else:
            return None
        
    def find_father(self, node, value):
        if node is not None:
            if node.value == value:
                return None
            elif node.value > value:
                result = self.find_father(node.left, value)
            else:
                result = self.find_father(node.right, value)

            if result is None:
                return node
            else:
                return result
        else:
            return None