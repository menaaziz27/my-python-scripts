def unpacking(name,*skills):
    print(f"Hello {name} your skills are : ")
    for skill in skills:
        print(skill)

unpacking("mina" , "HTML", "CSS", "Python", "OOP", "xamarin")