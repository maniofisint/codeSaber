
class GC():

    def __init__(self, max = 100):
        self.max = max
        self.avail = [i for i in range(self.max)]
        self.head = 0
        self.next = [None]*self.max
        self.down = [None]*self.max
        self.tag = [None]*self.max

        for i in range(self.max):
            if i == self.max-1:
                self.next[i] = None
            else:
                self.next[i] = i+1

        self.label = [None]*self.max
        self.lists = []
        self.deleted_lists = []

    def alloc(self):
        if self.head == None:
            Exception('no space')
        x = self.head
        self.head = self.next[self.head]
        return x

    def make_list(self, name, exp, save= True):
        l = list(exp)
        head = self.head
        if save == True:
            self.lists.append([name, head])

        for i in range(len(l)):
            if i == '(' and i != 0:
                a0 = a1 = 0
                u = []
                while a0 != a1 and a0 != 0:
                    u.append(l[i])
                    if l[i] == '(':
                        a0 += 1
                    if l[i] == ')':
                        a1 += 1
                u = u[1 , len(u)-1]
                self.down[head] = self.next[head]
                self.make_list(name,u, False)

            else:
                x = self.alloc()
                head = x
                self.label[x] = l[i]
                self.tag[x] = name

    def print_by_location(self,location,list_name):
        while self.tag[location] == list_name:
            print(self.label[location], end=' ')
            if self.down[location]!= None and self.tag[self.down[location]] == list_name:
                self.print_by_location(self.down[location],list_name)
            location = self.next[location]

    def print_list(self, list_name):
        for i in self.lists:
            if i[0] == list_name:
                head = i[1]
                self.print_by_location(head,list_name)
                print('\n')
                break

    def change_tag_by_location(self,location,list_name, new_name):
        while self.tag[location] == list_name:
            self.tag[location] == new_name
            if self.down[location] != None and self.tag[self.down[location]] == list_name:
                self.change_tag_by_location(self.down[location], list_name, new_name)
            location = self.next[location]

    def change_tag(self, list_name, new_name):
        for i in self.lists:
            if i[0] == list_name:
                head = i[1]
                self.change_tag_by_location(head,list_name,new_name)
                self.lists.remove(i)
                break


    def make_child(self, parent_name , child_name , node_num):
        name1 = parent_name ; name2 = child_name
        if name2 == name1:
            raise Exception('same!')
        a = 0
        for i in self.lists:
            if name1 == i[0]:
                head_1 = i[1]
                a+= 1
                if a == 2:
                    break
            elif name2 == i[0]:
                head_2 = i[1]
                a+=1
                if a== 2:
                    break
        index = head_1
        for i in range(int(node_num-1)):
            index = self.next[index]
        if self.down[index] == None and self.tag[index] == name1:
            self.down[index] == head_2
            self.change_tag(name2 , name1)
        else:
            raise Exception('invalid request')

    def del_by_location(self, location, list_name):
        tail = location
        while self.next[tail]!= None and self.tag[tail] == list_name:
            tail = self.next[tail]
        while self.tag[location] == list_name:
            self.label[location] = None
            if self.down[location]!= None and self.tag[self.down[location]] == list_name:
                new_tail = self.del_by_location(self.down[location], list_name)
                self.next[tail] = self.down[location]
                tail = new_tail
            location = self.next[location]

    def del_list(self, list_name):
        for i in self.lists:
            if i[0] == list_name:
                head = i[1]
                self.del_by_location(head, list_name)
                self.deleted_lists.append([list_name,head])
                break

    def gc(self):
        for list in self.deleted_lists:
            tail= list[1]
            head = tail
            while self.tag[tail] == list[0]:
                tail = self.next[tail]
            self.next[tail] == self.head
            self.head = head
            self.lists.remove(list)









