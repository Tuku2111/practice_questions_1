# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


lst = [10,40,20]
m_lst = tuple(" ".join(map(str,lst)).split())
out = f"select * from {m_lst}"
print(out)


word1 = "abc"
word2 = "pq"
res = ''
for i in range(max(len(word1),len(word2))):
    if len(word1) > i:
        res += word1[i]
    if len(word2) > i:
        res += word2[i]

print(res)