import data_structures as ds
# from data_structures import stack


def main():
    s = ds.stack.Stack()
    s.push("4")
    s.push("%")
    print("Peeked", s.peek())
    top = s.pop()
    print("Popped", top)
    print("Peeked", s.peek())
    if s.isEmpty():
        print("Stack is empty")
    else:
        print("Stack is NOT empty")


if __name__ == '__main__':
    main()
