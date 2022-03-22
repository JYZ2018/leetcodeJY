            if not dfs(llst.next):
                return False
             
            print("finnaly llst.val is: ",llst)
            print("finally self.dummy1.val is: ",self.dummy1.val)
            if llst.val==self.dummy1.val:
                self.dummy1=self.dummy1.next
                return True
            else:
                return False
         
        return dfs(dummy2)
        '''
        
        # method 3 reverse late half of the list
        def end_of_first_half(head):
            slow,fast=head,head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow
         
        def reverse_list(head):
            previous= None
            current=head
            while current:
                next_node=current.next
                current.next=previous
                previous=current
                current=next_node
            return previous
        
        first_half=end_of_first_half(head)
        second_half=reverse_list(first_half.next)
        
        result=True
        first_position=head
        second_position=second_half
        while result and second_position:
            if first_position.val != second_position.val:
                result=False
            first_position=first_position.next
            second_position=second_position.next
        return result
        
                
       
        
        
        # my mistake, can't change dummy1 to dummy1.next during recursion
        '''
        dummy1=head
        dummy2=head
        def dfs(llst):
