userids = ['ravi@123','raju@456','salman@153','akshay@153']
places = ["delhi",'noida','lucknow','kolkata']
courses = ['data science','data analysis','big data','backend']

running_courses = ['data sceince','data analysis','python','java']
num_of_course = len(running_courses)

running_places = ['Noida','Delhi','Lucknow','Chennai']
num_of_places = len(running_places)

operation = int(input('''1. Find info of Student
2. Add Student
3. Show Data
4. Delete the Data
Choose::::'''))

if operation ==1:
    '''----------------------Find Info: ----------------------'''
    userID = input('Enter the UserID: ')
    if userID in userids:
        ind = userids.index(userID)
        print(f'''User ID: {userids[ind]}
Place: {places[ind]}
Course: {courses[ind]} ''')
    '''----------------------Find Info: ----------------------'''
elif operation ==2:
    '''--------------ADD A STUDENT----------------'''
    userid = input("user id: ")
    if userid not in userids:
        '''----------------------Choose Places----------------------'''
        for n, p in enumerate(running_places):
            print(f'{n + 1}. {p}')

        while (True):
            place_code = int(input('enter the place code: '))
            if (place_code <= num_of_places and place_code > 0):
                place = running_places[place_code - 1]
                print(f'you chose: {place}.')
                break
            else:
                print(f'We have {num_of_places} as of now.')
        '''----------------------Choose Places----------------------'''
        '''----------------------Choose Courses----------------------'''
        for n, c in enumerate(running_courses):
            print(f'{n + 1}. {c}')

        while (True):
            course_code = int(input('enter the course code: '))
            if (course_code <= num_of_course and course_code > 0):
                course = running_courses[course_code - 1]
                print(f'you chose: {course}.')
                break
            else:
                print(f'We have {num_of_course} as of now.')
        '''----------------------Choose Courses----------------------'''
        userids.append(userid)
        places.append(place)
        courses.append(course)
    else:
        print(f'{userid} is alraedy in list')
    '''--------------ADD A STUDENT----------------'''
elif operation ==3:
    '''--------------SHOW DATA-----------------'''
    print(f'userids | place | courses')
    for u,p,c in zip(userids,places,courses):
        print(f'{u} | {p} | {c}')
    '''--------------SHOW DATA-----------------'''
elif operation ==4:
    '''--------------------Delete the data--------------------'''
    DeleteUser = input('enter the delete the student: ')
    if DeleteUser in userids:
        ind = userids.index(DeleteUser)
        deleteuserid = userids.pop(ind)
        deleteplace = places.pop(ind)
        deletecourse = courses.pop(ind)

    else:
        print(f'this {DeleteUser} is not in list')
'''--------------------Delete the data--------------------'''
