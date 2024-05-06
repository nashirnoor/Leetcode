        
        head = reverse(head)
        cur = head
        cur_max = cur.val
        while cur.next:
            if cur.next.val < cur_max:
                cur.next = cur.next.next
            else:
                cur_max = cur.next.val
                cur = cur.next
        return reverse(head)


            return prev
                prev, cur = cur, tmp
                cur.next = prev
[
