PROBLEM 1:
Identify whether the linked list is cyclic or not?
Solution:

def circular_list(head):
	fnode=head
	lnode=head
	while lnode:
    	lnode=lnode.Next
    	if lnode==fnode:
        	print("Circular linked list")
    	else:
        	print("No Circular linked list")
			
PROBLEM 3:
Find The Longest Palindrome From given String.eg.madam,civic,radar.
Solution:

string1=input("Enter a string:")
rev=string1[::-1]
if string1==rev:
	print("Longest palindrome sequence:",string1)
else:
    for j in range(2,len(string1)):
        for i in range(j,len(string1)+1):
            rev1=string1[i-j:i]
        if rev1==rev1[::-1]:
            print("Longest palindrome sequence:",rev1)
