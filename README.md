# Dance Class Finder Application

## Project Description:

The Dance Class Finder is an application that helps users search for dance classes in New York City without having to visit each studio's website individually. The application collects relevant and up-to-date data to populate its database and provide users with a comprehensive and convenient way to search for dance classes in NYC. The entities in the application include: Studio, Class, Time-slot, Instructor, and Student. The relationships between these entities include Studio-Class, Class-Time-slot, Class-Instructor, Student-Class, Studio-Instructor, Studio-Student, and Instructor-Student.

The attributes for each entity include:

Studio (Studio_ID, Name, Address, Phone_Number)
Class (Class_ID, Dance_Style, Dance_Level, Price, Room_Number, Duration)
Time-slot (Time_Slot_ID, Day, Time (StartTime, EndTime))
Instructor (Instructor_ID, Name (FirstName, LastName), Bio, Instagram)
Student (Student_ID, Name(FirstName, LastName), interest, Email, Phone_Number)

## Data Plan:

The data plan for the Dance Class Finder database involves gathering information from dance studios in NYC. This includes information about each studio, such as its name, address, and phone number, as well as information about the classes offered at each studio, such as the dance style, level, price, instructor name, and class schedule. The data will be collected through web scraping and direct collection of publicly available data.


## Web-Front Description

The Dance Class Finder application will have a simple and intuitive interface for users to search for dance classes in NYC. The main entities involved in this process will be the student (users), dance studios, classes, instructors, and time-slots.

Upon accessing the website, users will be able to use a search bar to enter specific criteria such as location, day, time, dance level, instructor, or price range to filter the available classes and find the one that best suits their needs. The results will be displayed in a user-friendly manner, with each class listed along with relevant information such as the studio name, instructor name, and class schedule. Users will also have the option to create an account, which will allow them to enroll in a dance class.

The DanceFinder app is a web-based application designed to help users easily find dance classes in New York City.
