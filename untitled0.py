from tkinter import*
root=Tk()
root.geometry("1000x1000")
root.title("Fibonacci Series")
root.configure(background="blue")

lbl_1=Label(root,text="Fibonacci Series",font=("Arial",15))
lbl_1.place(relx=0.5,rely=0.25,anchor=CENTER)

lbl_2=Label(root,text="")
lbl_2.place(relx=0.5,rely=0.8, anchor=CENTER)

lbl_3=Label(root,text="Enter the number of terms you want")
lbl_3.place(relx=0.3,rely=0.4,anchor=CENTER)

input=Entry(root)
input.place(relx=0.7,rely=0.4,anchor=CENTER)

def fibo():
    first=0
    second=1
    terms=int(input.get())
    sum=0
    counter=1
    
    while counter<=terms:
        print(sum)
        lbl_2["text"]+=str(sum)+" "
        first=second
        second=sum
        sum=first+second
        
        counter=counter+1
        
    

btn=Button(root,text="Generate",command=fibo)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)




   
    
root.mainloop()